def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()
            
            if content1 == content2:
                return 0
            else:
                return 1  
    except FileNotFoundError:
        return -1
    

if __name__ == "__main__":
    file_name1 = "./1.out"
    file_name2 = "./2.out"
    out = open("./res.out", "w")
    result = compare_files(file_name1,file_name2)
    if result != -1:
        print(result, file=out)
    else:
        print("file doesn't exist!")