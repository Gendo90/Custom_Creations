from collections import defaultdict


class Trie:
    def __init__(self):
        self.trie_map = defaultdict(dict)
        self.counter = 0

    def insert(self, pattern: str) -> None:
        pattern += "$"
        curr_node = 0
        i = 0
        n_pattern = len(pattern)
        # go through letters in the pattern until the letter is no longer
        # in the trie
        while (i < n_pattern and pattern[i] in self.trie_map[curr_node]):
            curr_node = self.trie_map[curr_node][pattern[i]]
            i += 1

        if (i < n_pattern):
            # add all the remaining letters in the pattern to the end of the trie
            # as a separate branch
            for j in range(i, n_pattern):
                self.trie_map[curr_node].update({pattern[j]: self.counter + 1})
                self.counter += 1
                curr_node = self.counter

    def search(self, text: str) -> bool:
        text_len = len(text)

        curr_node = 0
        curr_letter = text[0]
        counter = 0

        while (curr_letter in self.trie_map[curr_node]):
             curr_node = self.trie_map[curr_node][curr_letter]
              counter += 1

               if (counter < text_len):
                    curr_letter = text[counter]
                else:
                    break

        return "$" in self.trie_map[curr_node] and counter == text_len

    def startsWith(self, prefix: str) -> bool:
        text_len = len(prefix)

        curr_node = 0
        curr_letter = prefix[0]
        counter = 0

        while (curr_letter in self.trie_map[curr_node]):
             curr_node = self.trie_map[curr_node][curr_letter]
              counter += 1

               if (counter < text_len):
                    curr_letter = prefix[counter]
                else:
                    break

        return counter == text_len


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
