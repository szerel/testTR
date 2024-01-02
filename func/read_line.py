

def read_line(FILE_ENG, FILE_RU, index):

    try:
        with open(FILE_ENG, 'r+') as file:
            line_eng = file.readlines()
            line_eng = line_eng[index].strip()

        with open(FILE_RU, 'r+') as file:
            line_ru = file.readlines()
            line_ru = line_ru[index].strip()
            return line_eng, line_ru


    except FileNotFoundError:
        print('FileNotFound.')
        return

    except Exception as e:
        print('Error: {}'.format(str(e)))
        return



