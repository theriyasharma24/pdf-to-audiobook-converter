import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

def pdftoaudio():
    global s
    s="Normal"
    global g
    g="Male"
    global speaker

    window1=Tk()
    window1.geometry("1800x1800")
    window1.title("PDF to Audiobook Converter!")
    window1.configure(bg="black")
    

    def getfile():
        global path      
        path= filedialog.askopenfilename()
        
        
        
    def convert():
        if path=="":
            messagebox.showerror('Error! No PDF Found', 'Please select a PDF first!')
        else:
            book=open(path,'rb')
            pdfReader=PyPDF2.PdfFileReader(book)
            pages=pdfReader.numPages
            global text
            text=''
            Label(window1,text="Converting.....                        ",font=("Times",23,"bold"),bg="gold").place(x=510,y=410)
            global speaker

            speaker=pyttsx3.init()
            rate = speaker.getProperty('rate')
            global s,g
            speed=s.replace(" ", "")
            if speed=="Slower":
                rate=60
            elif speed=="Slow":
                rate=100
            elif speed=="Normal":
                rate=140
            elif speed=="Fast":
                rate=180
            else:
                rate=220
            print(speed,"hi")
            print(rate)
            for i in range(0,pages):
                    
                    
                      
                    speaker.setProperty('rate', rate)

                    voices = speaker.getProperty('voices')

                    gender=g.replace(" ","")
                    if gender=="Male":
                        speaker.setProperty('voice', voices[0].id)
                    else:
                        speaker.setProperty('voice', voices[1].id)
                        
                    page=pdfReader.getPage(i)
                    
                    text+=page.extractText()
                    
            file=filedialog.asksaveasfilename(defaultextension='.mp3')
            speaker.save_to_file(text, file)

            Label(window1,text="Your audiobook is saved!",font=("Times",23,"bold"),bg="gold").place(x=510,y=410)
            
            


            speaker.runAndWait()

    Label(window1,text="PDF To Audiobook Converter",font=("Times",38,"bold"),fg="white",bg="black").place(x=340,y=0)
    Label(window1,text="Get your customized audiobook in just 5 easy steps!",font=("Times",18),fg="white",bg="black").place(x=425,y=70)
    border_color = Frame(window1, background="white")

    
    canvas = Canvas(border_color,height=500,width=900,bg="gold")
    canvas.pack(padx=1, pady=1)
    border_color.pack(padx=40, pady=160)
    Label(window1,text=" 1. Select the PDF you want to convert to audiobook",font=("Times",18,"bold"),fg="black",bg="gold").place(x=250,y=170)


    Label(window1,text=" 2. Choose the gender of voice for your audiobook",font=("Times",18,"bold"),fg="black",bg="gold").place(x=250,y=230)
    Label(window1,text=" 3. Choose the speed of audio for your audiobook",font=("Times",18,"bold"),fg="black",bg="gold").place(x=250,y=290)
    Label(window1,text=" 4. Convert the PDF into your customized audiobook",font=("Times",18,"bold"),fg="black",bg="gold").place(x=250,y=350)


    Button(window1,text="  Select PDF  ",bd=5,width=20,font=("Aharani",12,"bold"),height=1,fg="white",bg="midnightblue",command=getfile).place(x=900,y=170)
    def gender(h):
        h=clicked.get()
        global g
        g=h
    
    options = ["              Male                ","              Female              "]
    # datatype of menu text 
    clicked = StringVar()
    clicked.set("Male")
    # Create Dropdown menu
    drop = OptionMenu(window1 ,clicked , *options, command=gender)
    drop.config(width=19,font=("Aharani",12,"bold"),height=1,fg="white",bg="midnightblue")
    drop.place(x=900,y=230)

    def speed(h):
        h=clicked1.get()
        global s
        s=h
        



    options1 = ["            Slower                 ","            Slow               ","            Normal        ","             Fast        ","             Faster             "]
    # datatype of menu text
    clicked1 = StringVar()
    # initial menu text
    clicked1.set( "Normal" )
    # Create Dropdown menu
    drop1 = OptionMenu(window1 , clicked1 , *options1,command=speed)
    drop1.config(width=19,font=("Aharani",12,"bold"),height=1,fg="white",bg="midnightblue")
    drop1.place(x=900,y=290)

    def convertagain():
        Label(window1,text="                                             ",font=("Times",23,"bold"),bg="gold").place(x=510,y=410)
        getfile()
    
        
        
    

    Button(window1,text="  Convert PDF  ",bd=5,width=20,font=("Aharani",12,"bold"),height=1,fg="white",bg="midnightblue",command=convert).place(x=900,y=350)
 
    Button(window1,text="  Convert Another PDF  ",bd=5,width=20,font=("Aharani",14,"bold"),height=1,fg="white",bg="dark green",command=convertagain).place(x=360,y=490)


    Button(window1,text="  Exit  ",bd=5,width=20,font=("Aharani",14,"bold"),height=1,fg="white",bg="dark red",command=lambda:(window1.destroy())).place(x=730,y=490)

    window1.mainloop()

text=''
path=''
pdftoaudio()

