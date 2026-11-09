# Variáveis de estado
tentativas = 3
pontos = 0
acertos = 0

# Pergunta
pergunta = 'Quantos lados tem um triângulo? '
perguntas = ["Quanto é 7 + 8?", "Qual é a capital do Brasil?", "Quantas horas tem um dia?"]
respostas = ["15", "Brasilia", "24"]

while tentativas > 0:
    resposta = int(input(pergunta))

    if resposta == 3:
for i in range(3):
    resposta = input(perguntas[i])
    if resposta == respostas[i]:
        pontos += 1
        acertos += 1
        print('Resposta correta!')
        pontos = pontos + 1
        break
    else:
        print( 'Resposta errada')
        tentativas = tentativas - 1
        print(f'Você tem {tentativas} tentativa(s)...')
        print('Resposta errada!')

print(f'Pontuação: {pontos}.')
print(f'Pontuação final: {pontos}. Você acertou {acertos} perguntas...')