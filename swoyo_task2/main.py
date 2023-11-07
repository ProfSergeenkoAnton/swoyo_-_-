def match_RU(text:str, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    if text.isalpha():
        return not alphabet.isdisjoint(text.lower())
    else:
        return None
def match_EU(text: str, alphabet=set('abcdefghijklmnopqrstuvwxyz')):
    if text.isalpha():
        return not alphabet.isdisjoint(text.lower())
    else:
        return None
def text_stat(filename: str):
    dict = {}
    buff = {}
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            if "Word ammount" not in dict:
                dict["Word ammount"] = len(line.split())
            else:
                dict["Word ammount"] += len(line.split())
            for w in line.split():
                lst = []
                st = set()
                if match_EU(w) and match_RU(w) is True:
                    if "Paragraph amount" not in dict:
                        dict["bilingual_word_amount"] = 1
                    else:
                        dict["bilingual_word_amount"] += 1
                for i in range(len(w)):
                    if w[i] not in dict:
                        if w[i].isalpha():
                            dict[w[i]] = [1]
                            lst.append(w[i])
                    else:
                        if w[i].isalpha():
                            dict[w[i]][0] += 1
                            lst.append(w[i])
                lst = set(lst)
                for i in lst:
                    if i in w:
                        if i not in buff:
                            buff[i] = 1
                        else:
                            buff[i] += 1
                if line[0:4] == "    ":
                    if "Paragraph amount" not in dict:
                        dict["Paragraph amount"] = 1
                    else:
                        dict["Paragraph amount"] += 1
    for i in dict:
        if len(i) == 1:
            dict[i].append(buff[i])
            dict[i] = tuple(dict[i])
    file.close()
    return dict

if __name__ == '__main__':
    print(text_stat("data.txt"))
