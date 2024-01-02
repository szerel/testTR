import unicodedata


def is_english(character):
    return 'LATIN' in unicodedata.name(character, '')

def is_russian(character):
    return 'CYRILLIC' in unicodedata.name(character, '')

def check_unicode(str_FILE_ENG, str_FILE_RU):
    str_FILE_ENG = ''.join(ch for ch in str_FILE_ENG if ch.isalpha())
    str_FILE_RU = ''.join(ch for ch in str_FILE_RU if ch.isalpha())

    for eng in list(str_FILE_ENG):
        if eng.isdigit():
            pass
        else:
            if is_english(eng) is False:
                return False


        for ru in list(str_FILE_RU):
            if ru.isdigit():
                pass
            else:
                if is_russian(ru) is False:
                    return False

