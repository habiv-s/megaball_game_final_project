def overlap(x1, y1, r1, x2, y2, r2):
    dx = x1 - x2
    dy = y1 - y2
    dist = dx * dx + dy * dy
    radius_sum = r1 + r2
    return dist < radius_sum * radius_sum


def contains_other(x1, y1, r1, x2, y2, r2):
    radius_diff = r1 - r2
    if radius_diff < 0:
        return False

    dx = x1 - x2
    dy = y1 - y2
    dist = dx * dx + dy * dy
    radius_sum = r1 + r2
    return not (radiusDiff * radiusDiff < dist) and (dist < radius_sum * radius_sum)


def contains_point(x, y, radius, px, py):
    dx = x - px
    dy = y - py
    return dx * dx + dy * dy <= radius * radius


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
