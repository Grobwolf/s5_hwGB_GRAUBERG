# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('text2.txt', 'r') as f:
    text = f.read()


def compressing(file):
    compressed_text = ''
    prev_char = ''
    count = 1
    for char in file:
        if char != prev_char:
            if prev_char:
                compressed_text += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    print(compressed_text)
    return compressed_text


compressing(text)


with open('compressed_text2.txt', 'r') as data:
    text2 = data.read()


def decompressing(file: str):
    count = ''
    decompressed_text = ''
    for char in file:
        if char.isdigit():
            count += char
        else:
            decompressed_text += char * int(count)
            count = ''
    print(decompressed_text)
    return decompressed_text


decompressing(text2)
