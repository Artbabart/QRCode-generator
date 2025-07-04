import qrcode
from io import BytesIO
import base64

def generateCode(text: str, img_name: str = 'QRCode.png') -> any:
    code = qrcode.QRCode(
        version= 1,
        box_size= 10,
        border= 4
    )

    code.add_data(text)
    code.make(fit=True)
    img = code.make_image(fill_color = 'black', back_color = 'white')
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    qrCode = f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"
    return qrCode