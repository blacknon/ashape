#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


# @brief:
#    文字列の配列を受け取り、正方形とした場合の辺のサイズを返す関数
def get_string_size(str_list):
    i = 1
    while 1:
        if i**2 >= len(str_list):
            break
        i = i + 1
    return i


# @brief:
#    文字列を螺旋状に出力する関数
def print_spiral_array(num_array, string_array):
    # num_arrayの行列転置を行う
    num_array = list(map(list, zip(*num_array)))
    n = len(num_array)

    result = []
    for x in range(n):
        line = []
        for y in range(len(num_array[x])):
            num = num_array[x][y]

            if num < len(string_array):
                str = string_array[num]
            else:
                str = "　"

            line.append(str)
        line = " ".join(line)
        result.append(line)

    print("\n".join(result))


# @brief:
#    文字列を螺旋状に出力するための数字配列を生成する関数
def get_num_spiral_array(max_x, max_y):
    myarray = [[None] * max_y for j in range(max_x)]

    dx, dy = 1, 0
    x, y = 0, 0

    m = 0
    for i in range(max_x * max_y):
        myarray[x][y] = m
        nx, ny = x + dx, y + dy

        if 0 <= nx < max_x and 0 <= ny < max_y and myarray[nx][ny] is None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy

        m += 1
    return myarray


stdin_str = sys.stdin.readline().strip()
stdin_str_list = list(stdin_str)

str_size = get_string_size(stdin_str_list)
print(print_spiral_array(get_num_spiral_array(str_size, str_size), stdin_str_list))
