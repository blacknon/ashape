import copy


# @brief:
#    配列から再帰的に位置情報の文字を抽出する関数
def get_string_recursion(num, string_array):
    array = copy.deepcopy(string_array)
    i = 1
    while 1:
        if len(array) * i - 1 <= num:
            array.extend(string_array)
            continue
        else:
            break
        i += 1

    return array[num]
