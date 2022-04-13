import re

class WordFinder:
    phrases = [["нажати", "на", "форм"],
               ["[Сс]озда", "отчёт"],
               ["[Уу]каз", "ответственн"],
               ["[Тт]екущ", "дат"],
               ["[Пп]ечата"],
               ["[Пп]оказыва", "сообщен"]]
    patterns = []
    re_pattern = "[^[ ,\:,\.,\,,\!,\?,(,),\[,\],\;]"
    def __init__(self):
        for phrase in self.phrases:
            temp_dict = []
            for word in phrase:
                temp_dict.append(re.compile(f"(?i){word}{self.re_pattern}"))
            self.patterns.append(temp_dict)
        self.counter = [0,0,0,0,0,0]


    def __continue_find(self, input_line:list, pattern_num:int, start_word_num:int = 0):
        print(start_word_num,'\n')
        if len(self.patterns[pattern_num]) == 1:
            return True
        current_pattern = 1
        for i in range(start_word_num, len(input_line)):
            print(i,pattern_num,current_pattern,'\n',sep=' ')
            if self.patterns[pattern_num][current_pattern].match(input_line[i]) is None:
                if current_pattern == len(self.patterns[pattern_num]) - 1:
                    return True
                else:
                    current_pattern = current_pattern + 1
        return False

    def find_in_line(self,input_line:str):
        """
        finds word in line of text
        :param input_line: line from docx, where you need to find some words
        :return:
        """
        words = input_line.split(sep=' ')
        for j in range(len(words)):
            for i in range(len(self.patterns)):
                if self.patterns[i][0].match(words[j]) is not None:
                    if self.__continue_find(words, i, j):
                        self.counter[i] = self.counter[i] + 1

        pass

    def get_list_results(self):
        return self.counter

    def get_dict_results(self):
        return {"a" : self.counter[0],
                "b" : self.counter[1],
                "c" : self.counter[2],
                "d" : self.counter[3],
                "e" : self.counter[4],
                "f" : self.counter[1]}