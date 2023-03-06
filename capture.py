# Importing Image class from PIL module
from PIL import Image
import pytesseract
import pyautogui
import time
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    # Open the image
    image = Image.open(image_path)

    # Extract text from the image using Tesseract OCR
    text = pytesseract.image_to_string(image)

    return text

time.sleep(15)

for i in range(10):
    power = ''
    current = ''
    while power == '' or current == '':
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'D:\\shots\\{}.png'.format(i))

        # Opens an image in RGB mode
        im = Image.open(r'D:\\shots\\{}.png'.format(i))
        
        # Setting the points for cropped image
        left_p = 1000
        top_p = 1000
        right_p = 1170
        bottom_p = 1200
        
        # Cropped image of above dimension
        # (It will not change original image)
        im1_p = im.crop((left_p, top_p, right_p, bottom_p))
        
        # Shows the image in image viewer
        # im1.show()
        # save image
        im1_p.save(r'D:\\power\\{}.png'.format(i))
        power = image_to_text(r'D:\\power\\{}.png'.format(i))

        # Setting the points for cropped image
        left_c = 800
        top_c = 1000
        right_c = 930
        bottom_c = 1090
        
        # Cropped image of above dimension
        # (It will not change original image)
        im1_c = im.crop((left_c, top_c, right_c, bottom_c))
        
        # Shows the image in image viewer
        # im1.show()
        #save image
        im1_c.save(r'D:\\current\\{}.png'.format(i))
        current = image_to_text(r'D:\\current\\{}.png'.format(i))

    power = float(power)
    power = str(power)
    current = float(current)
    current = str(current)

    im = Image.open(r'D:\\shots\\{}.png'.format(i))
    # Setting the points for cropped image
    left = 900
    top = 40
    right = 1050
    bottom = 97
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    # im1.show()

    #save image
    im1.save(r'D:\\title\\{}.png'.format(i))
    title = image_to_text(r'D:\\title\\{}.png'.format(i))
    
    # Opens a image in RGB mode
    im = Image.open(r'D:\\shots\\{}.png'.format(i))
    
    # Setting the points for cropped image
    left = 1220
    top = 1
    right = 1260
    bottom = 23
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
     
    # Shows the image in image viewer
    # im1.show()

    # save image
    im1.save(r'D:\\time\\{}.png'.format(i))

    time_ = image_to_text(r'D:\\time\\{}.png'.format(i))
    time_ = time_.replace(':', '.')
    time_ = float(time_)
    time_ = "{:.2f}".format(time_)
    time_ = str(time_)
    time_ = time_.replace('.', ':')

    file = open('plug_readings.txt', 'a')
    file.write('time, ' + time_ + ', ' + 'current, ' + current + ', ' + 'power, ' + power + ', ' + 'plug, ' + title + '\n')
    file.close()
    time.sleep(5)