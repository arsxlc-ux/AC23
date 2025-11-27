class TreeNode:
    def __init__(self, v):
        self.v = v
        self.l = self.r = None
def i(r, k):
    if r is None:
        return TreeNode(k)
    if k < r.v:
        r.l = i(r.l, k)
    else:
        r.r = i(r.r, k)
    return r
def h(n):
    return 0 if n is None else max(h(n.l), h(n.r)) + 1
def b(n):
    if n is None:
        return True
    lh, rh = h(n.l), h(n.r)
    return abs(lh-rh)<=1 and b(n.l) and b(n.r)
nums = [7, 3, 2, 1, 9, 5, 4, 6, 8]
r = None
for x in nums:
    r = i(r, x)
print('YES' if b(r) else 'NO')
