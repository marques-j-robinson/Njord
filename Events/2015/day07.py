from util import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        self.split_by_new_line()

    def part_01(self):
        wires = init(self.data)
        for w in wires:
            data = wires[w]
            print(data)
            is_gate = data.get('isGate')
            if is_gate is True:
                val = data['val']
                a = val[0]
                b = val[len(val)-1]
                ready = False
                if wires[a]['isGate'] is False and wires[b]['isGate'] is False:
                    ready = True
                print(a)
                print(b)
            else:


    def part_02(self):
        pass


def init(data):
    wires = {}
    for i in data:
        [a, b] = i.split(' -> ')
        is_gate = False

        for g in GATES.keys():
            if g in a:
                is_gate = True

        wires[b] = {
                        "isGate": is_gate,
                        "val": a,
                    }
    return wires


GATES = {
            "AND":      lambda a, b: a&b,
            "OR":       lambda a, b: a|b,
            "NOT":      lambda a: bit_not(a),
            "LSHIFT":   lambda a, b: a << b,
            "RSHIFT":   lambda a, b: a >> b
        }


def bit_not(n, numbits=16):
    return (1 << numbits) - 1 - n
