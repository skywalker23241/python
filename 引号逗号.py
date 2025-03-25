# Specify the path to your input file
input_file_path = r'C:\Users\le187\Desktop\1.txt'  # Windows路径示例
# Or for macOS/Linux
# input_file_path = '/path/to/your/input.txt'

# Specify the path to your output file
output_file_path = r'C:\Users\le187\Desktop\2.txt'  # Windows路径示例
# Or for macOS/Linux
# output_file_path = '/path/to/your/output.txt'

# Read the input file
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Process each line
processed_lines = [f'"{line.strip()}",\n' for line in lines]

# Write the output to a new file
with open(output_file_path, 'w') as file:
    file.writelines(processed_lines)
