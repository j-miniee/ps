n, m = map(int, input().split())

word_dict = {}

for _ in range(n):
    word = input() 
    if len(word) >= m:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1 # 리스트.count() 쓰지말고!

word_dict = dict(sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

for k, v in word_dict.items():
    print(k)
