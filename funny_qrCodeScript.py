import qrcode


video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=3
)

qr.add_data(video_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.show()

