import subprocess
import os

def resize_webp_images_in_folder(folder_path, width=800):
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return
    
    # Get a list of all .webp files in the folder
    webp_files = [f for f in os.listdir(folder_path) if f.endswith('.webp')]
    
    if not webp_files:
        print("No .webp files found in the folder.")
        return
    
    for webp_file in webp_files:
        # Define input and output paths for each file
        input_path = os.path.join(folder_path, webp_file)
        output_path = os.path.join(r"C:\Users\le187\Desktop\python\blog相关\adjust_px（调整像素大小）", f"{webp_file}")
        
        # Construct the ImageMagick command
        command = [
            'magick', 'convert',  # Use 'magick' for ImageMagick on Windows
            input_path,
            '-resize', f'{width}x',  # Resize width to 800px, keeping aspect ratio
            output_path
        ]
        
        # Run the command
        try:
            subprocess.run(command, check=True)
            print(f"Resized {webp_file} successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error resizing {webp_file}: {e}")

# Example usage
folder_path = r"C:\Users\le187\Desktop\iSumsoft_Web_3\trunk\images\mac-tips\how-to-use-your-macbook-entire-day-without-charing"

resize_webp_images_in_folder(folder_path)
