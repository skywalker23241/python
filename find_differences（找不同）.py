def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def find_differences(file1_data, file2_data):
    set_file1 = set(file1_data)
    set_file2 = set(file2_data)

    differences = {
        'only_in_file1': list(set_file1 - set_file2),
        'only_in_file2': list(set_file2 - set_file1),
        'in_both_files': list(set_file1 & set_file2)
    }

    return differences

def main():
    # 在这里指定你的文件路径
    file1_path = r'C:\Users\le187\Desktop\1.txt'
    file2_path = r'C:\Users\le187\Desktop\2.txt'

    file1_data = read_file(file1_path)
    file2_data = read_file(file2_path)

    differences = find_differences(file1_data, file2_data)


    print("\nIn both files:")
    for line in differences['in_both_files']:
        print(line.strip())

if __name__ == "__main__":
    main()
