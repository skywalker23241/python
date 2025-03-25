import os

def list_files(directory):
    """
    This function takes a directory path as input and returns a list of file names in that directory.
    """
    try:
        # List all files and directories in the specified directory
        files = os.listdir(directory)

        # Filter out directories, only keep files
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

        return files
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
directory_path = r'C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\windows-tips'
file_names = list_files(directory_path)

for file_name in file_names:
    print(f"\"{file_name}\",")
