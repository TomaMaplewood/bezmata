def parse_options(options_file_path:str) -> list:
    """
    Returns list of regular expressions, that made from expressions in options file
    :param options_file_path:
    :return: list of regular expressions for word finder
    """
    re_pattern = "[^[ ,\:,\.,\,,\!,\?,(,),\[,\],\;]"
    options_list = []
    opt_file = open(options_file_path, 'r', encoding='utf-8')
    options_line = opt_file.readlines()
    for line in options_line:
        if line[0] == '#':
            continue
        line = line.strip('\n')
        current_opt = []
        words = line.split(' ')
        for word in words:
            word_type, raw_word = word.split(':')
            if word_type == 'n':
                current_opt.append(f"(?i){raw_word[:len(raw_word) - 1].replace('е','ё').replace('ё','[е,ё]')}{re_pattern}")
            elif word_type == 'v':
                current_opt.append(f"(?i){raw_word[:len(raw_word) - 3].replace('е','ё').replace('ё','[е,ё]')}{re_pattern}")
            elif word_type == 'ad':
                current_opt.append(f"(?i){raw_word[:len(raw_word) - 2].replace('е','ё').replace('ё','[е,ё]')}{re_pattern}")
            elif word_type == 'pr':
                current_opt.append(f"(?i){raw_word.replace('е','ё').replace('ё','[е,ё]')}")
            else:
                print("Warning: some options are unable to read. Probably you wrong define type of word")
                continue
        options_list.append(current_opt)
    return options_list
