import tkinter
import tkfilebrowser
import cv2
import imutils
from PIL import Image
from PIL import ImageTk
from matplotlib import pyplot as plt


def cargar_imagen():
    global image1, img1, path


    path = tkfilebrowser.askopenfilename(initialdir="/", title="Select file",
                                     filetypes = [( "png" ,  "* .png" ),  ( "jpeg" ,  "* .jpg" ),  ( "all files" ,  "*" )])

    image1 = cv2.imread(path)
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    img1 = image1
    image1 = Image.fromarray(image1).resize((500,480))
    image1 = ImageTk.PhotoImage(image1)

    show = tkinter.Label(image=image1)
    show.image = image1
    show.place(x=150, y=0)

def histogram_generator():
    global image1
    a = 0
    color = ('b', 'g', 'r')
    while(a<=1):
        for i, c in enumerate(color):

            hist = cv2.calcHist([img1], [i], None, [256], [0,256])
            plt.plot(hist, color=c)
            a+=1

        plt.xlabel('Number of pixels')
        plt.ylabel('pixel intensity')
        plt.show()

def rgb_to_bw():

    global path, image2,  img2
    image2 = cv2.imread(path)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    img2 = image2
    image2 = Image.fromarray(image2).resize((500, 480))
    image2 = ImageTk.PhotoImage(image2)

    show2 = tkinter.Label(image=image2)
    show2.image = image2
    show2.place(x=150, y=0)

def hist_black_and_white():

    global image2, img2
    hist = cv2.calcHist([img2], [0], None, [256], [0,256])
    plt.plot(hist, color='gray')

    plt.show()





root = tkinter.Tk()
root.title('Histogram Generator')

frame = tkinter.Frame(root)
frame.config(width = 820, height=650)
frame.config(cursor='pirate')
frame.config(bg='blue')
frame.pack()


imagen1 = tkinter.PhotoImage(file='cargar.gif')
button1 = tkinter.Button(frame, image=imagen1, command=cargar_imagen)
button1.place(x=5, y=500)

imagen2 = tkinter.PhotoImage(file='boton_hist_1_.gif')
button2 = tkinter.Button(frame, image=imagen2, command=histogram_generator)
button2.place(x=170, y =500)

imagen3 = tkinter.PhotoImage(file="boton-b_a_w.gif")
button3 = tkinter.Button(frame, image=imagen3, command=rgb_to_bw)
button3.place(x=335, y =500)

imagen4 = tkinter.PhotoImage(file="histo_bn.gif")
button4 = tkinter.Button(frame, image=imagen4, command=hist_black_and_white)
button4.place(x=495, y=500)

imagen5 = tkinter.PhotoImage(file="readme.gif")
button5 = tkinter.Button(frame, image=imagen5)
button5.place(x=660, y=500)


text1=tkinter.Label(text="Load image")
text1.place(x=50, y=478)


text2= tkinter.Label(text="Generate Hist RGB")
text2.place(x=190, y=478)

text3= tkinter.Label(text="Converter RGB to B/W")
text3.place(x=340, y=478)

text4 = tkinter.Label(text="Generate hist B/W")
text4.place(x=520, y=478)

text5 = tkinter.Label(text="ReadMe")
text5.place(x=710, y=478)


root.mainloop()
