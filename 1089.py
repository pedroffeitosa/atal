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


# while True:
#     pontos = int(input())
    
#     if pontos == 0:
#         break
    
#     arr_pontos = [int(x) for x in input().split()]
#     arr_pontos.append(arr_pontos[0])
#     arr_pontos.append(arr_pontos[1])
#     picos = 0
#     for i in range(1, pontos+1):
#         if arr_pontos[i] < arr_pontos[i-1] and arr_pontos[i] < arr_pontos[i+1]:
#             picos += 1
#         elif arr_pontos[i] > arr_pontos[i-1] and arr_pontos[i] > arr_pontos[i+1]:
#             picos += 1
#     print(picos)
