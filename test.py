from bs4 import BeautifulSoup
import requests

# 解析 HTML 内容
def parse_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # 提取关键词和元描述
    keywords = soup.find("meta", attrs={"name": "Keywords"})
    description = soup.find("meta", attrs={"name": "Description"})
    
    # 获取 H1, H2, H3 标题
    h1 = soup.find("h1").get_text() if soup.find("h1") else None
    h2 = [h2.get_text() for h2 in soup.find_all("h2")]
    h3 = [h3.get_text() for h3 in soup.find_all("h3")]

    # 获取导言/首段
    first_paragraph = soup.find("p").get_text() if soup.find("p") else None

    # 获取所有图片的 URL 和 ALT 标签
    images = [{"src": img.get("src"), "alt": img.get("alt")} for img in soup.find_all("img")]

    # 返回解析结果
    parsed_data = {
        "keywords": keywords["content"] if keywords else None,
        "description": description["content"] if description else None,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "first_paragraph": first_paragraph,
        "images": images
    }
    
    return parsed_data

# 主程序
if __name__ == "__main__":
    url = input(r"C:\Users\Admin\Desktop\3-ways-to-fix-the-android-recovery-mode-not-working-problem.html")
    
    if url.startswith("http"):  # 处理在线网页
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
        else:
            print("Failed to fetch the page.")
            exit()
    else:  # 处理本地 HTML 文件
        try:
            with open(url, "r", encoding="utf-8") as file:
                html_content = file.read()
        except FileNotFoundError:
            print(f"File {url} not found.")
            exit()
    
    parsed_data = parse_html(html_content)
    print(parsed_data)
