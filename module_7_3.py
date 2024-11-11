class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            words = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    s = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
                    for sim in s:
                        line = line.replace(sim, '')
                    words.extend(line.split(' '))
            t = {name: words}
            all_words.update(t)
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            word = word.lower()
            for names in self.file_names:
                name = names
                find_dict.update({name: words.index(word) + 1})
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            word = word.lower()
            for names in self.file_names:
                name = names
                counter = 0
                for check in words:
                    if word == check:
                        counter += 1
                count_dict.update({name: counter})
        return count_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего