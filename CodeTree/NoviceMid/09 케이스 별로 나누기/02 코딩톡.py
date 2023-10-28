n, m, p = tuple(map(int, input().split()))
info = [
    input().split()
    for _ in range(m)
]
people = [
    chr(i + 65)
    for i in range(n)
]

if info[p - 1][1] == '0':
    people = []
    print()

else:
    for person in people:
        read = False
        for cur, num in info:
            num = int(num)
            if num >= int(info[p - 1][1]) and cur == person:
                read = True

        if read == False:
            print(person, end=' ')
