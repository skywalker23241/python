import os

def list_files(directory):
    """
    This function takes a directory path as input and returns a list of file names in that directory.
    """
    try:
        files = os.listdir(directory)
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        return files
    except Exception as e:
        print(f"Error: {e}")
        return []

def generate_alt_list(filenames):
    """
    This function takes a list of filenames and returns a list of formatted alt text.
    """
    formatted_filenames = []
    for filename in filenames:
        name_without_extension = filename.replace(".png", "").replace(".jpg", "").replace(".jpeg", "")
        words = name_without_extension.split("-")
        capitalized_words = [word.capitalize() for word in words]
        formatted_name = " ".join(capitalized_words)
        formatted_filenames.append(formatted_name)
    return formatted_filenames

def generate_img_urls(filenames, base_url):
    """
    This function takes a list of filenames and a base URL, and returns a list of formatted HTML img tags.
    """
    img_urls = []
    for filename in filenames:
        src_path = os.path.join(base_url, filename).replace("\\", "/")
        img_urls.append(src_path)
    return img_urls

def main(image_folder):
    # Step 1: List all files in the directory
    files = list_files(image_folder)
    
    # Step 2: Generate alt text for all files
    alts = generate_alt_list(files)
    
    # Step 3: Generate img URLs for all files
    urls = generate_img_urls(files, image_folder)
    
    for filename, alt, url in zip(files, alts, urls):
        html_img_tag = f'<img src="{url}" width="" height="" alt="{alt}">'
        print(html_img_tag)

if __name__ == "__main__":
    image_folder = r'C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\images\mac-tips\how-to-use-your-macbook-entire-day-without-charing'  # 直接在这里设置图片文件夹路径
    main(image_folder)
