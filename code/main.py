from docx import Document
from word_finder import WordFinder


if __name__=="__main__":
    word_finder = WordFinder()
    document_name = "C:\\Users\\Ivan\\Documents\\Начало работы.docx"
    docx = Document(document_name)
    for para in docx.paragraphs:
        word_finder.find_in_line(para.text)
    print(word_finder.get_list_results())
