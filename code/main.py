import os

from docx import Document
from word_finder import WordFinder


if __name__=="__main__":
    word_finder = WordFinder()

    #Recuired to have environment variable DOC_PATH where you can define path to document
    #It is temporary measure

    document_name = str(os.getenv("DOC_PATH"))
    docx = Document(document_name)
    for para in docx.paragraphs:
        word_finder.find_in_line(para.text)
    print(word_finder.get_list_results())
