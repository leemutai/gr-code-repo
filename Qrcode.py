import pyqrcode
import png
from pyqrcode import QRCode
QRstring = "................"# paste any url here
url = pyqrcode.create(QRstring)
url.png('Desktop\\qr.png', scale=8)
