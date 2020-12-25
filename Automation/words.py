from string import punctuation


class Text:
    def __init__(self, s, remove_numbers=True):
        self._to_remove = punctuation + "0123456789" if remove_numbers else punctuation
        self.words = []

        for word in s.split():
            if self.__remove_all_from_iter(word, self._to_remove) != '':
                self.words.append(self.__remove_all_from_iter(word, self._to_remove))

        self._lowered = [word.lower() for word in self.words]

    @staticmethod
    def __remove_all_from_iter(s, itr):
        res = ''
        for char in s:
            if char not in itr:
                res += char
        return res

    def get_len(self):
        return len(self.words)

    def unsorted_count_map(self):
        return {k: self._lowered.count(k) for k in set(self._lowered)}

    def sorted_count_map(self):
        # Least to most
        return dict(sorted(self.unsorted_count_map().items(), key=lambda item: item[1]))

    def most_used_word(self):
        return tuple(self.sorted_count_map().keys())[-1]


with open("bee_movie_script", 'r') as f:
    myText = Text(f.read(), remove_numbers=False)
    print(f"Length: {myText.get_len()}\nWords: {myText.sorted_count_map()}\nMost used: {myText.most_used_word()}")
