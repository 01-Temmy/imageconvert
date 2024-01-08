import cv2
import pytesseract
import googletrans
import pyttsx3
import os
import sys


#asks user for image path e.g C:\\Users\\Temmy\\Pictures\\poem.jpg
image_path = input("Please input the path to your image: ")

#to check if the path exists
if os.path.exists(image_path):
    print('The image path exists.\n')
else:
    print("The specified file does not exists!")

    
#reads the image
img = cv2.imread(image_path)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#converts imaeg to text first
text = pytesseract.image_to_string(img)
print(text)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#ask user to pick whatever voice
voice_num = int(input("Please choose a voice, 1 for Female and 0 for male: "))
engine.setProperty('voice',voices[voice_num].id)
#sets the rate i.e 150 words per minute
engine.setProperty('rate', 200)
#asks user to input volume
voice_volume = float(input("Please set the volume from 0.0 to 1: "))
engine.setProperty('volume', 0.9)

engine.say(text)
engine.runAndWait()
engine.stop()
