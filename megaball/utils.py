import math

import pyxel


def angle_reflect(incidence_angle, surface_angle):
    angle = surface_angle * 2 - incidence_angle
    return (angle + 360) % 360


def sign_triangle(point_1, point_2, point_3):
    return (point_1[0] - point_3[0]) * (point_2[1] - point_3[1]) - (point_2[0] - point_3[0]) * (point_1[1] - point_3[1])


def is_point_in_triangle(px, py, ax, ay, bx, by, cx, cy):
    # print("Checking point [{a},{b}] in tri [{c}][{d}], [{e}][{f}], [{g}][{h}] ({i})".format(
    #    a=px, b=py, c=ax, d=ay, e=bx, f=by, g=cx, h=cy, i=pyxel.frame_count
    # ))
    sign_ab = sign_triangle([px, py], [ax, ay], [bx, by])
    sign_bc = sign_triangle([px, py], [bx, by], [cx, cy])
    sign_ca = sign_triangle([px, py], [cx, cy], [ax, ay])

    has_neg = (sign_ab < 0) or (sign_bc < 0) or (sign_ca < 0)
    has_pos = (sign_ab > 0) or (sign_bc > 0) or (sign_ca > 0)

    # print("return: " + str(not(has_neg and has_pos)))

    return not (has_neg and has_pos)


def circle_rect_overlap(circle_x, circle_y, circle_radius, rect_x, rect_y, rect_width, rect_height):
    closest_x = circle_x
    closest_y = circle_y

    if circle_x < rect_x:
        closest_x = rect_x
    elif circle_x > rect_x + rect_width:
        closest_x = rect_x + rect_width

    if circle_y < rect_y:
        closest_y = rect_y
    elif circle_y > rect_y + rect_height:
        closest_y = rect_y + rect_height

    closest_x = closest_x - circle_x
    closest_x *= closest_x
    closest_y = closest_y - circle_y
    closest_y *= closest_y

    return closest_x + closest_y < circle_radius * circle_radius


def get_angle_deg(x1, y1, x2, y2):
    degs = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return (degs + 360) % 360


def get_tile_x(index):
    return index[0] * 8  # math.floor(index % 32) * 8


def get_tile_y(index):
    return index[1] * 8  # math.floor(index / 32) * 8


def get_tile_index(x, y):
    return (x // 8, y // 8)  # x/8 + (y / 8) * 32


def lerp(value_range, delta):
    # print("delta: " + str(delta) + ", value_range: " + str(value_range[0]) + "," + str(value_range[1]))
    # print()
    return (value_range[0] * (1.0 - delta)) + (value_range[1] * delta)


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
