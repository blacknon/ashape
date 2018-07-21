import unicodedata

from . import common


class Spiral():

    # @brief:
    #    argsの内容を元に処理に必要となる値を求め、self関数として保持させる
    def new(self, args):
        # 文字列を配列化する
        self.string_array = list(args.string)

        # argsからself変数へ取り込み
        self.delimiter = args.delimiter
        self.reverse = args.reverse
        self.recursion = args.recursion
        self.width = args.width
        self.height = args.height

        # キャラクタに全角文字が含まれている場合、空文字に使うスペースを全角にする
        self.empty_value = " "
        for char in self.string_array:
            char_type = unicodedata.east_asian_width(char)
            if char_type in 'FWA':
                self.empty_value = "　"

        # オプションで空文字(empty_char)を指定されている場合は、上書きをする
        if args.empty_char is not None:
            self.empty_value = args.empty_char[0]

    # @brief:
    #    文字列の配列を受け取り、正方形とした場合の辺のサイズを返す関数
    # @return:
    #    width, height
    def get_spiral_size(self):
        # 初期値を定義
        x = 0
        y = 0

        # self関数より値を取得する
        if self.width != 0:
            x = self.width
        if self.height != 0:
            y = self.height

        str_list = self.string_array
        # オプションの指定パターンに応じて処理を切り替える
        # width,heightの指定が無い場合
        if x == y == 0:
            i = 1
            while 1:
                if i**2 >= len(str_list):
                    break
                i = i + 1
            return i, i
        # width,heightどちらかが指定されている場合
        elif (x > 0 and y == 0) or (x == 0 and y > 0):
            if x > 0:
                set_value = x
            else:
                set_value = y

            i = 1
            while 1:
                if set_value * i >= len(str_list):
                    break
                i += 1

            if x > 0:
                return x, i
            else:
                return i, y
        # width,heightどちらも指定されている場合
        else:
            return x, y

    # @brief:
    #    文字列を螺旋状に出力するための数字配列を生成する関数
    def get_spiral_num_array(self, max_x, max_y):
        myarray = [[None] * max_y for j in range(max_x)]

        dx, dy = 1, 0
        x, y = 0, 0

        # 出力範囲の数字リストを作成する
        num_range = range(max_x * max_y)

        # reverseフラグが有効の場合、リストを逆順にする
        if self.reverse:
            num_range = list(reversed(num_range))

        for m in num_range:
            myarray[x][y] = m
            nx, ny = x + dx, y + dy

            if 0 <= nx < max_x and 0 <= ny < max_y and myarray[nx][ny] is None:
                x, y = nx, ny
            else:
                dx, dy = -dy, dx
                x, y = x + dx, y + dy

        self.num_array = myarray

    # @brief:
    #    文字列を螺旋状に出力する関数
    def print_spiral_array(self):
        num_array = self.num_array
        string_array = self.string_array

        result = []

        # num_arrayの行列転置を行う
        num_array = list(map(list, zip(*num_array)))

        n = len(num_array)
        x_range = range(n)

        for x in x_range:
            line = []
            for y in range(len(num_array[x])):
                num = num_array[x][y]

                # 範囲外の場合、空文字を代入しておく
                if num < len(string_array):
                    str = string_array[num]
                elif self.recursion:
                    str = common.get_string_recursion(num, string_array)
                else:
                    str = self.empty_value

                line.append(str)

            delimiter = self.delimiter
            line = delimiter.join(line)
            result.append(line)

        print("\n".join(result))
