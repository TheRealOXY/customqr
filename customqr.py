import random
import qrcode
from PIL import Image

print('Enter QR data:')
x = input()
print('Enter box size:')
q = input()
print('Enter border size:')
z = input()
print('Enter file name:')
custom = input()
print('Enter background color: (HEX without #)')
bc = input()

qr = qrcode.QRCode(
    version=1,
    box_size=q,
    border=z
)

qr.add_data(x)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='#' + bc)
img.save(custom + '.png')
