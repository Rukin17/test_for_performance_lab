import sys
import math


def calculate_point_position(circle_x, circle_y, radius, point_x, point_y):
    
    distance = math.sqrt((point_x - circle_x) ** 2 + (point_y - circle_y) ** 2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    with open(circle_file, 'r') as f:
        circle_x, circle_y = map(float, f.readline().split())
        radius = float(f.readline())

    with open(points_file, 'r') as f:
        for line in f:
            point_x, point_y = map(float, line.split())
            position = calculate_point_position(circle_x, circle_y, radius, point_x, point_y)
            print(position)


if __name__ == "__main__":
    main()