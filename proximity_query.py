import sys


class ProximityQuery:

    def __init__(self, index, word1, word2, k):
        self.index = index
        self.word_1 = word1
        self.word_2 = word2
        self.k = k
        self.result = []

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
            pos_list_1 = index_word_1[item]
            pos_list_2 = index_word_2[item]
            pos_res_list = []
            ii = 0
            jj = 0
            while ii != len(pos_list_1):
                while jj != len(pos_list_2):
                    distance = abs(pos_list_1[ii] - pos_list_2[jj])
                    if distance <= self.k:
                        pos_res_list.append(pos_list_2[jj])
                    elif pos_list_2[jj] > pos_list_1[ii]:
                        break
                    jj += 1
                while pos_res_list != [] and abs(pos_res_list[0] - pos_list_1[ii]) > self.k:
                    pos_res_list.remove(pos_res_list[0])
                for it in pos_res_list:
                    self.result.append({'docID': item, 'position_word1': pos_list_1[ii], 'position_word2': it})
                ii += 1
        if not self.result:
            print("ERROR: words '{}' and '{}' are not found within {} positions in documents: {}".
                  format(self.word_1,
                         self.word_2,
                         self.k,
                         intersection))
            sys.exit(1)
        return self.result


