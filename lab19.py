n, k = [int(v) for v in input().split()]
tree = [[int(v) for v in input().split()] for _ in range(n)]


def make_chain(chain, pos, found):
    if found:
        chain.add(pos)

    found = found or pos == k

    for j, c in enumerate(tree[pos]):
        if c == 1:
            chain |= make_chain(chain, j, found)

    return chain


chain = make_chain(set([]), 0, False)
chain = list(chain)
chain.sort()
chain = [str(k)] + list(map(str, chain))
print(' '.join(chain))
