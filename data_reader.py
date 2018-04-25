# SentenceDataSet:
#    txt-file with data rows
#    row structure: <text-type>\t<sentence-count>\t<sep-pos-1>\t...\t<sep-pos-n>\t<text>
#    sep-pos -- separator position: index of first symbol next sentence

# SentenceDataSetReader:
#    read data from txt-file and return:
#       data: list of texts
#       target: list of separator positions


class DataReader:

    def __init__(self):
        self.encoding = 'utf-8'

    def read_data_target(self, data_filename: str) -> list:
        data, target = list(), list()
        with open(data_filename, 'r', encoding=self.encoding, errors='ignore') as f:
            rows = [line.split('\t') for line in f.read().split('\n\n') if line.count('\t')>3]
            for row in rows:
                text_type = int(row[0])
                sent_count = int(row[1])
                s_poses = [int(x) for x in row[2:2+sent_count]]
                text = row[-1]
                data.append(text)
                target.append(s_poses)

        return data, target

if __name__ == '__main__':
    SENTENCE_DATA_SET_FILENAME = '/resource/snt_data.dat'

    data_reader = DataReader()
    data, target = data_reader.read_data_target(SENTENCE_DATA_SET_FILENAME)

    for i, text in enumerate(data):
        print('Text: {0}'.format(text))
        print('Sentence count: {0}'.format(len(target[i])))
        print('Separator positions: {0}'.format(target[i]))
        print('Sentences: ')
        if len(target[i]) > 1:
            print('\t1). {0}'.format(text[:target[i][0]]))
        else:
            print('\t1). {0}'.format(text))
        for j, pos in enumerate(target[i]):
            if j+1!= len(target[i]):
                print('\t{0}). {1}'.format(j+2, text[pos:target[i][j+1]]))
        print()

