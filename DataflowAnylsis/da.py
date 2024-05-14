import sys

def check_declare(vars, var_name):
    try:
        if vars[var_name] == 1:
            return True
        else:
            return False
    except:
        return False


def deep_copy_dict(d):
    new_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            new_dict[key] = deep_copy_dict(value)
        else:
            new_dict[key] = value
    return new_dict


def forward_branch_execute(vars, undeclared_lines, target_line, current_line, back_lines):
    back_lines = back_lines[:]
    for j in range(target_line,len(lines)):
        line_j = lines[j]
        line_j = line_j.strip()
        token = line_j[0]
        if token == "D":
            vars[line_j[-4:]] = 1
        elif token == "A":
            index = line_j.find("v")
            var_name = line_j[index:index+4]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(j)
            else:
                while index != -1:
                    index = line_j.find("v", index+1)
                    if index == -1:
                        break
                    var_name = line_j[index:index+4]
                    if check_declare(vars, var_name) != True:
                        undeclared_lines.append(j)
                        break
        elif token == "R":
            var_name = line_j[-4:]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(j)
            if var_name in vars:
                vars[var_name] = 0
        elif token == "O":
            var_name = line_j[-4:]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(j)
        elif token == "B":
            index = line_j.find("v")
            if index != -1:
                var_name = line_j[index:index+4]
                if check_declare(vars, var_name) != True:
                    undeclared_lines.append(j)
                else:
                    while index != -1:
                        index = line_j.find("v", index+1)
                        if index == -1:
                            break
                        var_name = line_j[index:index+4]
                        if check_declare(vars, var_name) != True:
                            undeclared_lines.append(j)
                            break
            inner_target_line = int(line_j[2:5])
            new_vars = deep_copy_dict(vars)
            if inner_target_line > j:
                if len(back_lines) != 0:
                    undeclared_lines = forward_branch_execute(new_vars,undeclared_lines,inner_target_line,current_line,back_lines)
                else:
                    undeclared_lines = forward_branch_execute(new_vars,undeclared_lines,inner_target_line,j,back_lines)
            elif inner_target_line < j:
                if len(back_lines) != 0:
                    if j < current_line and inner_target_line < int(lines[current_line][2:5]):
                        back_lines.append(j)
                        undeclared_lines = backward_branch_execute(new_vars,undeclared_lines,inner_target_line,j,back_lines)
                else:
                    back_lines.append(j)
                    undeclared_lines = backward_branch_execute(new_vars,undeclared_lines,inner_target_line,j,back_lines)
    return list(set(undeclared_lines))

def backward_branch_execute(vars, undeclared_lines, target_line, current_line, back_lines):
    back_lines = back_lines[:]
    for j in range(target_line,len(lines)):
        line_j = lines[j]
        line_j = line_j.strip()
        token = line_j[0]
        if token == "D":
            vars[line_j[-4:]] = 1
        elif token == "A":
            index = line_j.find("v")
            var_name = line_j[index:index+4]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(j)
            else:
                while index != -1:
                    index = line_j.find("v", index+1)
                    if index == -1:
                        break
                    var_name = line_j[index:index+4]
                    if check_declare(vars, var_name) != True:
                        undeclared_lines.append(j)
                        break
        elif token == "R":
            var_name = line_j[-4:]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(j)
            if var_name in vars:
                vars[var_name] = 0
        elif token == "O":
            var_name = line_j[-4:]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(j)
        elif token == "B":
            index = line_j.find("v")
            if index != -1:
                var_name = line_j[index:index+4]
                if check_declare(vars, var_name) != True:
                    undeclared_lines.append(j)
                else:
                    while index != -1:
                        index = line_j.find("v", index+1)
                        if index == -1:
                            break
                        var_name = line_j[index:index+4]
                        if check_declare(vars, var_name) != True:
                            undeclared_lines.append(j)
                            break
            inner_target_line = int(line_j[2:5])
            new_vars = deep_copy_dict(vars)
            if inner_target_line > j:
                back_lines.append(current_line)
                undeclared_lines = forward_branch_execute(new_vars,undeclared_lines,inner_target_line,current_line,back_lines)
            elif inner_target_line < j:
                if j < current_line and inner_target_line < target_line:
                    back_lines.append(j)
                    undeclared_lines = backward_branch_execute(new_vars,undeclared_lines,inner_target_line,j,back_lines)
    return list(set(undeclared_lines))

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    vars = dict()
    result = 0
    undeclared_lines = []
    back_lines = []
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        token = line[0]
        if token == "D":
            vars[line[-4:]] = 1
        elif token == "A":
            index = line.find("v")
            var_name = line[index:index+4]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(i)
            else:
                while index != -1:
                    index = line.find("v", index+1)
                    if index == -1:
                        break
                    var_name = line[index:index+4]
                    if check_declare(vars, var_name) != True:
                        undeclared_lines.append(i)
                        break
        elif token == "R":
            var_name = line[-4:]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(i)
            if var_name in vars:
                vars[var_name] = 0
        elif token == "O":
            var_name = line[-4:]
            if check_declare(vars, var_name) != True:
                undeclared_lines.append(i)
        elif token == "B":
            index = line.find("v")
            if index != -1:
                var_name = line[index:index+4]
                if check_declare(vars, var_name) != True:
                    undeclared_lines.append(i)
                else:
                    while index != -1:
                        index = line.find("v", index+1)
                        if index == -1:
                            break
                        var_name = line[index:index+4]
                        if check_declare(vars, var_name) != True:
                            undeclared_lines.append(i)
                            break
            # branch no matter what the expression is
            target_line = int(line[2:5])
            new_vars = deep_copy_dict(vars)
            if target_line > i:
                undeclared_lines = forward_branch_execute(new_vars,undeclared_lines,target_line,i,back_lines)
            elif target_line < i:
                back_lines.append(i)
                undeclared_lines = backward_branch_execute(new_vars,undeclared_lines,target_line,i,back_lines)
                        
    result = len(set(undeclared_lines))
    print(result)