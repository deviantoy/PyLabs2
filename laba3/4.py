def get_string():
    text = "ss jfjfj er fhfhf ff h456 4444"  # input("Enter your text : ")
    print("Inputed text : ", text)
    return text


def get_word_len():
    n = "3"
    return n


def del_words_shorter_than(text, n):
    words = text.split(' ')
    # print("words: ",words)
    for word in words:
        if len(word) <= int(n):
            # print(word)
            words.remove(word)
    text2 = " ".join(words)
    print("Longer than", n, ":", text2)
    return text2


def replace_digits(text):
    secret = ''.join(['*' if c.isdigit() else c for c in text])
    print("Replace all digits with * : ", secret)
    return secret


def seperate_letters(text):
    words = text.split(' ')
    newLetters = []
    for item in words:
        newLetters.append(list(item))
    # print(newLetters)
    # print(fin)
    flat = [x for sublist in newLetters for x in sublist]
    fin = ' '.join(flat)
    print("Seperated letters : ", fin)
    return (fin)


def sort_words_len(text):
    xs = text.split(' ')
    xs.sort(key=len)
    fin = ' '.join(xs)
    print("Sorted len : ", fin)
    return fin


def sort_words_alph(text):
    tmp = text.split(' ')
    # print(tmp)
    sort = sorted(tmp)
    # print(sort)
    fin = ' '.join(sort)
    print("Sorted alph : ", fin)
    return fin


txt = get_string()
num = get_word_len()
txt2 = del_words_shorter_than(txt, num)
txt3 = replace_digits(txt)
txt4 = seperate_letters(txt)
txt5 = sort_words_alph(txt)
txt6 = sort_words_len(txt)