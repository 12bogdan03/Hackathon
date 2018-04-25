from text_splitter import TextSplitter
import re


class DefaultSplitter(TextSplitter):

    def __init__(self):
        self.team_caption = 'Default'

    def split(self, text: str):
        match = re.finditer('\. ', text)
        predicted = [m.start()+2 for m in match]

        return predicted


if __name__ == '__main__':
    text = 'Я тут почуваю себе багатим, хоч нічого не маю. Бо поза всякими програмами й партіями — земля належить ' \
           'до мене. Вона моя. Всю її, велику, розкішну, створену вже, — всю я вміщаю в собі. Там я творю її наново, ' \
           'вдруге, — і тоді здається мені, що ще більше права маю на неї.'

    default_splitter = TextSplitter()
    s_poses = default_splitter.split(text)

    print(text)
    print()

    print('Sentences: ')
    if len(s_poses) > 1:
        print('1). {0}'.format(text[:s_poses[0]]))
    else:
        print('1). {0}'.format(text))
    for i, pos in enumerate(s_poses):
        if i+1 != len(s_poses):
            print('{0}). {1}'.format(i+2, text[pos:s_poses[i+1]]))
    print()

    from accuracy_calculator import AccuracyCalculator
    DATA_FILENAME = './resource/snt_data.dat'
    accuracy_calculator = AccuracyCalculator()
    snt_accuracy, sep_accuracy = accuracy_calculator.get_accuracy(default_splitter, DATA_FILENAME)
    print('Accuracy: {0:3.4}%, {1:3.4}%'.format(100*snt_accuracy, 100*sep_accuracy))
