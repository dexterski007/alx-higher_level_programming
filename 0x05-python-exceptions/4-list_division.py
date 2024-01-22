#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    length = []
    
    for i in range(list_length):
        try:
            length.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            length.append(0)
            print("division by 0")
            continue
        except (TypeError):
            length.append(0)
            print("wrong type")
            continue
        except IndexError:
            length.append(0)
            print("out of range")
            continue
        finally:
            pass
    return length
