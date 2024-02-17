import tkinter as tk
from PIL import ImageTk, Image
import cv2
import numpy as np
from keras.models import load_model
import threading
from Image_Captioning import *
from caption import *


model = load_model('keras_model.h5')
labels = open('labels.txt', 'r').readlines()
def camOn():
    threading.Timer(57.0, camOn).start()
    global model, labels
    camera = cv2.VideoCapture(0)
    global textOutput
    global img, frameOutput
    ret, image = camera.read()
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    # cv2.imshow('Webcam Image', image)
    cv2.imwrite("b.jpg", image)
    img=ImageTk.PhotoImage(Image.open("b.jpg"))
    frameOutput=tk.Label(window, image=img)
    frameOutput.grid(row=3, column=1)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    # Normalize the image array
    image = (image / 127.5) - 1
    probabilities = model.predict(image)
    l=np.argmax(probabilities)
    print(labels[l])
    global captionOutput
    if l==3:
        x=caption_this_image("b.jpg")
        textOutput["text"]="Non-Threat"
        print(x)
        captionOutput["text"]=x
        textOutput["fg"]="green"
    else:
        x=predict_caption(l)
        textOutput["text"]="Threat"
        textOutput["fg"]="red"
        captionOutput["text"]=x
    camera.release()
    cv2.destroyAllWindows()
    
    
    
window=tk.Tk()
window.geometry("700x400")
greeting= tk.Label(window, text="Intelligent Surveillance System", font=("Arial", 20), fg="blue")
greeting.grid(row=0, column=1)
heading= tk.Label(window, text="Dashboard", font=("Arial", 15))
heading.grid(row=1, column=1)
startCam=tk.Button(window, text="Start Surveillance", width=15, height=2, bg="black", fg="white", font=("Arial", 15), command=camOn)
startCam.grid(row=3, column=0)

img=ImageTk.PhotoImage(Image.open("a.jpg"))
frameOutput=tk.Label(window, image=img)
frameOutput.grid(row=3, column=1)
captionOutput= tk.Label(window, text="------", font=("Arial", 15),wraplength=500, justify="center")
captionOutput.grid(row=4, column=1)
textOutput= tk.Label(window, text="Non-Threat", font=("Arial", 15), fg="green")
textOutput.grid(row=5, column=1)
window.mainloop()