from text_splitter import TextSplitter
from data_reader import DataReader


class AccuracyCalculator:

    def __init__(self):
        self.data_reader = DataReader()

    def get_accuracy(self, text_splitter: TextSplitter, data_filename: str) -> list:
        data, target = self.data_reader.read_data_target(data_filename)
        predicted = [text_splitter.split(text) for text in data]
        snt_accuracy = sum([1 if len(predicted[i]) == len(target[i]) else 0 for i in range(len(predicted))])/len(predicted)
        sep_accuracy = self.__get_sep_pos_accuracy(predicted, target)
        return snt_accuracy, sep_accuracy

    def __get_sep_pos_accuracy(self, predicted, target) -> float:
        true_count = all_count = 0
        for i in range(len(predicted)):
            true_count += len(set(predicted[i]).intersection(set(target[i])))
            all_count += len(target[i])
        return true_count/all_count

if __name__ == '__main__':
    DATA_FILENAME = '/resource/snt_data.dat'

    from main import DefaultSplitter
    default_splitter = DefaultSplitter()

    accuracy_calculator = AccuracyCalculator()
    snt_accuracy, sep_accuracy = accuracy_calculator.get_accuracy(default_splitter, DATA_FILENAME)
    print('Accuracy: {0:3.4}%, {1:3.4}%'.format(100*snt_accuracy, 100*sep_accuracy))