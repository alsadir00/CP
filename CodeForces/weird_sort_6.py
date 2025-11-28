
n = int(input())
for  i in range(n):
    a, p = map(int, input().split())
    nums = [int(x) for x in input().split()]
    idxs = [int(x) for x in input().split()]

    poss = [False] * (n+1)
    for i in idxs:
        poss[i] = True
    
    sorted_nums = sorted(nums)
    i = 1
    while i < n:
        if poss[i]:
            j = 1
            while j < n and poss[j]:
                j += 1
            seg = a[i-1:j]      
            seg.sort()
            a[i-1:j] = seg
            i = j
        else:
            i += 1
    if a == sorted_nums:
        print("YES")
    else:
        print("NO")

    