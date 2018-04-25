import re


class TextSplitter:

    team_caption = 'Фіксики'

    ABBRS = """
    н.е.
    грн.
    опубл.
    включ.
    рр.
    к.
    стор.
    стр.
    ім.
    о.
    вул.
    просп.
    бул.
    пров.
    пл.
    г.
    р.
    див.
    п.
    с.
    м.
    """.strip().split()

    def split(self, text: str) -> list:

        spans = []
        for match in re.finditer('[^\s]+', text):
            spans.append(match)

        spans_count = len(spans)

        rez = []
        off = 0
        offs = list()
        f = open('file.txt', 'a')
        for i in range(spans_count):
            tok = text[spans[i].start():spans[i].end()]

            f.write('TOK "' + tok + '" ')

            if i == spans_count - 1:
                rez.append(text[off:spans[i].end()])
            elif tok[-1] in ['.', '!', '?', '…', '»']:
                tok1 = tok[re.search('[.!?…»]', tok).start() - 1]
                next_tok = text[spans[i + 1].start():spans[i + 1].end()]
                f.write('NEXT_TOK "' + next_tok + '"\n\n')
                if (next_tok[0].isupper()
                        and not tok1.isupper()
                        and not re.match(r'\d+?\.', tok)
                        and not (tok.endswith(').') and next_tok[0].isupper())
                        or (re.match(r'[А-ЯЮІЇЄа-яюіїє]+?\.', tok) and re.match(r'\d+?\.', next_tok))
                        or (re.match(r'(\d\.\d-\d\.\d\.|\d+?/\d+?\.)', tok) and re.match(r'\d+?\.', next_tok))
                        and not (tok1[0] == '('    # tok[-1] != '.'
                                 or tok in self.ABBRS)):
                    rez.append(text[off:spans[i].end()])
                    off = spans[i + 1].start()
                    offs.append(off)
        f.close()

        return offs
