
#imageBytes = os.path.getsize('image.gif')
import base64
import os
pach = "image.jpg"
imageBytes = os.path.getsize(pach)
print(imageBytes)


# with open("image.jpg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#     print(encoded_string)


# For both Python 2.7 and Python 3.x
#import base64
#with open("imageToSave.jpg", "wb") as fh:
#    fh.write(base64.decodebytes(encoded_string))
      

