import os

input_dir = "./input/"
output_dir = "./output/"

def get_input_files():
    input_files = os.listdir(input_dir)
    return input_files

def get_data(input_file: str):
    file = open(input_dir + input_file, "r")
    alpha = file.readline().strip("\n").replace(' ', '').split("OR")
    n = file.readline()
    kb = [clause.strip("\n").replace(' ', '').split("OR") for clause in file.readlines()]
    return alpha, kb

def NOT(literal: str) -> str:
    if literal[0] != "-":
        return "-" + literal
    return literal[1:]

def get_clause_str(clause: list) -> str:
    if clause == []:
        return "{}"
    return " OR ".join(clause)

def PL_Resolve(u: list, v: list):
    for literal in u:
        if NOT(literal) in v:
            ul = False
            for s_literal in u:
                if s_literal != literal and NOT(s_literal) in v:
                    ul = True
            if ul:
                return None
            
            res = []
            for s_literal in u:
                if s_literal != literal:
                    res.append(s_literal)

            for s_literal in v:
                if NOT(s_literal) != literal and s_literal not in u:
                    res.append(s_literal)

            def sort_condition(e):
                if e[0] == "-":
                    return NOT(e)
                return e
            res.sort(key=sort_condition)
            return res
    return None

def PL_Resolution(KB: list, alpha: list):
    for literal in alpha:
        KB.append([NOT(literal)])

    output = []
    while True:
        new = []
        for i in range(0, KB.__len__()):
            for j in range(i + 1, KB.__len__()):
                res = PL_Resolve(KB[i], KB[j])
                if res != None:
                    new.append(res)

        has_new_item = False
        print_items = []
        for clause in new:
            if clause not in KB:
                KB.append(clause)
                print_items.append(clause)
                has_new_item = True
        
        empty = False
        output.append(str(print_items.__len__()))
        for item in print_items:
            if item == []:
                empty = True
            output.append(get_clause_str(item))
        if empty:
            output.append("YES")
            return True, output
        if not has_new_item:
            break
    output.append("NO")
    return False, output

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    input_files = get_input_files()
    for input_file in input_files:
        alpha, kb = get_data(input_file)
        print("Solving " + input_file)
        try:
            output_file = input_file.replace("input", "output")
            file = open(output_dir + output_file, "w")
            ans, output = PL_Resolution(kb, alpha)        
            file.writelines(line + "\n" for line in output)
        except Exception as e:
            print(e)