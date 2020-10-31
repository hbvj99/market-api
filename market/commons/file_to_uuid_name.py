import os
import uuid


def get_user_profile_upload_path(_, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('user/profile-pictures/', filename)
