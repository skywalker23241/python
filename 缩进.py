import re
import os

def clean_img_tag(img_tag):
    # 处理 src 和 alt 属性值
    img_tag = re.sub(r'\s*src\s*=\s*"([^"]*)"\s*', lambda m: f'src="{clean_img_path(m.group(1))}"', img_tag)
    img_tag = re.sub(r'\s*alt\s*=\s*"([^"]*)"\s*', lambda m: f'alt="{m.group(1).strip()}"', img_tag)
    return img_tag

def clean_img_path(path):
    # 处理 src 属性中的路径格式问题
    path = re.sub(r'\s+', ' ', path)  # 将多个空格替换为单个空格
    path = re.sub(r'\/\s*', '/', path)  # 去除斜杠后的多余空格
    path = re.sub(r'\s*\/', '/', path)  # 去除斜杠前的多余空格
    cleaned_path = path.strip()
    return cleaned_path


def format_li_tag(li_text):
    # 使用正则表达式提取原始的 <a> 标签和 <img> 标签中的信息
    link_match = re.search(r'href="([^"]+)"', li_text)
    img_tag_match = re.search(r'<img [^>]*>', li_text)
    text_match = re.search(r'</span>\s*<a[^>]*>([^<]+)</a>', li_text)

    if link_match and img_tag_match and text_match:
        link = link_match.group(1)
        img_tag = img_tag_match.group(0)
        # 清理 <img> 标签中的空格和路径格式
        cleaned_img_tag = clean_img_tag(img_tag)
        img_src_match = re.search(r'src="([^"]+)"', cleaned_img_tag)
        img_alt_match = re.search(r'alt="([^"]+)"', cleaned_img_tag)
        text = ' '.join(text_match.group(1).split())  # 处理 <a> 标签中的文本内容

        if img_src_match and img_alt_match:
            img_src = img_src_match.group(1)
            img_alt = img_alt_match.group(1)

            # 使用模板替换内容
            return f'''
<li>
    <span>
        <a href="{link}">
        <img src="{img_src}" alt="{img_alt}" />
        </a>
    </span>
        <a href="{link}">{text}</a>
</li>'''
    return li_text

def format_html_content(content):
    # 查找并处理 <div class="related-articles clearfloat"> 内的 <li> 标签
    def replace_li(match):
        return re.sub(r'(<li>[\s\S]*?</li>)', lambda m: format_li_tag(m.group(0)), match.group(0))
    
    formatted_content = re.sub(r'(<div class="related-articles clearfloat">[\s\S]*?</div>)', replace_li, content)
    return formatted_content

def process_html_files(directory):
    # 遍历指定目录中的所有文件
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.html'):  # 仅处理HTML文件
                file_path = os.path.join(root, file_name)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # 处理 HTML 内容
                formatted_content = format_html_content(content)

                # 将格式化后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(formatted_content)

                print(f"Processed file: {file_path}")

# 指定包含HTML文件的目录路径
html_directory = r'C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\backup-recovery'

# 处理目录中的所有HTML文件
process_html_files(html_directory)

print("所有文件处理完成。")
