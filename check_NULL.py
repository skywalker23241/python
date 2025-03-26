from bs4 import BeautifulSoup
import requests

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # 提取meta信息
    meta_keywords = soup.find("meta", attrs={"name": "keywords"})
    keywords = meta_keywords["content"] if meta_keywords else ""
    
    meta_description = soup.find("meta", attrs={"name": "description"})
    description = meta_description["content"] if meta_description else ""
    
    # 提取导言/首段
    first_paragraph = soup.find("p")
    first_paragraph_text = first_paragraph.get_text(strip=True) if first_paragraph else ""
    
    # 提取标题信息
    headings = {f'h{i}': [tag.get_text(strip=True) for tag in soup.find_all(f'h{i}')] for i in range(1, 4)}
    
    # 提取目录（h2/h3 结构）
    toc = {f'h{i}': [tag.get_text(strip=True) for tag in soup.find_all(f'h{i}')] for i in range(2, 4)}
    
    # 提取图片信息
    images = [
        {"src": img["src"], "alt": img.get("alt", "")}
        for img in soup.find_all("img") if img.get("src")
    ]
    
    # 返回结果
    return {
        "keywords": keywords,
        "description": description,
        "first_paragraph": first_paragraph_text,
        "headings": headings,
        "toc": toc,
        "images": images
    }

if __name__ == "__main__":
    url = input("https://www.isumsoft.com/android/factory-reset-samsung-phone-that-is-locked.html")
    response = requests.get(url)
    if response.status_code == 200:
        parsed_data = parse_html(response.text)
        print(parsed_data)
    else:
        print("Failed to fetch the page.")