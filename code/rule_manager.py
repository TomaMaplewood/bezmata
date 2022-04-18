from docx import Document


class SingleRule:
    def __init__(self, rule: str, appearance: list):
        self.rule = rule
        self.appearance = appearance
    def get_range(self)->int:
        return len(self.appearance)

class PairRule:
    def __init__(self, rule_1: SingleRule, rule_2: SingleRule, min_num: int = 3):
        if len(rule_1.appearance) != len(rule_2.appearance):
            raise Exception("Rules have not equal appearance arrays")

        self.rule_1 = rule_1
        self.rule_2 = rule_2
        self.min_num = min_num

    def __count_appearance(self) -> bool:
        count_app = 0
        for i in range(self.rule_1.get_range()):
            if self.rule_1.appearance[i]*self.rule_2.appearance[i] > 0:
                count_app += 1

        return count_app >= self.min_num

    def check_pair_rule(self) -> bool:
        if self.__count_appearance():
            print("**********\n")
            print(f"Если {self.rule_1.rule} то {self.rule_2.rule}\n")
            print(f"Если {self.rule_2.rule} то {self.rule_1.rule}\n")
            print("**********\n")
            return True
        else:
            return False

class RuleWriter:
    def __init__(self, rule_list: list, file_name: str):
        self.rule_list = rule_list
        self.file_name = file_name
        self.docx = Document()

    def rule_appear(self, num: int):
        self.docx.add_paragraph(self.rule_list[num])

    def __del__(self):
        self.docx.save(self.file_name)
