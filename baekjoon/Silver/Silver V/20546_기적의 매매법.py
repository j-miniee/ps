money = int(input())
stock = list(map(int, input().split(' ')))

jun, sung = 0, 0
m1, m2 = money, money
s_money = 0

for i in range(0, 14):
    increase, decrease = True, True
    
    if i+3 < len(stock) :
        for j in range(i, i+2):
            if stock[j] <= stock[j+1]:
                decrease = False
            if stock[j] >= stock[j+1]:
                increase = False

        if decrease and m2 >= stock[i+3]:
            sung += m2 // stock[i+3]
            m2 = m2 % stock[i+3]

        if increase and m2 != money:
            s_money = m2 + stock[i+3]*sung
            break

if s_money == 0:
    s_money = m2 + stock[-1]*sung

for i in range(0, 14):
    if m1 >= stock[i]:
        jun += m1 // stock[i]
        m1 %= stock[i]
j_money = m1 + stock[-1]*jun

if s_money > j_money:
    print("TIMING")
elif s_money < j_money:
    print('BNP')
else:
    print('SAMESAME')