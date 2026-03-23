import difflib

def generate_diff(file1, file2):
    """Generate a unified diff between two text files."""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()
    
    diff = difflib.unified_diff(file1_lines, file2_lines, fromfile=file1, tofile=file2)
    return ''.join(diff)

def main():
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    diff = generate_diff(file1, file2)
    print(diff)

if __name__ == '__main__':
    main()