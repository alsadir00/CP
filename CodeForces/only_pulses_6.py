# A. Only Pluses
# time limit per test1 second
# memory limit per test256 megabytes
# Kmes has written three integers a, b and c in order to remember that he has to give Noobish_Monk a×b×c bananas.

# Noobish_Monk has found these integers and decided to do the following at most 5 times:

# pick one of these integers;
# increase it by 1.
# For example, if a=2, b=3 and c=4, then one can increase a three times by one and increase b two times. After that a=5, b=5, c=4. Then the total number of bananas will be 5×5×4=100.

# What is the maximum value of a×b×c Noobish_Monk can achieve with these operations?

# Input
# Each test contains multiple test cases. The first line of input contains a single integer t (1≤t≤1000) — the number of test cases. The description of the test cases follows.

# The first and only line of each test case contains three integers a, b and c (1≤a,b,c≤10) — Kmes's integers.

# Output
# For each test case, output a single integer — the maximum amount of bananas Noobish_Monk can get.


n = int(input())

for i in range(n):
    a,b,c = map(int, input().split())

    sm = min(a,b,c)
    mx = max(a,b,c)
    md = a + b + c - sm - mx

    for i in range(5):
        if sm <= md and sm <= mx:
            sm += 1
        elif md <= sm and md <= mx:
            md += 1
        else:
            mx += 1
    print(sm * md * mx)
# Alternative solution
n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    nums = [a, b, c]

    for _ in range(5):
        nums.sort()
        nums[0] += 1

    print(nums[0] * nums[1] * nums[2])


