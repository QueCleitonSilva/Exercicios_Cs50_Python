def main():
    text = input("input: ")  # Não é necessário usar str(input()), pois input() já retorna uma string

    for char in text:
        if char.lower() not in ['a', 'e', 'i', 'o', 'u']:  # Verifica se o caractere não é uma vogal
            print(char, end='')  # Imprime o caractere se não for uma vogal
    print()  # Imprime uma nova linha após o loop

if __name__ == "__main__":
    main()
