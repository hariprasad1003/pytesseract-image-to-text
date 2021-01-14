'''

author : Hari Prasad

Resources : 
    https://www.geeksforgeeks.org/python-convert-image-to-text-and-then-to-speech/
    https://stackoverflow.com/questions/62904506/2-usage-pytesseract-l-lang-input-file-on-google-colab

'''


from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

image_text = pytesseract.image_to_string(Image.open('image.png'))
text_file = open("image_text.txt", "a")
text_file.write(image_text)
text_file.close()