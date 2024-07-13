import os
import pyqrcode
import png

# URL to be encoded in the QR code
url = pyqrcode.create('https://re-connect.ro/webinar/')

# Save the generated QR code as a PNG image
url.png('WebinarQR.png', scale=8)

# Open the saved image
os.system("start WebinarQR.png")
