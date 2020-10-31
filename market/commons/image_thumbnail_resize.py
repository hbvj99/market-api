import sys
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def resize_image(image, size, quality, upload_to, *args, **kwargs):
    image_temporary = Image.open(image).convert('RGB')
    output_io_stream = BytesIO()
    image_temporary.thumbnail(size, Image.ANTIALIAS)
    image_temporary.save(output_io_stream, format='JPEG', quality=quality, optimize=True)
    output_io_stream.seek(0)
    image = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % image.name.split('.')[0], upload_to,
                                 sys.getsizeof(output_io_stream), None)
    return image
