

sample_file = 'sample.txt'

try:
    with open(sample_file,'r') as file:
        read_lines = file.readlines()
        print('Reading contents of file:')
        for i , line in enumerate(read_lines, start=1):
            print(f'This is Line {i}: {line}', end='')
except FileNotFoundError:
    print(f'Error: The file {sample_file} not found.')

