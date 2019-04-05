gorengan=["bakwan","cireng","tahu"]

for g in gorengan:
    print(g)

bakwan = 'bakwan'

for i in bakwan:
    print(i)

buah = ["anggur","jeruk","apel"]
sayur = ["kangkung","wortel","kentang"]

belanja=[gorengan,buah,sayur]

for subBelanja in belanja:
    #print(subBelanja)
    for komponen in subBelanja:
        print(komponen)
