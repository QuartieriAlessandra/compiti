dec = input("inserire numero decimale ")


res_list = []
risultato = dec

while True:
    res_list.append(risultato % 2)
    risultato = risultato / 2
    if risultato == 1:
        res_list.append(1)
        break

binary = ""
res_list.reverse()
for e in res_list:
    binary+=str(e)

a = bin(dec)[2:]

print("calcolo",binary)
print("funzione", a)
print()
print()

if binary == a :
    print("funziona")


