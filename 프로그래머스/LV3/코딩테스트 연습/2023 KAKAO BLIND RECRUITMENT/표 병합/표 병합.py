class Cell:
    def __init__(self, r, c):
        self.value = None
        self.loc = (r, c)
        self.group = {(r, c)}


    def reset(self):
        self.value = None
        self.group = {self.loc}


class ValueLocsInfo():
    def __init__(self):
        self.value_locs = dict()

    
    def sub(self, v, locs):
        if v in self.value_locs:
            self.value_locs[v] -= locs


    def add(self, v, locs):
        if v not in self.value_locs:
            self.value_locs[v] = set()
        self.value_locs[v] |= locs


    def delete(self, v):
        del self.value_locs[v]


    def is_in(self, v):
        return v in self.value_locs
    

    def get_locs(self, v):
        return self.value_locs[v]


class Table:
    def __init__(self):
        self.table = [[Cell(r, c) for c in range(51)] for r in range(51)]
        self.value_locs = ValueLocsInfo()


    def change_value(self, v, locs):
        for r, c in locs:
            self.table[r][c].value = v


    def update(self, args):
        if len(args) == 3:
            r, c, v = int(args[0]), int(args[1]), args[2]
            cell = self.table[r][c]
            if v == cell.value: return
            self.value_locs.sub(cell.value, cell.group)
            self.change_value(v, cell.group)
            self.value_locs.add(v, cell.group)
        else:
            v1, v2 = args
            if not self.value_locs.is_in(v1) or v1 == v2:
                return
            self.change_value(v2, self.value_locs.get_locs(v1))
            self.value_locs.add(v2, self.value_locs.get_locs(v1))
            self.value_locs.delete(v1)


    def merge(self, r1, c1, r2, c2):
        if (r1, c1) == (r2, c2):
            return

        cell1, cell2 = self.table[r1][c1], self.table[r2][c2]
        cells = (cell1.group | cell2.group)

        v1, v2 = cell1.value, cell2.value
        value = None

        if v1 != None and v2 != None:
            value = v1
            if v1 == v2: pass
            self.value_locs.sub(v2, cell2.group)
            self.value_locs.add(value, cell2.group)
        elif v1 != None and v2 == None:
            value = v1
            self.value_locs.add(value, cell2.group)
        elif v1 == None and v2 != None:
            value = v2
            self.value_locs.add(value, cell1.group)

        for r, c in cells:
            self.table[r][c].group = cells
            self.table[r][c].value = value   


    def unmerge(self, r, c):
        cell = self.table[r][c]
        v = cell.value
        self.value_locs.sub(v, cell.group)

        for _r, _c in cell.group:
            self.table[_r][_c].reset()

        if v != None:
            cell.value = v
            self.value_locs.add(v, cell.group)


    def print(self, r, c):
        return "EMPTY" if self.table[r][c].value == None else self.table[r][c].value


def solution(commands):
    answer = []
    table = Table()

    for command in commands:
        command = command.split(' ')
        if command[0] == "UPDATE":
            table.update(command[1:])
        elif command[0] == "MERGE":
            table.merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "UNMERGE":
            table.unmerge(int(command[1]), int(command[2]))
        elif command[0] == "PRINT":
            answer.append(table.print(int(command[1]), int(command[2])))

    return answer