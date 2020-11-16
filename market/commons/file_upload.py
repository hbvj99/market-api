import os
import uuid

from rest_framework import exceptions

user_image_path = "user/image/"
product_image_path = 'products/image/'


def get_user_profile_upload_path(_, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    print(filename, user_image_path)
    return os.path.join(user_image_path, filename)


def validate_image_extension_size(file, extension, supported_extension, max_size_mb, *args, **kwargs):
    if extension not in supported_extension:
        raise exceptions.NotAcceptable({"message": "invalid file extension. i.e. jpg, jpeg, png are only supported."})
    file_size = file.size
    megabyte_limit = max_size_mb
    if file_size > megabyte_limit * 1024 * 1024:
        raise exceptions.NotAcceptable({"message": "file size cannot be greater than %sMB" % str(megabyte_limit)})
