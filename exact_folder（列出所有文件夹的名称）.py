import os

def print_folder_names(source_folder):
    # 遍历源文件夹中的所有文件和文件夹
    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)
        
        # 检查是否为文件夹
        if os.path.isdir(item_path):
            # 打印文件夹名称
            print(f"\"{item}\",")

# 示例参数
source_folder = r"C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\images\computer-tweaks"  # 替换为你的源文件夹路径

# 调用函数
print_folder_names(source_folder)
