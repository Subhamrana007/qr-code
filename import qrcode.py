import qrcode
from PIL import Image

qr=qrcode.QRCode(version = 1,
                 error_correction = qrcode.constants.ERROR_CORRECT_H,
                 box_size = 5,
                 border = 3,)
qr.add_data("https://humornama.com/wp-content/uploads/2020/11/Chala-Ja-Bsdk-meme-template.jpg")
qr.make(fit=True)
img=qr.make_image(fill_color="black",background_color="white")
img.save("sirf tere lie.png")