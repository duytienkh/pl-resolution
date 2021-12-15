import random as rd
import os

def clause_str(clause):
    return " OR ".join(clause)

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    test_size = 100
    clause_size = 8
    while test_size > 0:
        print("Generating testcase " + str(test_size))
        file = open("./input/input" + str(test_size) + ".txt", "w")
        _size = 0
        _clause_size = rd.randint(clause_size // 2, clause_size)
        while _size < _clause_size:
            a = 65
            clause = rd.randint(1, 2**4 - 1)
            lst = []
            while clause > 0:
                present = clause & 1
                clause = clause >> 1
                if present:
                    lst.append(chr(a))
                a += 1

            sign = rd.randint(0, 2 ** lst.__len__() - 1)

            i = 0
            while sign > 0:
                present = sign & 1
                sign = sign >> 1
                if present:
                    lst[i] = "-" + lst[i]
                
                i += 1
            
            # print(clause_str(lst))
            file.write(clause_str(lst) + "\n")
            if _size == 0:
                # print(_clause_size - 1)
                file.write(str(_clause_size - 1) + "\n")
            _size += 1

        test_size -= 1