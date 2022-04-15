import re

class WordFinder:
    def __init__(self, patterns:list, depth:int):
        self.patterns = []
        self.depth = depth
        for pattern_line in patterns:
            new_pattern = []
            for pattern in pattern_line:
                new_pattern.append(re.compile(pattern))
            self.patterns.append(new_pattern)
        self.counter = []
        self.file_num = 0

    def __continue_find(self, input_line:list, pattern_num:int, start_word_num:int = 0):
        if len(self.patterns[pattern_num]) == 1:
            return True
        current_pattern = 1
        current_depth = 0
        for i in range(start_word_num, len(input_line)):
            if self.patterns[pattern_num][current_pattern].match(input_line[i]) is not None:
                current_depth = 0
                if current_pattern == len(self.patterns[pattern_num]) - 1:
                    return True
                else:
                    current_pattern += 1

            elif current_depth == self.depth:
                    break

            current_depth += 1
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
                        self.counter[self.file_num][i] += 1

        pass

    def get_result_by_files(self):
        return self.counter

    def reset_results(self):
        self.counter = []

    def ignition(self):
        self.counter.append([0] * len(self.patterns))

    def next_file(self):
        self.file_num += 1

    def get_summary(self) -> list:
        _sum = [0] * len(self.patterns)
        for i in range(len(self.patterns)):
            for j in range(len(self.counter)):
                _sum[i] += self.counter[j][i]

        return _sum

    def get_result_by_rules(self)->list:
        _sum = []
        for i in range(len(self.patterns)):
            current_sum = [0] * len(self.counter)
            for j in range(len(self.counter)):
                current_sum[j] = self.counter[j][i]

            _sum.append(current_sum)
        return _sum