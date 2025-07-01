n, m = map(int, input().split())

pokemon = {}
for i in range(1, n+1):
    name = input()
    pokemon[name] = i
    
pokemon_swap = {v:k for k,v in pokemon.items()}

find = [input() for _ in range(m)]

for f in find:
    if f.isdigit():
        print(pokemon_swap[int(f)])
    else:
        print(pokemon[f])
