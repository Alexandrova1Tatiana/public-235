
def yeah():
    print(
        " Добро пожаловать в игру загадки, здесь вам предстоить найти ответ на 3 сложные загадки. У вас будет 5 попыток, ответы пишите с маленькой буквы и вы выиграйте")
    answer_1:   str = "водопровод"
    answer_2:   str = "машины"
    answer_3:   str = "сапоги"
    question_1: str = "Речка спятила с ума —По домам пошла сама."
    question_2: str = "Маленькие домики по улице бегут, Мальчиков и девочек домики везут."
    question_3: str = "Пустые отдыхаем, А полные шагаем."
    question_number: int = 1
    correct_answers: int = 0
    errors:          int = 0

    while errors < 5 and correct_answers < 3:
         if question_number == 1:
             user_input_1: str = input(question_1 + '\n').strip().lower()

             if user_input_1 == answer_1:
                 print("Здорово!")
                 correct_answers += 1
                 question_number += 1
             else:
                 errors += 1
                 print("Попробуйте еще раз‚!", errors," количество ошибок")

         elif question_number == 2:
             user_input_2: str = input(question_2 + '\n').strip().lower()

             if user_input_2 == answer_2:
                 print("Так держать!")
                 correct_answers += 1
                 question_number += 1
             else:
                 errors += 1
                 print("Попробуйте еще раз‚!", errors ,"количество ошибок")
         elif question_number == 3:
             user_input_3: str = input(question_3 + '\n').strip().lower()
             if user_input_3 == answer_3:
                 print("Молодец!")
                 correct_answers += 1
                 question_number += 1
             else:
                 errors += 1
                 print("Попробуйте еще раз‚!" , errors ,"количество ошибок")
         if errors == 5:
             print("Вы проиграли!")
         elif correct_answers == 3:
             print("Вы выиграли!")
yeah()