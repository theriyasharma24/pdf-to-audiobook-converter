#importing the modules
import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#function to convert pdf to audiobook
def pdftoaudio():

    window1=Tk()
    window1.configure(bg='blue4')
    window1.geometry("500x500")
    window1.title("PDF to Audiobook Converter!")
    window1.configure(bg="midnightblue")
    Label(window1,text="PDF to Audiobook Converter",font=("Elephant",16),bg="pink").place(x=90,y=0)

    #function to get the pdf file
    def getfile():
        global path
        path= filedialog.askopenfilename()
    
    #function to convert the pdf file to audiobook
    def convert():
        book=open(path,'rb')
        pdfReader=PyPDF2.PdfFileReader(book)
        pages=pdfReader.numPages
        text=''
        Label(window1,text="Converting.....",font=("Elephant",16),bg="pink").place(x=170,y=300)
        for i in range(0,pages):
                speaker=pyttsx3.init()

                rate = speaker.getProperty('rate')   
                speaker.setProperty('rate', 130)

                voices = speaker.getProperty('voices')
                speaker.setProperty('voice', voices[1].id)
                page=pdfReader.getPage(i)
                text+=page.extractText()
          
        #saving the audiobook
        file=filedialog.asksaveasfilename(defaultextension='.mp3')
        speaker.save_to_file(text, file)

        Label(window1,text="Your audiobook is saved!",font=("Elephant",16),bg="pink").place(x=120,y=300)
        speaker.runAndWait()


    Button(window1,text="  Select PDF  ",bd=5,width=20,font=("Aharani",10,"bold"),height=1,bg="gold",command=getfile).place(x=160,y=100)
    Button(window1,text="  Convert PDF  ",bd=5,width=20,font=("Aharani",10,"bold"),height=1,bg="gold",command=convert).place(x=160,y=150)
    Button(window1,text="  Exit  ",bd=5,width=20,font=("Aharani",10,"bold"),height=1,bg="gold",command=lambda:(window1.destroy())).place(x=160,y=200)

    window1.mainloop()


pdftoaudio()
