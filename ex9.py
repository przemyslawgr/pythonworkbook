money = int(input("How much money did you deposit?"))
for i in range(3):
    money = money + 0.04 * money
    print(round(money,  2))