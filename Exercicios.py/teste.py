'''
def funcao_nome(nome, idade):
    print('Meu nome é ' + nome + '.')
    print('Tenho '+ str(idade) + ' anos.')


funcao_nome('Cláudio', 43)
funcao_nome('Amanda', 39)
'''
# variavel global
numero = 10

def sumario():
    #transforma global
    global numero
    #variavel local
    numero = 20
    print('Inicial: ' + str(numero))

sumario()
print('Final: ' + str(numero))

