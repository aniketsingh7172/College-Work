import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

content="RadheRadhe"
qr_code = pyqrcode.create(content)
qr_code.png("msg.png", scale=5)

img=Image.open("msg.png")
qr_content=decode(img)
print(qr_content[0].data.decode())