
text = input("Enter text to write to the file: ")

with open('output.txt', 'w') as file:
    file.write(text + '\n')
    print('Data Successfully Written to output.txt')
add_text = input("Enter more text to append to the file: ")
print('Data successfully appended.')
with open('output.txt', 'a') as file:
    file.write(add_text + '\n')


print("\nFinal content of output.txt:")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
