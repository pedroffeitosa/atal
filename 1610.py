arr_documentsA = []
arr_documentsB = []
arr_documents = []
ans = []

tests = int(input())
for i in range(tests):
    documents, dependences = list(map(int, input().split()))
    loop = 0    

    for i in range(dependences):
        a, b = list(map(int, input().split()))

        if loop == 0:        
            arr_documentsA.append(a)
            arr_documentsB.append(b)
            if a not in arr_documents:
                arr_documents.append(a)
            if b not in arr_documents:
                arr_documents.append(b)
            if a in arr_documentsB:
                b in arr_documentsA
                loop += 1
    if loop == 0:
        ans.append("NAO")
    else:
        ans.append("SIM")
    
for i in range(tests):
    print(ans[i])
