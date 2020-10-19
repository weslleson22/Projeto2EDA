


f = open("file.txt",'r')
linha = f.readlines()

x = 0

while x < len(linha):
    if linha[x] == "\n":
        local = linha.index(linha[x])
        linha.pop(local)
    else:
        linha[x] = linha[x].split(',')
        x += 1

# Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.

for i in linha:
    local = linha.index(i) # Local do i em texto
    for b in i:
        local2 = linha[local].index(b) # Local2 do b em i ( local )
        if "\n" in b:
            linha[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"

lista1, lista2 = linha
print("linha1 =",lista1)
print("linha2 =",lista2)


#soma=lista1+lista1
#print(soma)

