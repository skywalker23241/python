import os
import re
import subprocess

def tidy_html(content):
    # 将需要处理的部分写入临时文件
    with open("temp.html", "w", encoding="utf-8") as temp_file:
        temp_file.write(content)

    # 使用 Tidy 处理临时文件
    subprocess.run(["tidy", "-m", "-i", "-wrap", "0", "temp.html"])

    # 读取 Tidy 处理后的内容
    with open("temp.html", "r", encoding="utf-8") as temp_file:
        tidy_content = temp_file.read()

    return tidy_content

def replace_html_section(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 正则表达式提取指定部分
    pattern = re.compile(r'(<div class="bread">.*?<!--\s+#EndLibraryItem\s+--></div>)', re.DOTALL)
    match = pattern.search(content)

    if match:
        # 提取的部分
        section = match.group(1)

        # 使用 Tidy 处理提取的部分
        tidy_section = tidy_html(section)

        # 替换原始内容中的部分
        new_content = content.replace(section, tidy_section)

        # 写回文件
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)

        print(f"File processed: {file_path}")
    else:
        print(f"No matching section found in: {file_path}")

def process_folder(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                replace_html_section(file_path)

# 使用示例：设置要处理的文件夹路径
folder_path = r"C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\backup-recovery"
process_folder(folder_path)
