from random import *
Length = randint(50,100)
Lengther = randint(50,100)
List = []
Lister = []
for num in range(Lengther):
    Lister.append(randint(1,9999))
for number in range (Length):
    List.append(randint(1,9999))
Lisimmular = []
for numi in range(Length):
    count=list[numi]
    if Lister.count(List[numi])>0:
        continue
    else:
        Lisimmular.append(count)
print(Lisimmular)