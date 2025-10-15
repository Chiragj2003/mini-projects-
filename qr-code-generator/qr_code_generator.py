import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = input("Enter text or URL to convert to QR code: ")

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
filename = "qrcode.png"
img.save(filename)
print(f"QR code saved as {filename}")
