

def overlay_texts(text_file_list):
    result = []

    # 各ファイルを読み込んで、resultに上書きしていく
    for text_file in text_file_list:
        overlay_contents = text_file.read().splitlines()
        result = join_overlay_text(result, overlay_contents)

    print("\n".join(result))


def join_overlay_text(before_text, overlay_text):
    max_line = max(len(before_text), len(overlay_text))

    result = []
    for i in range(max_line):
        if len(before_text) <= i:
            before_text.append("")
        elif len(overlay_text) <= i:
            overlay_text.append("")

        line = join_overlay_line(before_text[i], overlay_text[i])
        result.append(line)

    return result


def join_overlay_line(before_line, overlay_line):
    before_line_array = list(before_line)
    overlay_line_array = list(overlay_line)

    line_length = max(len(before_line_array), len(overlay_line_array))

    result = []
    for i in range(line_length):
        if len(before_line_array) <= i:
            before_line_array.append(" ")
        elif len(overlay_line_array) <= i:
            overlay_line_array.append(" ")

        if before_line_array[i] == ' ' and overlay_line_array[i] != ' ':
            result.append(overlay_line_array[i])
        elif overlay_line_array[i] in ' 　' and before_line_array[i] not in ' 　':
            result.append(before_line_array[i])
        else:
            result.append(overlay_line_array[i])
    return ''.join(result)
