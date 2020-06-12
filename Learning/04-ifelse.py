while True :
    a = int(input("请输入一个数："))
    if a < 10 :
        print("a < 10")
    elif a >= 10 and a < 100 :
        print("a >= 10 and a < 100")
    elif a >= 100 and a < 1000 :
        print("a >= 100 and a < 1000")
    else :
        print("a >= 1000")

