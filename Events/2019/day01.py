from util import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        self.data = [int(x) for x in self.data.split()]

    def part_01(self):
        for m in self.data:
            self.p1 += calc_fuel(m)

    def part_02(self):
        for m in self.data:
            self.p2 += re_calc_fuel(m)


def calc_fuel(mass):
    return round(mass//3)-2

def re_calc_fuel(mass, total=0):
    fuel = calc_fuel(mass)
    if fuel <= 0:
        return total
    else:
        total += fuel
        return re_calc_fuel(fuel, total)
