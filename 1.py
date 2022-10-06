# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Напишитеабв программуабв, всеабв словаабв, содержащиеабв ""абв"" всеабв слова, содержащие ""абв"""
symbols = "абв"

def get_text(file, text):
    with open(file, 'w') as f:
        f.write(text)
    with open(file, 'r') as f:
        tmp = str(f.readlines())
        print(tmp)


def filter_words_with_symbols(file, symbols):
    with open(file, 'r') as f:
        tmp = str(f.readlines())
    with open(file, 'w') as f:
        f.write(" ".join(filter(lambda x: symbols not in x, tmp.split())))
    with open(file, 'r') as f:
        tmp = str(f.readlines())
        print(tmp)


get_text("text.txt", text)
filter_words_with_symbols("text.txt", symbols)


