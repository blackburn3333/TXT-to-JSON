import json
import codecs
import unicodedata

wordfile = 'testdata.txt'

def readMethod():
    file = open(wordfile, encoding="utf8")
    textline = file.readlines()

    words = []
    options = []
    dictionary = []
    for x in range(len(textline)):
        if textline[x].strip():
            dataline = textline[x]
            splited = dataline.split("=")
            words.append(splited[0])
            options.append(splited[1].strip("\n ' '"))

            print("Adding " + splited[0] + " to JSON with options " + splited[1].strip("\n ' '"))
            dictionary = [{'word': word, 'options': option} for word, option in zip(words, options)]

    with codecs.open('entosin.json', 'w', encoding='utf8') as output:
        json.dump(dictionary, output, ensure_ascii=False)


def mainMethod():
    print("Convert text to json..")
    print("Starting.....")
    readMethod()
    print("Completed....")


if __name__ == '__main__':
    mainMethod()
