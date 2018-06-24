n, k = map(int, input().split())
tree = [input().split() for _ in range(n)]


def make_chain(c, pos):
    if pos != k:
        c.add(pos)
    for j, e in enumerate(tree[pos]):
        if e == '1':
            c |= make_chain(c, j)
    return c


chain = list(make_chain(set([]), k))
chain.sort()
print(' '.join(map(str, [k] + chain)))
