print("Данная программа имеет информацию по притяжению тел таких как:")
print("1. Солнце")
print("2. Меркурий")
print("3. Венера")
print("4. Луна")
print("5. Марс")
print("6. Юпитер")
print("7. Сатурн")
print("8. Уран")
print("9. Нептун")
print("10. Плутон")
print("Введите номер желаемой планеты")
G1=11
G=6.6743
m11=24
m1=5.976
m21=21
check=int(input())
R3=18
x=1
if check==1: 
    m2=1989100000
    R1=150
elif check==2:
    m2=330.2
    R1=92
elif check==3:
    m2=4868.5
    R1=42
elif check==4:
    m2=73.5
    R1=384467*1000
    R3=0
elif check==5:
    m2=641.85
    R1=79
elif check==6:
    m2=1898600
    R1=628
elif check==7:
    m2=568460
    R1=1278
elif check==8:
    m2=86832
    R1=4348
elif check==9:
    m2=102430
    R1=2721
elif check==10:
    m2=12.105
    R1=6239
else:
    print("Введён неправильный номер")
    x=2
R2=R1**2
count=0
if x!=2:
    F1=G*m1*m2/R2
    while x!=0:
        if F1*10>=1:
            x=0
        count+=1    
        F1=F1*10
    F2=m11+m21-G1-R3-count
    F2=10**F2
    F=round(F1,5)*F2
    print("У данной планеты данное притяжение с Землей:")
    print(F, "(данное значение округленно до 5 знаков после запятой)")
    




