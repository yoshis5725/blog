#
# ----- This function will allow the upload of pictures. It takes the picture that the user uploaded, converts the
# name of the picture to the user's username. It will assign it a file name, then convert that uploaded picture into a
# thumbnail and then finally return back the storage filename
#

import os
from PIL import Image  # installed pillow
from flask import url_for, current_app


def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]  # example.jpeg ---> jpeg

    # if myPic.jpeg was uploaded, then it is saved as username.jpeg. This is done for uniqueness
    storage_filename = str(username) + '.' + ext_type

    # telling flask where to save the profile picture
    filepath = os.path.join(current_app.root_path, 'static/profilePics', storage_filename)

    # ---- converting the pic into a thumbnail -----

    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
