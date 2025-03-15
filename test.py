import os

# Specify the parent directory where the folders are located
parent_dir = 'DSA_DAILY_PRACTICE/'

# List all directories (folders) inside the parent directory
folders = [f.path for f in os.scandir(parent_dir) if f.is_dir()]

# C++ code content for the file
cpp_code = '''#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
'''

# Iterate over each folder in the list
for folder in folders:
    # Create the full path for the C++ file
    cpp_file_path = os.path.join(folder, 'main.cpp')
    
    # Open the file in write mode and write the C++ code
    with open(cpp_file_path, 'w') as cpp_file:
        cpp_file.write(cpp_code)
    print(f'Created {cpp_file_path}')
