from func.read_line import read_line
from func.сount_punctuation_marks import count_punctuation_marks
from szFilter.punctuation import punctuation_mark
from func.write_new_file import write_new_file
from func.count_lines import count_lines
from szFilter.unicode import check_unicode
from szFilter.count_words import count_words
import datetime


FILE_ENG = 'WikiMatrix.en-ru.en'
FILE_RU = 'WikiMatrix.en-ru.ru'
RESULT_PATH = 'RESULT/{}'


count_lin_eng, count_lin_ru = count_lines(FILE_ENG), count_lines(FILE_RU)
if count_lin_eng == count_lin_ru:
    print(datetime.datetime.now().time())

    indexSTR = 0
    flag = False

    while True:
        print(indexSTR)
        # if indexSTR == 100:
        #     print(datetime.datetime.now().time())
        #     break
        if count_lin_eng < indexSTR:
            print(datetime.datetime.now().time())
            break
        if flag == False:
            str_FILE_ENG, str_FILE_RU = read_line(FILE_ENG, FILE_RU, indexSTR)
            count_pm_eng, count_pm_ru = count_punctuation_marks(str_FILE_ENG), count_punctuation_marks(str_FILE_RU)
            if punctuation_mark(count_pm_eng, count_pm_ru) is False:
                indexSTR += 1
            else:
                if check_unicode(str_FILE_ENG, str_FILE_RU) is None:
                    if count_words(str_FILE_ENG, str_FILE_RU) == 'Maybe':
                        flag = True
                    else:
                        indexSTR += 1
                        flag = False
                else:
                    indexSTR += 1
                    flag = False
        else:
            if write_new_file(FILE_ENG, FILE_RU, str_FILE_ENG, str_FILE_RU, RESULT_PATH) is True:
                flag = False
                indexSTR += 1