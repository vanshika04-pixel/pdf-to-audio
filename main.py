import pyttsx3
import  PyPDF2
file_path = input("Enter the path to the PDF file: ")
try:
    with open(file_path,mode="rb") as file:
        pdfreader=PyPDF2.PdfReader(file)
        pdf_pages = len(pdfreader.pages)
        engine=pyttsx3.init()
        for page in range(pdf_pages):
            page=pdfreader.pages[page]
            text=page.extract_text()
            clean_text=text.strip().replace("\n","")

    engine.save_to_file(clean_text,f"{file}.mp3")
    engine.runAndWait()
    engine.stop()
except:
    print("Sorry file does not exist!!!")

