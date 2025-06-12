n  = int(input())

for _ in range(n):
    ps = input()
    cnt = 0
    vpn = True

    for p in ps:
        if p == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            vpn = False
            break

    if cnt != 0:
        vpn = False

    print('Yes' if vpn else 'No' )