import os

def check_null_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # 检查文件内容是否为 "NULL"
            if "NULL" in content:
                print(f"Warning: File contains 'NULL' content - {file_path}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                check_null_content(file_path)

# 使用示例：设置要处理的文件夹路径
folder_path = r"C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\computer-tweaks"
process_folder(folder_path)
