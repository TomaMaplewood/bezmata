import os

from docx import Document

from word_finder import WordFinder
from options_parser import parse_options
from rule_manager import SingleRule, PairRule, RuleWriter

if __name__=="__main__":
    options, text_rules = parse_options("options.txt")

    #FIND_DEPTH is maximum interval in text between searching words in phrase
    #SAVE_PATH is full name of file where you want to save results
    word_finder = WordFinder(options, int(os.getenv("FIND_DEPTH", 3)), RuleWriter(text_rules, os.getenv("SAVE_PATH")))

    #MIN_NUM is minimal frequency for candidates
    minimal_number = int(os.getenv("MIN_NUM", 1))


    #Recuired to have environment variable DOC_PATH where you can define path to document
    #It is temporary measure
    #Full file names must be written in DOC_PATH variable and separated by comma ','

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


    if len(word_finder.get_summary()) != len(text_rules) or len(word_finder.get_result_by_rules()) != len(text_rules):
        raise Exception("Unexpected Runtime Error")
    
    single_rules = []
    
    for i in range(len(text_rules)):
        if word_finder.get_summary()[i] >= minimal_number:
            single_rules.append(SingleRule(text_rules[i], word_finder.get_result_by_rules()[i]))

    pair_rules = []

    for i in range(len(single_rules)):
        for j in range(i + 1,len(single_rules)):
                pair_rules.append(PairRule(single_rules[i], single_rules[j], minimal_number))

    for r in pair_rules:
        r.check_pair_rule()

