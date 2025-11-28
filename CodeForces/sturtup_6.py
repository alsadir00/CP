n = int(input())
for i in range(n):
    n,k = map(int, input().split())
    d = {}
    for i in range(k):
        b,c = map(int, input().split())
        if b in d:
            d[b] += c
        else:
            d[b] = c
    c = []
    for i in d.keys():
        c.append(d[i])
    c.sort(reverse=True)
    print(sum(c[:n]))

