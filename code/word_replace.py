def word_replace(sentence, find_word, replace_word):
    result = ''
    i = 0
    while i<len(sentence):
        is_exist = True # 찾는 단어가 문자열 i번째에 있는지 체크하는 변수
        for j in range(len(find_word)):
            if sentence[i + j] !=  find_word[j]:
                is_exist = False
                break
        if is_exist:
            result += replace_word
            i += len(find_word)
        else:
            result += sentence[i]
            i += 1
    return result