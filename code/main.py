import os

from docx import Document
from word_finder import WordFinder
from options_parser import parse_options

if __name__=="__main__":
    options, rules = parse_options("options.txt")
    word_finder = WordFinder(options, int(os.getenv("FIND_DEPTH", 3)))

    #Recuired to have environment variable DOC_PATH where you can define path to document
    #It is temporary measure

    document_names = str(os.getenv("DOC_PATH")).split(',')
    for document_name in document_names:
        try:
            docx = Document(document_name)

        except Exception as e:
            print("Can not open file because of ", str(e))
            raise e
        word_finder.ignition()
        for para in docx.paragraphs:
            word_finder.find_in_line(para.text)
        word_finder.next_file()
    print(word_finder.get_list_results(),'\n')
    print(word_finder.summarise())
