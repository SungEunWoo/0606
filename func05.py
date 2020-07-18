def calc_gugudan(dan):
    for i in range(1, 10):
        print(dan, "*", i, "=", dan*i)

d = int(input("단 : "))
if 1 <= d <= 9:
    calc_gugudan(d)
