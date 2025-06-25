from flask import Flask, render_template, request, redirect,url_for
from main import generateCode

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_data = ''
    message = ''
    if request.method == 'POST':
        codeText = str(request.form['codeText'])
        if codeText:
            qr_code_data = generateCode(codeText)
        else:
            message = 'Please enter the text to generate QR code'
    
    return render_template ('qrcodegenerator.html', mesage = message, generateCode = qr_code_data)

if __name__ == '__main__':
    app.run(port=5002)
