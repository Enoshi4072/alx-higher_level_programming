#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    answers = []
    for i in range(list_length):
        try:
            ele1 = my_list_1[i]
            ele2 = my_list_2[i]
            result = ele1 / ele2
            answers.append(result)
        except (TypeError):
            print("wrong type")
            answers.append(0)
        except (IndexError):
            print("Out of range")
            answers.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            answers.append(0)
        finally:
            pass
    return answers
