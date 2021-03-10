import sys


class ProximityQuery:

    def __init__(self, index, word1, word2, k):
        self.index = index
        self.word_1 = word1
        self.word_2 = word2
        self.k = k

    def query(self):
        try:
            index_word_1 = self.index[self.word_1][1]
        except KeyError:
            print("ERROR: word '{}' not found in dictionary!".format(self.word_1))
            sys.exit(1)
        try:
            index_word_2 = self.index[self.word_2][1]
        except KeyError:
            print("ERROR: word '{}' not found in dictionary!".format(self.word_2))
            sys.exit(1)
        intersection = list(index_word_1.keys() & index_word_2.keys())
        if not intersection:
            print("ERROR: words '{}' and '{}' do not occur together in any document!".format(self.word_1, self.word_2))
            sys.exit(1)
        for item in intersection:
            print("docID: ", item)
            # print(index_word_1[item])
            # print(index_word_2[item])
            # implement your logic here and return the result

        #return intersection


