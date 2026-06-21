import math

import pyxel


def angle_reflect(incidence_angle, surface_angle):
    angle = surface_angle * 2 - incidence_angle
    return (angle + 360) % 360


def sign_triangle(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def is_point_in_triangle(px, py, ax, ay, bx, by, cx, cy):
    # print("Checking point [{a},{b}] in tri [{c}][{d}], [{e}][{f}], [{g}][{h}] ({i})".format(
    #    a=px, b=py, c=ax, d=ay, e=bx, f=by, g=cx, h=cy, i=pyxel.frame_count
    # ))
    d1 = sign_triangle([px, py], [ax, ay], [bx, by])
    d2 = sign_triangle([px, py], [bx, by], [cx, cy])
    d3 = sign_triangle([px, py], [cx, cy], [ax, ay])

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    # print("return: " + str(not(has_neg and has_pos)))

    return not (has_neg and has_pos)


def circle_rect_overlap(cx, cy, cr, rx, ry, rw, rh):
    closest_x = cx
    closest_y = cy

    if cx < rx:
        closest_x = rx
    elif cx > rx + rw:
        closest_x = rx + rw

    if cy < ry:
        closest_y = ry
    elif cy > ry + rh:
        closest_y = ry + rh

    closest_x = closest_x - cx
    closest_x *= closest_x
    closest_y = closest_y - cy
    closest_y *= closest_y

    return closest_x + closest_y < cr * cr


def get_angle_deg(x1, y1, x2, y2):
    degs = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (degs + 360) % 360


def get_tile_x(index):
    return index[0] * 8  # math.floor(index % 32) * 8


def get_tile_y(index):
    return index[1] * 8  # math.floor(index / 32) * 8


def get_tile_index(x, y):
    return (x // 8, y // 8)  # x/8 + (y / 8) * 32


def lerp(v, d):
    # print("delta: " + str(d) + ", v: " + str(v[0]) + "," + str(v[1]))
    # print()
    return (v[0] * (1.0 - d)) + (v[1] * d)


def ease_out_expo(x):
    if x == 1:
        return 1

    return 1 - math.pow(2, -10 * x)


def ease_out_cubic(x):
    return 1 - math.pow(1 - x, 3)


def draw_number_shadowed(x, y, num, zeropad=0):
    strnum = str(num)
    if zeropad > 0:
        strnum = strnum.zfill(zeropad)

    for i in range(len(strnum)):
        pyxel.blt(x + i * 8, y, 0, 16 + int(strnum[i]) * 8, 56, 8, 8, 8)
