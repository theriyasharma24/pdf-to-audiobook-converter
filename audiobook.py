import pyttsx3
import PyPDF2

#In place of filelocation give your PDF's location in single quotes ''
book=open('oop.PDF','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages

speaker=pyttsx3.init()

#rate of speed can be change as per convenience 
#increase the value for slower speed
rate = speaker.getProperty('rate')   
speaker.setProperty('rate', 130)

#voice can be changed as per convenience
#For male voice put
#speaker.setProperty('voice', voices[0].id)

voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

#Write the page number of the PDF you want audiobook for
#Here the page no. is 2

page=pdfReader.getPage(2)

text=page.extractText()


#Your audiobook will be saved with name audio.mp3
speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()
