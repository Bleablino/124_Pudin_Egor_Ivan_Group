from random import *
Length = randint(50,100)
Lengther = randint(50,100)
List = []
for number in range (Length):
    List.append(randint(1,9999))
Lister = []
for num in range(Lengther):
    Lister.append(randint(1,9999))
for numi in range(Length):
    if Lister.count(List[numi])>0:
        continue
    else:
        print(List[numi])
# command "in" for finding numbers in list. fix the code
from random import *
Length = randint(50,100)
Lengther = randint(50,100)
List = []
for number in range (Length):
    List.append(randint(1,9999))
Lister = []
for num in range(Lengther):
    Lister.append(randint(1,9999))
for numi in range(Length):
    if Lister.count(List[numi])>0:
        continue
    else:
        continue
