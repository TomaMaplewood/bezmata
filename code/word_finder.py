import re

class WordFinder:
    def __init__(self, patterns:list):
        self.patterns = []
        for pattern_line in patterns:
            new_pattern = []
            for pattern in pattern_line:
                new_pattern.append(re.compile(pattern))
            self.patterns.append(new_pattern)
        self.counter = [0,0,0,0,0,0]

    def __continue_find(self, input_line:list, pattern_num:int, start_word_num:int = 0):
        if len(self.patterns[pattern_num]) == 1:
            return True
        current_pattern = 1
        for i in range(start_word_num, len(input_line)):
            if self.patterns[pattern_num][current_pattern].match(input_line[i]) is not None:
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