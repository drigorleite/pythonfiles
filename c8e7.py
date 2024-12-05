def characterAnalysis():
    with open('text.txt', 'r') as file:
        content = file.read()

    uppercase = sum(char.isupper() for char in content)
    lowercase = sum(char.islower() for char in content)
    digits = sum(char.isdigit() for char in content)
    whitespace = sum(char.isspace() for char in content)

    return uppercase, lowercase, digits, whitespace


print(characterAnalysis())
