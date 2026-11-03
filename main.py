# Variáveis de estado
tentativas = 3
pontos = 0

# Pergunta
pergunta = 'Quantos lados tem um triângulo? '

while tentativas > 0:
    resposta = int(input(pergunta))

    if resposta == 3:
        print('Resposta correta!')
        pontos = pontos + 1
        break
    else:
        print( 'Resposta errada')
        tentativas = tentativas - 1
        print(f'Você tem {tentativas} tentativa(s)...')

print(f'Pontuação: {pontos}.')