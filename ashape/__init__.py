import argparse
from signal import signal, SIGPIPE, SIG_DFL

from . import overlay, spiral, square

__version__ = "0.1.0"


def main():
    # global変数の__version__を使用するための宣言
    global __version__

    # Broken Pipe errorを出力させないための記述
    signal(SIGPIPE, SIG_DFL)

    # @brief:
    #    spiralサブコマンドの処理
    def scmd_spiral(args):
        sp = spiral.Spiral()
        sp.new(args)

        # 螺旋状の数字配列を取得
        x_size, y_size = sp.get_spiral_size()
        sp.get_spiral_num_array(x_size, y_size)

        # 文字列を螺旋状にして出力
        sp.print_spiral_array()

    # @brief:
    #    squareサブコマンドの処理
    def scmd_square(args):
        sq = square.Square()
        sq.new(args)

        # 各辺の長さからサイズを取得して数字配列を生成する
        x_size, y_size = sq.get_square_size()
        sq.get_square_num_array(x_size, y_size)

        # 文字列を各辺の枠とした四角形を出力
        sq.print_square_array()

    # @brief:
    #    overlayサブコマンドの処理
    def scmd_overlay(args):
        overlay.overlay_texts(args.text)

    # @brief:
    #    helpサブコマンドの処理
    def scmd_help(args):
        print(parser.parse_args([args.command, '--help']))

    # コマンドラインパーサーを作成
    parser = argparse.ArgumentParser(
        description='Making ascii shapes from strings.'
    )
    subparsers = parser.add_subparsers()

    # spiralサブコマンドのparser
    p_spiral = subparsers.add_parser(
        'spiral', aliases=['sp'],
        help='Create ascii spiral from strings. see `spiral -h`.'
    )
    p_spiral.add_argument('string', nargs='?', type=str,
                          help="use strings")
    p_spiral.add_argument('-e', '--empty-char', type=str,
                          dest="empty_char",
                          help="use empty character")
    p_spiral.add_argument('-d', '--delimiter', type=str,
                          dest="delimiter", default=" ",
                          help="use delimiter")
    p_spiral.add_argument('-r', '--reverse', dest="reverse",
                          action='store_true', default=False,
                          help="string reverse flag")
    p_spiral.add_argument('-R', '--recursion', dest="recursion",
                          action='store_true', default=False,
                          help="string recursion flag")
    p_spiral.add_argument('-W', '--width', type=int, default=0,
                          help="width size(char)")
    p_spiral.add_argument('-H', '--height', type=int, default=0,
                          help="height size(line)")
    p_spiral.set_defaults(handler=scmd_spiral)

    # squareサブコマンドのparser
    p_square = subparsers.add_parser(
        'square', aliases=['sq'],
        help='Create ascii square from strings. see `square -h`.'
    )
    p_square.add_argument('string', nargs='?', type=str,
                          help="use strings")
    p_square.add_argument('-e', '--empty-char', type=str,
                          dest="empty_char",
                          help="use empty character")
    p_square.add_argument('-i', '--square-in-char', type=str,
                          dest="square_in_char", default="　",
                          help="square in charcter")
    p_square.add_argument('-d', '--delimiter', type=str,
                          dest="delimiter", default="",
                          help="use delimiter")
    p_square.add_argument('-r', '--reverse', dest="reverse",
                          action='store_true', default=False,
                          help="string reverse flag")
    p_square.add_argument('-R', '--recursion', dest="recursion",
                          action='store_true', default=False,
                          help="string recursion flag")
    p_square.add_argument('-W', '--width', type=int, default=0,
                          help="width size(char)")
    p_square.add_argument('-H', '--height', type=int, default=0,
                          help="height size(line)")
    p_square.set_defaults(handler=scmd_square)

    # overlayサブコマンドのparser
    p_overlay = subparsers.add_parser(
        'overlay', aliases=['o'],
        help='Overlay text. see `overlay -h`.'
    )
    p_overlay.add_argument('text', nargs='+', type=argparse.FileType('r'),
                           help="overlay text data")
    p_overlay.set_defaults(handler=scmd_overlay)

    # crossサブコマンドのparser

    # triangleサブコマンドのparser

    # diamondサブコマンドのparser

    # help コマンドの parser を作成
    parser_help = subparsers.add_parser(
        'help', help='see `help -h`')
    parser_help.add_argument(
        'command', help='command name which help is shown')
    parser_help.set_defaults(handler=scmd_help)

    # --version(-v)オプションのparser定義
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__)
    )

    # コマンドライン引数をパースして対応するハンドラ関数を実行
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        # 未知のサブコマンドの場合はヘルプを表示
        parser.print_help()
