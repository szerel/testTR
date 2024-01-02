

def write_new_file(FILE_ENG, FILE_RU, str_FILE_ENG, str_FILE_RU, RESULT_PATH):

    with open(RESULT_PATH.format(FILE_ENG), 'a') as file:
        file.write(str_FILE_ENG + '\n')

    with open(RESULT_PATH.format(FILE_RU), 'a') as file:
        file.write(str_FILE_RU + '\n')

    return True