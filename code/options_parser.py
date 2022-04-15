def parse_options(options_file_path:str) -> tuple:
    """
    Returns list of regular expressions, that made from expressions in options file and list of rules
    :param options_file_path:
    :return: list of regular expressions for word finder, list of rules for human use
    """
    re_pattern = "[^[ ,\:,\.,\,,\!,\?,(,),\[,\],\;]"
    options_list = []
    rules_list = []
    opt_file = open(options_file_path, 'r', encoding='utf-8')
    lines_from_file = opt_file.readlines()
    for line in lines_from_file:
        if line[0] == '#':
            continue
        line = line.strip('\n')
        current_opt = []
        rule = ""
        words = line.split(' ')
        for raw_word in words:
            word_type, word = raw_word.split(':')
            rule += f"{word} "
            if word_type == 'n':
                current_opt.append(f"(?i){word[:len(word) - 1].replace('е','ё').replace('ё','[е,ё]')}{re_pattern}")
            elif word_type == 'v':
                current_opt.append(f"(?i){word[:len(word) - 3].replace('е','ё').replace('ё','[е,ё]')}{re_pattern}")
            elif word_type == 'ad':
                current_opt.append(f"(?i){word[:len(word) - 2].replace('е','ё').replace('ё','[е,ё]')}{re_pattern}")
            elif word_type == 'pr':
                current_opt.append(f"(?i)\\b{word.replace('е','ё').replace('ё','[е,ё]')}\\b")
            else:
                print("Warning: some options are unable to read. Probably you wrong define type of word")
                continue
        options_list.append(current_opt)
        rules_list.append(rule)
    return options_list, rules_list
