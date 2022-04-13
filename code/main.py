import os

from docx import Document
from word_finder import WordFinder
from options_parser import parse_options

if __name__=="__main__":

    word_finder = WordFinder(parse_options("options.txt"))
    #print(parse_options("options.txt"))
    #Recuired to have environment variable DOC_PATH where you can define path to document
    #It is temporary measure

    document_name = str(os.getenv("DOC_PATH"))
    try:
        docx = Document(document_name)

    except Exception as e:
        print("Can not open file because of", str(e))
        raise e

    for para in docx.paragraphs:
        word_finder.find_in_line(para.text)
    print(word_finder.get_list_results())
