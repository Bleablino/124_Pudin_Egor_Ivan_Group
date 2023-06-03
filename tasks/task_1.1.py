Tom = int(input("Скорость Тома:"))
Jerry = int(input("Скорость Джерри:"))
Path = int(input("Расстояние между ними:"))
if Tom<Jerry:
    print("Джерри убежал от Тома")
else:
    Speed = int(Tom-Jerry)
    Time = int(Path//Speed)
    if Path%Speed!=0:
        Time+=1
    print("Том догонит Джерри через " , Time , " секунд")