import string


def count_words(str_FILE_ENG, str_FILE_RU):
    str_FILE_ENG = str_FILE_ENG.strip(string.punctuation + " ")
    str_FILE_RU = str_FILE_RU.strip(string.punctuation + " ")

    words_eng = str_FILE_ENG.split()
    words_ru = str_FILE_RU.split()

    result = len(words_ru) - len(words_eng)
    if result >= -10 and result <= 10:
        return 'Maybe'
