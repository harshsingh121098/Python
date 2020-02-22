while True:
    try:
        num=int(input("enter the number\n"))
        print(100/num)
        break
    except ValueError:
        print("do it again")
        break
    except ZeroDivisionError:
        print("No zero plz")
        break
    finally:
        print("loop complete")