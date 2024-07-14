from translate import Translator
translator = Translator(to_lang="zh")

with open("translate_from.txt",mode="r") as translate_from:
    for _ in range(0,4):
        line_to_translate = translate_from.readline()
        translation = translator.translate(line_to_translate)
        print(translation)