from collections import Counter


def main(infilename):
    with open(infilename, 'r') as infile:
        #locations = [[int(x) for x in line.strip().split(',')] for line in infile]
        locations = [Coord.from_line(line, idx) for idx, line in enumerate(infile)]
    xmin = min(c.x for c in locations)
    xmax = max(c.x for c in locations)
    ymin = min(c.y for c in locations)
    ymax = max(c.y for c in locations)
    plane = {x: {y: Coord.from_locations(x, y, locations) for y in range(ymin, ymax+1)} for x in range(xmin, xmax+1)}

    # part 1
    assignments = Counter([plane[x][y].closest for x in plane for y in plane[x]])
    infinites = {plane[x][y].closest for x in plane for y in plane[x] if plane[x][y].is_edge(xmin, xmax, ymin, ymax)}
    for cid in infinites:
        assignments.pop(cid)
    print('furthest:', max(assignments.values()))

    # part 2
    dist_thresh = 10000
    region_size = sum(1 for x in plane for y in plane[x] if plane[x][y].total_dist < dist_thresh)
    print('region_size:', region_size)


class Coord:
    def __init__(self, x, y, id = None, closest = None, total_dist = None):
        self.id = id
        self.x = x
        self.y = y
        self.closest = closest
        self.total_dist = total_dist

    @classmethod
    def from_line(cls, line, idx):
        x, y = line.strip().split(',')
        return cls(int(x), int(y), id = idx, closest = idx)

    @classmethod
    def from_locations(cls, x, y, locations):
        me = cls(x, y)
        dists = me.distances(locations)
        me.closest = me.find_closest(dists)
        me.total_dist = me.find_total_dist(dists)
        return me

    def __repr__(self):
        return f"Coord({self.id}:[{self.x},{self.y}])"

    def l1_dist(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)

    def distances(self, locations):
        return {loc.id: self.l1_dist(loc) for loc in locations}

    def find_closest(self, distances, tie = '.'):
        smallest_dist = min(distances.values())
        nearest = {k for k in distances.keys() if distances[k] == smallest_dist}
        return tie if len(nearest) > 1 else nearest.pop()

    def find_total_dist(self, distances):
        return sum(distances.values())

    def is_edge(self, xmin, xmax, ymin, ymax):
        return self.x == xmin or self.x == xmax or self.y == ymin or self.y == ymax


if __name__ == "__main__":
    main('input.txt')