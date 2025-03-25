import re

# 读取Xenu导出的报告文件
with open(r'C:\Users\le187\Desktop\Xenu1.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用正则表达式匹配所有的broken links
# 假设broken links以 "Broken" 或 "Not found" 等关键词标识
broken_links = re.findall(r'Broken\s+Link:\s+(http[s]?://\S+)', content)

# 将所有broken links写入到一个新的文本文件中
with open('broken_links.txt', 'w', encoding='utf-8') as output_file:
    for link in broken_links:
        output_file.write(link + '\n')

print("Broken links 已成功导出到 'broken_links.txt'")
