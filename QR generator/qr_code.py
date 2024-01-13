import qrcode as qr
img = qr.make("https://github.com/")
img.save("qithub.png")