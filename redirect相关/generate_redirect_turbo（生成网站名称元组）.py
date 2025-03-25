def format_title_to_urls(titles, base_url, target_url_prefix):
    """
    将标题格式化为特定的URL规则并填入列表

    参数:
    - titles: 标题列表
    - base_url: 源URL的基础路径
    - target_url_prefix: 目标URL的前缀
    """
    formatted_urls = []

    for title in titles:
        # 将标题转换为URL友好的格式
        formatted_title = title.lower().replace(' ', '-')
        source_url = f"{base_url}/{formatted_title}"
        target_url = f"{target_url_prefix}/{formatted_title}"
        formatted_urls.append((source_url, target_url))

    return formatted_urls

# 示例标题列表
titles = [
"how-to-lock-windows-10-pc.html",
]

# 基础路径和目标URL前缀
base_url = "windows-tips"
target_url_prefix = "https://www.isumsoft.com/windows-tips/how-to-disable-lock-screen-in-windows-10.html"

# 格式化标题并生成URL规则列表
formatted_urls = format_title_to_urls(titles, base_url, target_url_prefix)

# 打印结果
for source, target in formatted_urls:
    print("("f"'{source}', '{target}'"")"",")
