import qrcode
import subprocess

# Define the data to be encoded in the QR code (xminds.com URL or relevant data)
data = "https://xminds.com"

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image to a file
img.save("xminds_qr_code.png")

# Open the QR code image using the default image viewer
subprocess.run(["xdg-open", "xminds_qr_code.png"])

