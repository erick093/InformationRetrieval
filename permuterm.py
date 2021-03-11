class Permuterm:
    def __init__(self, index):
        self.index = index
        self.keys = index.keys()
        self.permuterm_dict = {}


    @staticmethod
    def rotate(word, n):
        return word[n:] + word[:n]

    def construct_index(self):
        for key in self.keys:
            permuterm_key = key + "$"
            for i in range(len(permuterm_key), 0, -1):
                self.permuterm_dict[self.rotate(permuterm_key, i)] = key
        return self.permuterm_dict

    def execute_query(self, query, return_keys=False):
        if return_keys:
            return [k for k, v in self.permuterm_dict.items() if
                    k.startswith(query)]  # O(n) not the best, but does the work
        else:
            return [v for k, v in self.permuterm_dict.items() if
                    k.startswith(query)]  # O(n) not the best, but does the work

    def query_type_1(self, sectors):  # case X*
        query = '$' + sectors[0]
        return self.execute_query(query)

    def query_type_2(self, sectors):  # case *X
        query = sectors[1] + '$'
        return self.execute_query(query)

    def query_type_3(self, sectors):  # case *X*
        query = sectors[1]
        return self.execute_query(query)

    def query_type_4(self, sectors):  # case X*Y
        query = sectors[2] + '$' + sectors[0]
        return self.execute_query(query)

    def query_type_5(self, sectors):  # case X*Y*Z - it works for any 2 wildcard queries
        query_1 = sectors[2] + '$' + sectors[0]   # Z$X*
        query_2 = sectors[1]  # Y*
        matched_keys = self.execute_query(query_1, return_keys=True)
        result = []
        for item in matched_keys:
            if query_2 in item:
                result.append(self.permuterm_dict[item])
        return result

    def query(self, query):
        sectors = query.split('*')
        length_sectors = len(sectors)
        if length_sectors == 4:
            print("case 6")
        elif length_sectors == 3:
            if sectors[0] == '' and sectors[2] == '':
                print("case 3")
                dict_values = self.query_type_3(sectors)
            else:
                print("case 5")
                dict_values = self.query_type_5(sectors)
        elif length_sectors == 2:
            if sectors[0] == '':
                print("case 2")
                dict_values = self.query_type_2(sectors)
            elif sectors[1] == '':
                print("case 1")
                dict_values = self.query_type_1(sectors)
            elif sectors[0] != '' and sectors[1] != '':
                print("case 4")
                dict_values = self.query_type_4(sectors)
        result_dict = {}
        for item in dict_values:
            result_dict[item] = self.index[item]
        return result_dict













