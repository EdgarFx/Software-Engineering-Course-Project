import subprocess
import filecmp

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e.output.decode('utf-8'))

def are_files_identical(file1, file2):
    return filecmp.cmp(file1, file2)

for i in range(100):
    command_to_execute = "python gen.py"
    execute_command(command_to_execute)
    command_to_execute = "python pig.py"
    execute_command(command_to_execute)
    command_to_execute = "pig3.exe < input.pig > 2.out"
    execute_command(command_to_execute)
    with open('input.pig', 'r') as f1, open(f'./test_files/{i}.out', 'w') as f2:
        for line in f1:
            f2.write(line)

    file1_path = "1.out"
    file2_path = "2.out"
    if are_files_identical(file1_path, file2_path):
        print(i)
        print("Same")
    else:
        print(i)
        print("Different")

