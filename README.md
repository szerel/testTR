# ВАЖНО! 
Первым условием из задания было установить библиотеку https://github.com/Helsinki-NLP/OpusFilter, к сожалению на свою машину я не смог ее установить, пробовал на версии python от 3.8 до 3.12, посерфил просторы интернета и аналогичные ошибки, понял что возникают при использовании устройств на М процессорах от apple, (у меня мак на М2, ради теста на PVS с убунту все встало легко)

Если это было важным условием выполнения задания - то к сожалению спешу еще раз предупредить Вас, что в моем случае я не использую библиотеку OpusFilter.


Но сдаваться я не вижу смысла, поэтому важным для меня был пункт "Ваша задача - удалить строки, где неправильный перевод с английского на русский, те, где есть ошибки (грамматические, лексические итд). После чего прислать датасет только с хорошим переводом."

И так выше весь код, написал его еще в старом году, в ночь с 30 на 31го, запустил его на VPS и вот он 2 суток маслал цикл))) (Почему так долго? 1 процессор 3.6 и 2 ram, с запущенными 9 контейнерами на фоне, ну и то что я двигался по задаче step by step)

Перед тем как разрабатывать, разбил задачу на подзадачи (грубую и тонкую очистку) в файле IMG_1581.png
Комментарии не оставлял, в целом принцип простой, бегаю циклом, забираю по строке и с ней работаю. 

Мои фильтры:
1) Проверяю на знаки пунктуации (выполняется - тяну строки на 2ую проверку, не проходит проверку - беру другую строку) 
2) (если 1 условие выполняется) Количество слов (разница установлена на '10' слов, конечно изменив это значение - получим другой результат)
3) (если 2 условие выполняется) Принадлежность букв к их алфавиту. (выполняется условие - записываю строки в свой документ, нет - беру новую строку)

На входе 300 000 строк (1 файл), чистых получилось 59 155 (1 файл), Сейчас пишу этот текст перед пушем на гит, и понимаю что ничего не сделал для проверки '-' в словах, а именно, в своей инструкции рассматривал этот вопрос, что 2 англ через дефис могут транслит в 2 рус. без дефиса. Так же результат бы изменился из за разницы количества слов в предложении англ и рус, мое значение стоит не больше 10 штук, понизив его - уменьшу количество верных результатов.

Понимаю что это можно было запустить в несколько потоков и процесс ускорить в разы, разбивая весь файл на чанки, но сделал так и ушел готовиться к Празднику)

Спасибо за внимание! Спасибо за возможность поучаствовать в гонке. Понимаю что это не то что вы могли ожидать, но я руки не хотел опустить после первой неудачи на старте установки библы)

Результат фильтра в папке RESULT

С Новым Годом Вас! Спасибо за внимание!