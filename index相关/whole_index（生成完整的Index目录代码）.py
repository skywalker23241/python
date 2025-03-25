def generate_li_items(links, titles, descriptions):
    li_items = []
    
    for link, title, description in zip(links, titles, descriptions):
        li_item = f'''
        <li class="li-container">
            <a href="{link}">{title}</a>
            <p>{description}</p>
        </li>
        '''
        li_items.append(li_item.strip())
    
    return "\n".join(li_items)

# 示例用法
links = [
"2-methods-for-the-recovery-of-encrypted-word-file.html",
###所有的网页文件名称
]

titles = [
"2 Methods for the Recovery of Encrypted Word Files",
###提取的h1标签
]

descriptions = [
    
"In the previous article, we introduced how to recover an unsaved Word document. But what should we do for the encrypted Word files? Discard them to the Recycle Bin? Definitely not! This passage, 2 methods for the recovery of encrypted word file, will show you how to deal with this problem without data loss, including a free method.",
"File History is a file backup tool built in Windows 10, which can automatically and quickly back up personal files from the computer to an external drive. This is much more convenient than manual copy or transfer, especially if you have large number of files to back up.",
###所有的描述文本，其中不能有引号，否则报错。
]
# 生成HTML <li> 元素
html_output = generate_li_items(links, titles, descriptions)
print(html_output)
