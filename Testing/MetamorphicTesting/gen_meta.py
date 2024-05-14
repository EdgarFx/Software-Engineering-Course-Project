import random

# basic expressions: single operator with constant or existing vars
def form_basic_expression(existing_vars):
    var_types = ["bv8", "bv16", "bv32", "bv64"]
    operators = ["CONSTANT", "NOT", "AND", "OR", "ADD", "SUB"]
    operator = random.choice(operators)
    if operator == "CONSTANT":
        var_type = random.choice(var_types)
        bits = int(var_type[2:])
        exp = random.choice(["0", "1"]) * bits
    if operator == "NOT":
        flag = random.choice([0,1])
        if flag == 1: # use constant
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp = f"! ( {val} )"
        else: # use var
            var_name = random.choice(existing_vars)
            exp = f"! ( {var_name} )"
    if operator == "AND":
        flag_left = random.choice([0,1])
        flag_right = random.choice([0,1])
        if flag_left == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_left = val
        else:
            var_name = random.choice(existing_vars)
            exp_left = var_name
        if flag_right == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_right = val
        else:
            var_name = random.choice(existing_vars)
            exp_right = var_name
        exp = f"( {exp_left} ) & ( {exp_right} )"
    if operator == "OR":
        flag_left = random.choice([0,1])
        flag_right = random.choice([0,1])
        if flag_left == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_left = val
        else:
            var_name = random.choice(existing_vars)
            exp_left = var_name
        if flag_right == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_right = val
        else:
            var_name = random.choice(existing_vars)
            exp_right = var_name
        exp = f"( {exp_left} ) | ( {exp_right} )"
    if operator == "ADD":
        flag_left = random.choice([0,1])
        flag_right = random.choice([0,1])
        if flag_left == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_left = val
        else:
            var_name = random.choice(existing_vars)
            exp_left = var_name
        if flag_right == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_right = val
        else:
            var_name = random.choice(existing_vars)
            exp_right = var_name
        exp = f"( {exp_left} ) + ( {exp_right} )"
    if operator == "SUB":
        flag_left = random.choice([0,1])
        flag_right = random.choice([0,1])
        if flag_left == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_left = val
        else:
            var_name = random.choice(existing_vars)
            exp_left = var_name
        if flag_right == 1:
            var_type = random.choice(var_types)
            bits = int(var_type[2:])
            val = random.choice(["0", "1"]) * bits
            exp_right = val
        else:
            var_name = random.choice(existing_vars)
            exp_right = var_name
        exp = f"( {exp_left} ) - ( {exp_right} )"
    return exp

def form_complex_expression(existing_vars):
    operators = ["NOT", "AND", "OR", "ADD", "SUB"]
    operator = random.choice(operators)
    if operator == "NOT":
        exp1 = form_basic_expression(existing_vars)
        result1 = f"! ( {exp1} )"
        result2 = f"! ( ! ( ! ( {exp1} ) ) )"        
    if operator == "AND":
        exp1 = form_basic_expression(existing_vars)
        exp2 = form_basic_expression(existing_vars)
        result1 = f"( {exp1} ) & ( {exp2} )"
        result2 = f"! ( ! ( ( {exp2} ) & ( {exp1} ) ) )"
    if operator == "OR":
        exp1 = form_basic_expression(existing_vars)
        exp2 = form_basic_expression(existing_vars)
        result1 = f"( {exp2} ) | ( {exp1} )"
        result2 = f"! ( ! ( ( {exp1} ) | ( {exp2} ) ) )"
    if operator == "ADD":
        exp1 = form_basic_expression(existing_vars)
        exp2 = form_basic_expression(existing_vars)
        result1 = f"( {exp1} ) + ( {exp2} )"
        result2 = f"! ( ! ( ( {exp2} ) + ( {exp1} ) ) )"
    if operator == "SUB":
        exp1 = form_basic_expression(existing_vars)
        exp2 = form_basic_expression(existing_vars)
        result1 = f"( {exp1} ) - ( {exp2} )"
        result2 = f"! ( ! ( ( {exp1} ) - ( {exp2} ) ) )"
    return result1, result2


def eight_bit_constant():
    constant = random.randint(2,15)
    constant = bin(constant)[2:].zfill(8)
    return constant


if __name__ == "__main__":
    f = open("./input1.pig", "w")
    g = open("./input2.pig", "w")
    var_types = ["bv8", "bv16", "bv32", "bv64"]
    var_nums = random.randint(1, 800)
    line_nums = 0
    existing_vars = []
    expressions = []

    # declare vars
    for i in range(0, var_nums):
        var_flag = random.choice([0,1])
        if var_flag == 1:
            var_name = "v" + str(i).zfill(3)
            var_type = random.choice(var_types)
            stmt = f"D {var_type} {var_name}"
            print(stmt, file=f)
            print(stmt, file=g)
            line_nums += 1
            existing_vars.append(var_name)
            assign_0_flag = random.choice([0,1])
            if assign_0_flag == 1 and line_nums < 950:
                stmt = f"A {var_name} ( 00000000 )"
                print(stmt, file=f)
                line_nums += 1

    # assign, output, and remove vars
    for var_name in existing_vars:
        assign_flag = random.choice([0,1])
        if assign_flag == 1 and line_nums < 950:
            var_type = random.choice(var_types)
            basic_exp_type = random.choice([0,1])
            if basic_exp_type == 1:
                exp = form_basic_expression(existing_vars)
                stmt = f"A {var_name} ( {exp} )"
                print(stmt, file=f)
                print(stmt, file=g)
            else:
                exp1, exp2 = form_complex_expression(existing_vars)
                stmt = f"A {var_name} ( {exp1} )"
                print(stmt, file=f)
                stmt = f"A {var_name} ( {exp2} )"
                print(stmt, file=g)
            line_nums += 1

            # forward jump to the next line
            forward_branch_flag = random.randint(1,5)
            if forward_branch_flag == 1 and (line_nums+2) < 950:
                stmt = f"B {line_nums+1} ( ( {var_name} ) + ( 00000001 ) )"
                print(stmt, file=f)
                line_nums += 1
                stmt = f"O {var_name}"
                print(stmt, file=f)
                line_nums += 1


        output_flag = random.choice([0,1])
        if output_flag == 1 and line_nums < 950:
            stmt = f"O {var_name}"
            print(stmt, file=f)
            print(stmt, file=g)
            line_nums += 1

        remove_flag = random.choice([0,1])
        if remove_flag == 1 and line_nums < 950:
            stmt = f"R {var_name}"
            print(stmt, file=f)
            print(stmt, file=g)
            line_nums += 1
            existing_vars.remove(var_name)
    
    f.close()
    g.close()
