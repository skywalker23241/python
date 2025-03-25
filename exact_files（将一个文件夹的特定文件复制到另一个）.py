import os
import shutil

def extract_specific_files(source_folder, destination_folder, specific_filenames):
    # 确保目标文件夹存在
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # 遍历源文件夹中的文件
    for filename in os.listdir(source_folder):
        # 检查文件名是否在特定名称列表中
        if filename in specific_filenames:
            # 构建源文件和目标文件的完整路径
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            
            # 复制文件到目标文件夹
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {filename}")

# 示例参数
source_folder = r"C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\windows-10"  # 替换为你的源文件夹路径
destination_folder = r"C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\windows-tips"  # 替换为你的目标文件夹路径
specific_filenames = [
"2-ways-delete-user-profile-in-windows-10.html",
"2-ways-remove-double-blue-arrows-on-icons.html",
"2-ways-to-add-or-remove-languages-on-windows-10.html",
"2-ways-to-check-if-window-10-supports-miracast.html",
"2-ways-to-clear-quick-access-history.html",
"2-ways-to-enable-default-account-on-windows-10.html",
"2-ways-to-perform-a-full-shutdown.html",
"2-ways-to-remove-suggested-apps-from-start.html",
"2-ways-upgrade-to-windows-10-enterprise.html",

# 继续添加你需要的特定文件名
]

# 调用函数
extract_specific_files(source_folder, destination_folder, specific_filenames)
