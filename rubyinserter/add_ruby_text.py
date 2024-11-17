import MeCab
from pykakasi import kakasi

tagger = MeCab.Tagger()
kks = kakasi()


def convert(text):
    return "".join([tmp['hira'] for tmp in kks.convert(text)])


def add_ruby(text):

    parsed_text = tagger.parse(text)

    # 結果を行ごとに分割
    lines = parsed_text.splitlines()

    replaced_text = []
    for line in lines:
        # 行が形態素解析の結果である場合のみ処理する
        if '\t' in line:
            parts = line.split('\t')

            if parts[1] == "":
                if convert(parts[3]) == parts[0]:
                    replaced_text.append(parts[0])
                else:
                    replaced_text.append(f"{parts[0]}[{convert(parts[3])}]")
            else:
                if (convert(parts[2]) == parts[0]) or (convert(parts[1]) == parts[0]):
                    replaced_text.append(parts[0])
                else:
                    replaced_text.append(f"{parts[0]}[{convert(parts[1])}]")

    return "".join(replaced_text)


def main():
    text = "石炭の積み込みがもう終わった。"
    print(add_ruby(text))


if __name__ == "__main__":
    main()
