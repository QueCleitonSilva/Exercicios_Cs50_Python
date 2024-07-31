#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool is_digit(string s);

int main(int argc, string argv[])
{
    // Verifica se há exatamente um argumento de linha de comando
    if (argc != 2 || !is_digit(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Converte o argumento de linha de comando para um inteiro
    int k = atoi(argv[1]);

    // Obtém o texto plano do usuário
    string plaintext = get_string("plaintext:  ");

    // Cria um buffer para o texto cifrado
    char ciphertext[strlen(plaintext) + 1];

    // Aplica a cifra de César ao texto plano
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            char base = islower(plaintext[i]) ? 'a' : 'A';
            ciphertext[i] = (plaintext[i] - base + k) % 26 + base;
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }

    // Adiciona o terminador nulo ao texto cifrado
    ciphertext[strlen(plaintext)] = '\0';

    // Imprime o texto cifrado
    printf("ciphertext: %s\n", ciphertext);

    // Retorna 0 para indicar que o programa terminou com sucesso
    return 0;
}

// Função para verificar se uma string contém apenas dígitos
bool is_digit(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit((unsigned char) s[i]))
        {
            return false;
        }
    }
    return true;
}
