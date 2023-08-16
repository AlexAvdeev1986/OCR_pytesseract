import pytesseract
from PIL import Image

# Откройте изображение с помощью Pillow (PIL)
image = Image.open('1111.png')

# Вызовите pytesseract для распознавания текста
text = pytesseract.image_to_string(image, lang='rus+eng')

print(text)