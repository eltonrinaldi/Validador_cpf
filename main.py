import re
import sys

print(f'{20*'*'} Validador de CPF {20*'*'}\n')

cpf_enviado = input('Coloque seu CPF: ')
cpf_sequencial = cpf_enviado == cpf_enviado[0] * len(cpf_enviado)

if cpf_sequencial:
    print('Voce enviou dados sequencial')
    sys.exit()

cpf = re.sub(r'[^0-9]', '', cpf_enviado)
nove_digitos = cpf[:9]
contagem_regressiva = 10
digito_1 = 0
digito_final = ''

for digito in nove_digitos:
    digito_1 += int(digito) * contagem_regressiva
    contagem_regressiva -= 1
    
digito_1 = (digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

digito_final += str(digito_1)

nove_digitos = cpf[:9] + str(digito_1)
contagem_regressiva = 11
digito_2 = 0

for digito2 in nove_digitos:
    digito_2 += int(digito2) * contagem_regressiva
    contagem_regressiva -= 1
    
digito_2 = (digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

nove_digitos = cpf[:10] + str(digito_2)

digito_final += str(digito_2)

if digito_final == cpf[9:]:
    print(f'{cpf} cpf válido')

else:
    print('cpf invalido')




