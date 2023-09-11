class Node:
    def __init__(self, name):
        self.up = None
        self.name = name
        self.money = 0


def go(name, tree, gain):
    if gain == 0 or name not in tree:
        return
    
    temp = int(gain / 10)
    gain -= temp
    tree[name].money += gain
    go(tree[name].up, tree, temp)
    

def solution(enroll, referral, seller, amount):
    tree = dict()

    for e, r in  zip(enroll, referral):
        tree[e] = Node(e)
        tree[e].up = r

    for s, a in zip(seller, amount):
        go(s, tree, a * 100)

    return [tree[n].money for n in enroll]