text = input('Enter your text here: ')

total_characters = len(text)
letters = 0
digits = 0
spaces = 0
uppercase = 0
lowercase = 0


for i in text:
    if i.isalpha():
        letters += 1
        if i.isupper():
            uppercase += 1
        else:
            lowercase += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
    else:
        continue
    
print(f'''
total_characters = {total_characters}
letters = {letters} 
digits = {digits} 
spaces = {spaces} 
uppercase = {uppercase} 
lowercase = {lowercase} 
''')