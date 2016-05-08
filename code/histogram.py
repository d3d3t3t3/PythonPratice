def histogram(word_list):
    dic = {}
    for word in word_list:
        if dic.get(word, 0) == 0: # 키 'word'가 없을 시 0을 반환
            dic[word] = 1
        else :
            dic[word] += 1
    # 출력
    for key, value in dic.items():
        sign = ""
        for i in range(value):
            sign += '='
        print("{key}\t{sign}".format(key=key,sign=sign))
    print(dic)
histogram(["패스트", "캠퍼스", "패스트캠퍼스", "패스트", "트랙", "아시아"])