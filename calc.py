print('Калькулятор (Чтобы выключить калькулятор введите "выход")')
run = True
while run:
    run1 = True
    run2 = True
    run3 = True
    res = 0
    while run1:
        n1 = input("Первое число: ").strip()
        if n1.lower() == "выход":
            run = False
            run1 = False
            run2 = False
            run3 = False
            break
        if not n1:
            print("Введите корректное число!")
            continue
        ok1 = True
        minus1 = False
        dot1 = False
        for i, ch in enumerate(n1):
            if ch.isdigit():
                continue
            elif ch == "-" and i == 0:
                if minus1:  # Проверка повторяемости минуса
                    ok1 = False
                    break
                minus1 = True
                continue
            elif ch in ".,":
                if dot1:  # Проверка повторяемости точки/запятой
                    ok1 = False
                    break
                dot1 = True
                continue
            else:
                ok1 = False
                break
        if not ok1:
            print("Введите корректное число!")
            continue
        num1 = float(n1.replace(",", "."))
        run1 = False
    while run2:
        n2 = input("Второе число: ").strip()
        if n2.lower() == "выход":
            run = False
            run1 = False
            run2 = False
            run3 = False
            break
        if not n2:
            print("Введите корректное число!")
            continue
        ok2 = True
        minus2 = False
        dot2 = False
        for i, ch in enumerate(n2):
            if ch.isdigit():
                continue
            elif ch == "-" and i == 0:
                if minus2:
                    ok2 = False
                    break
                minus2 = True
                continue
            elif ch in ".,":
                if dot2:
                    ok2 = False
                    break
                dot2 = True
                continue
            else:
                ok2 = False
                break
        if not ok2:
            print("Введите корректное число!")
            continue
        num2 = float(n2.replace(",", "."))
        run2 = False
        run3 = True
    while run3:
        op = input("Операция: ").strip()
        if op.lower() == "выход":
            run = False
            run1 = False
            run2 = False
            run3 = False
            break
        ok3 = len(op) == 1
        for ch in op:
            if ch not in "+-/*":
                ok3 = False
                break
        if not ok3:
            print("Операции: + - * /")
            continue
        if op == "+":
            res = float(num1) + float(num2)
            print("Итого:", res)
            print("-------------------")
            run3 = False
        elif op == "-":
            res = float(num1) - float(num2)
            print("Итого:", res)
            print("-------------------")
            run3 = False
        elif op == "*":
            res = float(num1) * float(num2)
            print("Итого:", res)
            print("-------------------")
            run3 = False
        else:
            if num1 == 0 or num2 == 0:
                print("На 0 делить нельзя")
                run1 = True
                run2 = True
                run3 = False
                continue
            else:
                print(num1)
                print(num2)
                res = float(num1) / float(num2)
                print("Итого:", res)
                run3 = False
# Проверка связи для теста репы