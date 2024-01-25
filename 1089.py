aux = True
dir = 0
           
def isValid(a, b):
    if a == b:
        return False
    elif a == 0:
        return False
    elif b == 0:
        return False
    else:
        return True

def sobeOuDesce(a, b):
    if a < b:
        return 1
    else:
        return -1 

        
while aux == True:
    num_pontos = int(input())
    count = 0
    dir_atual = dir
    
    if num_pontos == 0:
        aux = False
    else:
        entrada = input()
        linha_de_pontos = entrada.split(' ')

        for i in range(len(linha_de_pontos)-1):
            a = int(linha_de_pontos[i])
            b = int(linha_de_pontos[i+1])

            if isValid(a, b) == True:
                dir_atual = sobeOuDesce(a, b)
                if dir_atual != dir:
                    count += 1

        print(count+1)                



