def go(tower, wires, visit, first_wire):
    if tower in visit:
        return
    visit.add(tower)

    for wire in wires:
        if wire == first_wire:
            continue
        if tower in wire:
            next = wire[0] if wire.index(tower) == 1 else wire[1]
            go(next, wires, visit, first_wire)

def solution(n, wires):
    ans = 101

    for wire in wires:
        left, right = set(), set()
        go(wire[0], wires, left, wire)
        go(wire[1], wires, right, wire)
        ans = min(ans, abs(len(left)-len(right)))
    return ans