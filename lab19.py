n, k = map(int, input().split())
tree = [input().split() for _ in range(n)]


def make_chain(c, pos):
    if pos != k:
        c.add(pos)
    for j, e in enumerate(tree[pos]):
        if e == '1':
            c |= make_chain(c, j)
    return c


def sort(l):
    for i in range(1, len(l)):
        curr = l[i]

        j = i - 1
        while curr < l[j] and j >= 0:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = curr


chain = list(make_chain(set([]), k))
sort(chain)
print(' '.join(map(str, [k] + chain)))
