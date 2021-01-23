'''

author : Hari Prasad

Resources : 
    https://www.geeksforgeeks.org/python-convert-image-to-text-and-then-to-speech/
    https://stackoverflow.com/questions/62904506/2-usage-pytesseract-l-lang-input-file-on-google-colab

'''

import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify, url_for, redirect
from PIL import Image
import pytesseract

app = Flask(__name__)

UPLOAD_FOLDER               = './static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ['GET', 'POST'])
def login():

    image_path = None
    error_msg  = None

    if request.method == 'POST':
        file = request.files['file']

        if file.filename == '':
            error_msg="Please Upload Any Image"

        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path="./static/images/{}".format(filename)

            pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

            image_text = pytesseract.image_to_string(Image.open(image_path))
            text_file = open("./static/text/image_text.txt", "a")
            text_file.write(image_text)
            text_file.close()

    return render_template("index.html", error_msg=error_msg)

@app.route('/view_text', methods = ['GET', 'POST'])
def view_text():
    with open('./static/text/image_text.txt', 'r') as f: 
        return render_template('show_text.html', text=f.read())

@app.route('/clear_text', methods = ['GET', 'POST'])
def clear_text():
    
    text_file = open("./static/text/image_text.txt","r+")
    text_file.truncate(0)
    text_file.close()

    return redirect(url_for('view_text'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)