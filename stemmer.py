
class PorterStemmer:

    def letter_consonant(self, i):
        vowels = "aeiou"
        if i in vowels:
            return False
        else:
            return True

    def is_consonant(self, word, i):
        letter = word[i]

        if self.letter_consonant(letter):
            #print(word,letter,i)
            if letter != 'y':
                return True
            elif letter == 'y' and i == 0:
                return True
            elif letter == 'y' and self.letter_consonant(word[i-1]):
                return False
            else:
                return True
        else:
            return False

    def is_vowel(self, word, i):
        return not(self.is_consonant(word, i))

    def contains_vowel(self, stem):
        for i in range(len(stem)):
            if self.is_vowel(stem, i):
                return True
        return False

    def get_form(self, word):
        pattern = []
        form = ''
        for i in range(len(word)):
            if self.is_vowel(word, i):
                pattern.append('V')
            else:
                pattern.append('C')
        for j in pattern:
            form += j
        return form

    def get_m_count(self, word):
        form_string = self.get_form(word)
        count = form_string.count('VC')
        return count

    def cvc(self, stem):
        if len(stem) > 3:
            if self.is_consonant(stem, -3) and self.is_vowel(stem, -2) and self.is_consonant(stem, -1):
                if stem[-1] != 'w' and stem[-1] != 'x' and stem[-1] != 'y':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def helper_1b(self, word):
        if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
            word += 'e'
        elif self.double_consonant(word) and not word.endswith('l') and not word.endswith('s') and not word.endswith('z'):
            word = word[:-1]
        elif self.get_m_count(word) == 1 and self.cvc(word):
            word += 'e'
        return word

    def double_consonant(self, stem):
        if len(stem) >= 2:
            if self.is_consonant(stem, -1) and self.is_consonant(stem, -2):
                return True
            else:
                return False
        else:
            return False

    def replace(self,word, rule, replace, threshold):
        result = word.rfind(rule)
        stem = word[:result]
        if self.get_m_count(stem) > threshold:
            word = stem + replace
            return word
        else:
            return word

    def step_1a(self, word):
        if word.endswith('sses'):
            word = word[:-2]
        elif word.endswith("ies"):
            word = word[:-2]
        elif word.endswith("ss"):
            word = word
        elif word.endswith("s"):
            word = word[:-1]
        return word

    def step_1b(self, word):

        if word.endswith('eed'):
            suffix_len = len('eed')
            stem = word[:suffix_len]
            if self.get_m_count(stem) > 0:
                word = word[:-1]

        elif word.endswith('ed'):
            suffix_len = word.rfind('ed')
            stem = word[:suffix_len]
            if self.contains_vowel(stem):
                word = stem
                word = self.helper_1b(word)

        elif word.endswith('ing'):
            suffix_len = word.rfind('ing')
            stem = word[:suffix_len]
            if self.contains_vowel(stem):
                word = stem
                word = self.helper_1b(word)

        return word

    def step_1c(self, word):
        if word.endswith('y'):
            result = word.rfind('y')
            stem = word[:result]
            if self.contains_vowel(stem):
                word = stem
                word += 'i'
        return word

    def step_2(self, word):
        if word.endswith('ational'):
            word = self.replace(word, 'ational', 'ate', 0)
        elif word.endswith('tional'):
            word = self.replace(word, 'tional', 'tion', 0)
        elif word.endswith('enci'):
            word = self.replace(word, 'enci', 'ence', 0)
        elif word.endswith('anci'):
            word = self.replace(word, 'anci', 'ance', 0)
        elif word.endswith('izer'):
            word = self.replace(word, 'izer', 'ize', 0)
        elif word.endswith('abli'):
            word = self.replace(word, 'abli', 'able', 0)
        elif word.endswith('alli'):
            word = self.replace(word, 'alli', 'al', 0)
        elif word.endswith('entli'):
            word = self.replace(word, 'entli', 'ent', 0)
        elif word.endswith('eli'):
            word = self.replace(word, 'eli', 'e', 0)
        elif word.endswith('ousli'):
            word = self.replace(word, 'ousli', 'ous', 0)
        elif word.endswith('ization'):
            word = self.replace(word, 'ization', 'ize', 10)
        elif word.endswith('ation'):
            word = self.replace(word, 'ation', 'ate', 0)
        elif word.endswith('ator'):
            word = self.replace(word, 'ator', 'ate', 0)
        elif word.endswith('alism'):
            word = self.replace(word, 'alism', 'al', 0)
        elif word.endswith('iveness'):
            word = self.replace(word, 'iveness', 'ive', 0)
        elif word.endswith('fulness'):
            word = self.replace(word, 'fulness', 'ful', 0)
        elif word.endswith('ousness'):
            word = self.replace(word, 'ousness', 'ous', 0)
        elif word.endswith('aliti'):
            word = self.replace(word, 'aliti', 'al', 0)
        elif word.endswith('iviti'):
            word = self.replace(word, 'iviti', 'ive', 0)
        elif word.endswith('biliti'):
            word = self.replace(word, 'biliti', 'ble', 0)
        return word

    def step_3(self, word):
        if word.endswith('icate'):
            word = self.replace(word, 'icate', 'ic', 0)
        elif word.endswith('ative'):
            word = self.replace(word, 'ative', '', 0)
        elif word.endswith('alize'):
            word = self.replace(word, 'alize', 'al', 0)
        elif word.endswith('iciti'):
            word = self.replace(word, 'iciti', 'ic', 0)
        elif word.endswith('ful'):
            word = self.replace(word, 'ful', '', 0)
        elif word.endswith('ness'):
            word = self.replace(word, 'ness', '', 0)
        return word

    def step_4(self, word):
        if word.endswith('al'):
            word = self.replace(word, 'al', '', 1)
        elif word.endswith('ance'):
            word = self.replace(word, 'ance', '', 1)
        elif word.endswith('ence'):
            word = self.replace(word, 'ence', '', 1)
        elif word.endswith('er'):
            word = self.replace(word, 'er', '', 1)
        elif word.endswith('ic'):
            word = self.replace(word, 'ic', '', 1)
        elif word.endswith('able'):
            word = self.replace(word, 'able', '', 1)
        elif word.endswith('ible'):
            word = self.replace(word, 'ible', '', 1)
        elif word.endswith('ant'):
            word = self.replace(word, 'ant', '', 1)
        elif word.endswith('ement'):
            word = self.replace(word, 'ement', '', 1)
        elif word.endswith('ment'):
            word = self.replace(word, 'ment', '', 1)
        elif word.endswith('ent'):
            word = self.replace(word, 'ent', '', 1)
        elif word.endswith('ou'):
            word = self.replace(word, 'ou', '', 1)
        elif word.endswith('ism'):
            word = self.replace(word, 'ism', '', 1)
        elif word.endswith('ate'):
            word = self.replace(word, 'ate', '', 1)
        elif word.endswith('iti'):
            word = self.replace(word, 'iti', '', 1)
        elif word.endswith('ous'):
            word = self.replace(word, 'ous', '', 1)
        elif word.endswith('ive'):
            word = self.replace(word, 'ive', '', 1)
        elif word.endswith('ize'):
            word = self.replace(word, 'ize', '', 1)
        elif word.endswith('ion'):
            result = word.rfind('ion')
            stem = word[:result]
            if self.get_m_count(stem) > 1 and (stem.endswith('s') or stem.endswith('t')):
                word = stem
            word = self.replace(word, '', '', 1)
        return word

    def step_5a(self, word):
        if word.endswith('e'):
            stem = word[:-1]
            if self.get_m_count(stem) > 1:
                word = stem
            elif self.get_m_count(stem) == 1 and not self.cvc(stem):
                word = stem
        return word

    def step_5b(self, word):
        if self.get_m_count(word) > 1 and self.double_consonant(word) and word.endswith('l'):
            word = word[:-1]
        return word

    def stem(self, word):
        # try:
        #     if len(word) > 2:
        #         word = self.step_1a(word)
        #         word = self.step_1b(word)
        #         word = self.step_1c(word)
        #         word = self.step_2(word)
        #         word = self.step_3(word)
        #         word = self.step_4(word)
        #         word = self.step_5a(word)
        #         word = self.step_5b(word)
        #         return word
        #     else:
        #         return word
        # except:
        #     print("ERROR: Word {} cannot be stemmed".format(word))
        if len(word) > 2:
            word = self.step_1a(word)
            word = self.step_1b(word)
            word = self.step_1c(word)
            word = self.step_2(word)
            word = self.step_3(word)
            word = self.step_4(word)
            word = self.step_5a(word)
            word = self.step_5b(word)
        return word








