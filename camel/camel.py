## python camel.py

def main():
    camelcase_var = input("Imput in camelCase: ")
    snakecase_var = camelsnake(camelcase_var)
    print(snakecase_var)

def camelsnake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

if __name__ == "__main__":
    main()
