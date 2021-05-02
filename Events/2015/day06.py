from util import BaseSolution


class Solution(BaseSolution):

    def translate(self):
        self.data = [l.strip() for l in self.data]

    def part_01(self):
        G = Grid(1000)

    def part_02(self):
        pass


class Light:

    def __init__(self):
        self.on = False
        self.brightness = 0

    def britten(self, i):
        self.brightness += i
        if self.brightness < 0:
            self.brightness = 0

    def toggle(self):
        self.on = not self.on

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False


class Grid:

    def __init__(self, size):
        self.elements = []
        self.size = size
        self.setup()

    def setup(self):
        for idx, _ in enumerate(range(self.size)):
            self.elements.append([])
            for _ in range(self.size):
                self.elements[idx].append(Light())


def parse_instruction(line):
    re_res = re.match(r"^(\D*) (\d*,\d*) \D* (\d*,\d*)", line.strip())
    task = re_res.group(1).strip()
    [start_x, start_y] = [int(i) for i in re_res.group(2).split(",")]
    [end_x, end_y] = [int(i) for i in re_res.group(3).split(",")]
    return {
        "task": task,
        "start": (start_x, start_y),
        "end": (end_x, end_y),
    }


G = Grid(1000)
lines = [l.strip() for l in fileinput.input()]
for line in lines:
    res = parse_instruction(line)
    start_x, start_y = res["start"]
    end_x, end_y = res["end"]
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            light = G.elements[y][x]
            if res["task"] == "toggle":
                light.toggle()
                light.britten(2)
            elif res["task"] == "turn on":
                light.turnOn()
                light.britten(1)
            elif res["task"] == "turn off":
                light.turnOff()
                light.britten(-1)

for rows in G.elements:
    for light in rows:
        if light.on is True:
            p1 += 1
        p2 += light.brightness
