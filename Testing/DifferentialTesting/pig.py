def twos_complement(binary_string):
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary_string)
    complement = bin(int(inverted, 2) + 1)[2:]
    return complement.zfill(len(binary_string))


def stored_value(bits,expression):
    exp_len = len(expression)
    if exp_len < bits:
        decimal_num = int(expression,2)
        exp_value = bin(decimal_num)[2:].zfill(bits)
        return exp_value
    elif exp_len > bits:
        expression = expression[-bits:]
        exp_value = expression
        return exp_value
    else:
        exp_value = expression
        return exp_value


def compute_basic_not(vars,expression): # NOT-VAR or NOT-CON
    if expression[0] == "v": # NOT-VAR
        exp_value = vars[expression][1]
        not_exp_value = ''.join('1' if bit == '0' else '0' for bit in exp_value)
        return not_exp_value
    else: # NOT-CON
        not_exp_value = ''.join('1' if bit == '0' else '0' for bit in expression)
        return not_exp_value


def compute_basic_and(vars,left_exp,right_exp):
    if left_exp[0] == "v":
        left_type = vars[left_exp][0]
        left_bits = int(left_type[2:])
        left_exp_value = vars[left_exp][1]
    else:
        left_bits = len(left_exp)
        left_exp_value = left_exp
    if right_exp[0] == "v":
        right_type = vars[right_exp][0]
        right_bits = int(right_type[2:])
        right_exp_value = vars[right_exp][1]
    else:
        right_bits = len(right_exp)
        right_exp_value = right_exp
    if left_bits == right_bits:
        result = bin(int(left_exp_value, 2) & int(right_exp_value, 2))[2:].zfill(left_bits)
        return result
    elif left_bits > right_bits:
        right_exp_value = right_exp_value.zfill(left_bits)
        result = bin(int(left_exp_value, 2) & int(right_exp_value, 2))[2:].zfill(left_bits)
        return result
    else:
        left_exp_value = left_exp_value.zfill(right_bits)
        result = bin(int(left_exp_value, 2) & int(right_exp_value, 2))[2:].zfill(right_bits)
        return result


def compute_basic_or(vars,left_exp,right_exp):
    if left_exp[0] == "v":
        left_type = vars[left_exp][0]
        left_bits = int(left_type[2:])
        left_exp_value = vars[left_exp][1]
    else:
        left_bits = len(left_exp)
        left_exp_value = left_exp
    if right_exp[0] == "v":
        right_type = vars[right_exp][0]
        right_bits = int(right_type[2:])
        right_exp_value = vars[right_exp][1]
    else:
        right_bits = len(right_exp)
        right_exp_value = right_exp
    if left_bits == right_bits:
        result = bin(int(left_exp_value, 2) | int(right_exp_value, 2))[2:].zfill(left_bits)
        return result
    elif left_bits > right_bits:
        right_exp_value = right_exp_value.zfill(left_bits)
        result = bin(int(left_exp_value, 2) | int(right_exp_value, 2))[2:].zfill(left_bits)
        return result
    else:
        left_exp_value = left_exp_value.zfill(right_bits)
        result = bin(int(left_exp_value, 2) | int(right_exp_value, 2))[2:].zfill(right_bits)
        return result

def compute_basic_add(vars,left_exp,right_exp):
    if left_exp[0] == "v":
        left_type = vars[left_exp][0]
        left_bits = int(left_type[2:])
        left_exp_value = vars[left_exp][1]
    else:
        left_bits = len(left_exp)
        left_exp_value = left_exp
    if right_exp[0] == "v":
        right_type = vars[right_exp][0]
        right_bits = int(right_type[2:])
        right_exp_value = vars[right_exp][1]
    else:
        right_bits = len(right_exp)
        right_exp_value = right_exp
    if left_bits == right_bits:
        result = bin(int(left_exp_value, 2) + int(right_exp_value, 2))[2:].zfill(left_bits)[-left_bits:]
        return result
    elif left_bits > right_bits:
        right_exp_value = right_exp_value.zfill(left_bits)
        result = bin(int(left_exp_value, 2) + int(right_exp_value, 2))[2:].zfill(left_bits)[-left_bits:]
        return result
    else:
        left_exp_value = left_exp_value.zfill(right_bits)
        result = bin(int(left_exp_value, 2) + int(right_exp_value, 2))[2:].zfill(right_bits)[-right_bits:]
        return result
        

def compute_basic_sub(vars,left_exp,right_exp):
    if left_exp[0] == "v":
        left_type = vars[left_exp][0]
        left_bits = int(left_type[2:])
        left_exp_value = vars[left_exp][1]
    else:
        left_bits = len(left_exp)
        left_exp_value = left_exp
    if right_exp[0] == "v":
        right_type = vars[right_exp][0]
        right_bits = int(right_type[2:])
        right_exp_value = vars[right_exp][1]
    else:
        right_bits = len(right_exp)
        right_exp_value = right_exp
    if left_bits == right_bits:
        right_exp_value = twos_complement(right_exp_value)
        result = bin(int(left_exp_value, 2) + int(right_exp_value, 2))[2:].zfill(left_bits)[-left_bits:]
        return result
    elif left_bits > right_bits:
        right_exp_value = right_exp_value.zfill(left_bits)
        right_exp_value = twos_complement(right_exp_value)
        result = bin(int(left_exp_value, 2) + int(right_exp_value, 2))[2:].zfill(left_bits)[-left_bits:]
        return result
    else:
        left_exp_value = left_exp_value.zfill(right_bits)
        right_exp_value = twos_complement(right_exp_value)
        result = bin(int(left_exp_value, 2) + int(right_exp_value, 2))[2:].zfill(right_bits)[-right_bits:]
        return result


def constant_or_var(expression):
    if expression[0] == "v":
        exp_value = vars[expression][1]
        return exp_value
    else:
        return expression


def compute_exp_value(vars, var_type, expression):
    bits = int(var_type[2:])
    if expression[0] != "(" and expression[0] != "!": # constant
        return stored_value(bits, expression)
    elif expression[0] == "!": # NOT
        inner_expression = expression[4:-2]
        if inner_expression[0] != "(" and inner_expression[0] != "!": # this is a basic NOT
            not_exp_val = compute_basic_not(vars, inner_expression)
            return stored_value(bits, not_exp_val)
        elif inner_expression[0] == "!": # this is a NOT-NOT structure
            inner_expression_2 = inner_expression[4:-2]
            not_exp_val_2 = compute_basic_not(vars, inner_expression_2)
            not_exp_val = compute_basic_not(vars, not_exp_val_2)
            return stored_value(bits, not_exp_val)
        else:   # begin with "(", this is NOT - other basic expressions
            if "&" in inner_expression: # NOT - AND
                op_pos = inner_expression.find("&")
                left_exp = inner_expression[2:op_pos-3]
                right_exp = inner_expression[op_pos+4:-2]
                and_exp_val_2 = compute_basic_and(vars, left_exp, right_exp)
                not_exp_val = compute_basic_not(vars, and_exp_val_2)
                return stored_value(bits, not_exp_val)
            elif "|" in inner_expression: # NOT - OR
                op_pos = inner_expression.find("|")
                left_exp = inner_expression[2:op_pos-3]
                right_exp = inner_expression[op_pos+4:-2]
                or_exp_val_2 = compute_basic_or(vars, left_exp, right_exp)
                not_exp_val = compute_basic_not(vars, or_exp_val_2)
                return stored_value(bits, not_exp_val)
            elif "+" in inner_expression:
                op_pos = inner_expression.find("+")
                left_exp = inner_expression[2:op_pos-3]
                right_exp = inner_expression[op_pos+4:-2]
                add_exp_val_2 = compute_basic_add(vars, left_exp, right_exp)
                not_exp_val = compute_basic_not(vars, add_exp_val_2)
                return stored_value(bits, not_exp_val)
            elif "-" in inner_expression:
                op_pos = inner_expression.find("-")
                left_exp = inner_expression[2:op_pos-3]
                right_exp = inner_expression[op_pos+4:-2]
                sub_exp_val_2 = compute_basic_sub(vars, left_exp, right_exp)
                not_exp_val = compute_basic_not(vars, sub_exp_val_2)
                return stored_value(bits, not_exp_val)
    else: # begin with "(", this is other operations except NOT, need to consider left and right parts
        if expression[2] != "(" and expression[2] != "!": # left part is a constant or variable
            first_rp = expression.find(")")
            left_expression = expression[2:first_rp-1]
            left_val = constant_or_var(left_expression)
            # then need to consider the right part
            right_expression = expression[first_rp+4:]
            if right_expression[2] != "(" and right_expression[2] != "!":
                right_val = constant_or_var(right_expression[2:-2])
            elif right_expression[2] == "!":
                inner_expression = right_expression[6:-4]
                right_val = compute_basic_not(vars, inner_expression)
            else:
                right_expression = right_expression[2:-2]
                if "&" in right_expression:
                    op_pos = right_expression.find("&")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_and(vars, left_exp, right_exp)
                elif "|" in right_expression:
                    op_pos = right_expression.find("|")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_or(vars, left_exp, right_exp)
                elif "+" in right_expression:
                    op_pos = right_expression.find("+")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_add(vars, left_exp, right_exp)
                elif "-" in right_expression:
                    op_pos = right_expression.find("-")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_sub(vars, left_exp, right_exp)
            operation = expression[first_rp+2]
            if operation == "&":
                exp_val = compute_basic_and(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "|":
                exp_val = compute_basic_or(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "+":
                exp_val = compute_basic_add(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "-":
                exp_val = compute_basic_sub(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            
        elif expression[2] == "!": # left part is a basic NOT
            first_rp = expression.find(")")
            inner_expression = expression[6:first_rp-1]
            left_val = compute_basic_not(vars, inner_expression)
            right_expression = expression[first_rp+6:]
            if right_expression[2] != "(" and right_expression[2] != "!":
                right_val = constant_or_var(right_expression[2:-2])
            elif right_expression[2] == "!":
                inner_expression = right_expression[6:-4]
                right_val = compute_basic_not(vars, inner_expression)
            else:
                right_expression = right_expression[2:-2]
                if "&" in right_expression:
                    op_pos = right_expression.find("&")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_and(vars, left_exp, right_exp)
                elif "|" in right_expression:
                    op_pos = right_expression.find("|")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_or(vars, left_exp, right_exp)
                elif "+" in right_expression:
                    op_pos = right_expression.find("+")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_add(vars, left_exp, right_exp)
                elif "-" in right_expression:
                    op_pos = right_expression.find("-")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_sub(vars, left_exp, right_exp)
            operation = expression[first_rp+4]
            if operation == "&":
                exp_val = compute_basic_and(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "|":
                exp_val = compute_basic_or(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "+":
                exp_val = compute_basic_add(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "-":
                exp_val = compute_basic_sub(vars,left_val,right_val)
                return stored_value(bits, exp_val)

        else:  # left part begin with "("
            first_rp = expression.find(")")
            second_rp = expression.find(")", first_rp+1)
            left_expression = expression[2:second_rp+1]
            if "&" in left_expression:
                op_pos = left_expression.find("&")
                left_exp = left_expression[2:op_pos-3]
                right_exp = left_expression[op_pos+4:-2]
                left_val = compute_basic_and(vars, left_exp, right_exp)
            elif "|" in left_expression:
                op_pos = left_expression.find("|")
                left_exp = left_expression[2:op_pos-3]
                right_exp = left_expression[op_pos+4:-2]
                left_val = compute_basic_or(vars, left_exp, right_exp)
            elif "+" in left_expression:
                op_pos = left_expression.find("+")
                left_exp = left_expression[2:op_pos-3]
                right_exp = left_expression[op_pos+4:-2]
                left_val = compute_basic_add(vars, left_exp, right_exp)
            elif "-" in left_expression:
                op_pos = left_expression.find("-")
                left_exp = left_expression[2:op_pos-3]
                right_exp = left_expression[op_pos+4:-2]
                left_val = compute_basic_sub(vars, left_exp, right_exp)
            
            right_expression = expression[second_rp+6:]
            if right_expression[2] != "(" and right_expression[2] != "!":
                right_val = constant_or_var(right_expression[2:-2])
            elif right_expression[2] == "!":
                inner_expression = right_expression[6:-4]
                right_val = compute_basic_not(vars, inner_expression)
            else:
                right_expression = right_expression[2:-2]
                if "&" in right_expression:
                    op_pos = right_expression.find("&")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_and(vars, left_exp, right_exp)
                elif "|" in right_expression:
                    op_pos = right_expression.find("|")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_or(vars, left_exp, right_exp)
                elif "+" in right_expression:
                    op_pos = right_expression.find("+")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_add(vars, left_exp, right_exp)
                elif "-" in right_expression:
                    op_pos = right_expression.find("-")
                    left_exp = right_expression[2:op_pos-3]
                    right_exp = right_expression[op_pos+4:-2]
                    right_val = compute_basic_sub(vars, left_exp, right_exp)
            operation = expression[second_rp+4]
            if operation == "&":
                exp_val = compute_basic_and(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "|":
                exp_val = compute_basic_or(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "+":
                exp_val = compute_basic_add(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            elif operation == "-":
                exp_val = compute_basic_sub(vars,left_val,right_val)
                return stored_value(bits, exp_val)
            

if __name__ == "__main__":
    with open("./input.pig", "r") as f:
        g = open("./1.out", "w") 
        vars = dict()
        lines = f.readlines()
        statements_num = 0
        global_target_line = 0
        for k in range(len(lines)):
            if (k < global_target_line):
                continue
            line = lines[k]
            statements_num += 1
            if statements_num > 5000:
                print("too-many-lines")
                break
            if line[0] == 'D':
                # initialize the variable value to be 0
                var_type = line[2:-5]
                bits = int(var_type[2:])
                vars[line[-5:-1]] = [var_type, "0" * bits]
            if line[0] == 'A':
                value_exp = line[9:-3]
                var_type = vars[line[2:6]][0]
                vars[line[2:6]][1] = compute_exp_value(vars, var_type, value_exp)
            if line[0] == 'O':
                print(vars[line[2:6]][1], file=g)

            if line[0] == "R":
                del vars[line[2:-1]]
            if line[0] == "B":
                target_line = int(line[2:5])
                value_exp = line[8:-3]
                value_res = compute_exp_value(vars, "bv64", value_exp)
                decimal_value = int(value_res, 2)
                if target_line < k:
                    while decimal_value != 0:
                        for i in range(target_line, k):
                            statements_num += 1
                            if statements_num > 5000:
                                print("too-many-lines")
                                break
                            b_line = lines[i]
                            if b_line[0] == 'D':
                                # initialize the variable value to be 0
                                var_type = b_line[2:-5]
                                bits = int(var_type[2:])
                                vars[b_line[-5:-1]] = [var_type, "0" * bits]
                            if b_line[0] == 'A':
                                value_exp = b_line[9:-3]
                                var_type = vars[b_line[2:6]][0]
                                vars[b_line[2:6]][1] = compute_exp_value(vars, var_type, value_exp)
                            if b_line[0] == 'O':
                                print(vars[b_line[2:6]][1], file=g)
                            if b_line[0] == "R":
                                del vars[b_line[2:-1]]
                        statements_num += 1
                        if statements_num > 5000:
                            break
                        value_exp = line[8:-3]
                        value_res = compute_exp_value(vars, "bv64", value_exp)
                        decimal_value = int(value_res, 2)
                else:
                    global_target_line = target_line