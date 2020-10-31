import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from ...commons.image_thumbnail_resize import resize_image
from ...commons.models import BaseModel
from ...products.models.category import Category

User = get_user_model()


class Product(BaseModel):
    product_id = models.UUIDField(blank=False, null=False, unique=True, default=uuid.uuid4,
                                  editable=False)
    title = models.CharField(max_length=130, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=True, editable=False)
    description = models.TextField(blank=False, max_length=1500, default='')
    image = models.ImageField(upload_to='images/product/%Y/%m/%d/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=70, blank=True)
    votes = models.ManyToManyField(User, related_name='product_votes', blank=True, through="ProductVotes",
                                   through_fields=('product', 'user'))
    views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def votes_count(self):
        return self.votes.count()

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        if self.image:
            size = 1080, 960
            quality = 75
            upload_to = 'images/product/%Y/%m/%d/'
            self.image = resize_image(self.image, size, quality, upload_to)
        super().save(*args, **kwargs)

    def get_tags(self):
        tag = self.tags.split(',')
        return tag

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)


class ProductVotes(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
