import os
from bs4 import BeautifulSoup

# 指定文件夹路径
folder_path = r'C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\backup-recovery'###输入需要提取的文件夹路径

# 用于存储结果
h1_contents = []
p2_contents = []

# 获取文件夹中的所有HTML文件，并按文件名排序
html_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.html')])

# 遍历所有排序后的HTML文件
for filename in html_files:
    file_path = os.path.join(folder_path, filename)
    
    # 打开并读取HTML文件
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        
        # 查找第一个<h1>标签
        h1_tag = soup.find('h1')
        if h1_tag:
            h1_contents.append((filename, h1_tag.get_text()))
        
        # 查找所有<p>标签，并提取第二个<p>标签的内容
        p_tags = soup.find_all('p')
        if len(p_tags) > 1:
            p2_contents.append((filename, p_tags[1].get_text()))
        else:
            p2_contents.append((filename, "文件中没有足够的<p>标签"))

# 打印第一个<h1>标签的内容
for filename, content in h1_contents:
    print(f"\"{content}\",")

# 打印第二个<p>标签的内容
for filename, content in p2_contents:
    print(f"\"{content}\",")
