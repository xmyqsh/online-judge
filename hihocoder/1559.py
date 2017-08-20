import sys
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        lines = word.split('/')
        for i in range(1, len(lines)):
            letter = lines[i]
            child = node.data.get(letter)
            if not child:
                node.data[letter] = TrieNode()
            node = node.data[letter]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ret = ""
        cur = []
        node = self.root
        lines = word.split('/')
        for i in range(1, len(lines)):
            letter = lines[i]
            cur.append(letter)
            node = node.data.get(letter)
            if len(node.data.keys()) == 0:
                break
            elif len(node.data.keys()) > 1:
                ret = ret + "/" + '-'.join(cur)
                cur = []
        ret = ret + "/" + '-'.join(cur[:-1]) + "/" + letter
        return ret

# Your Trie object will be instantiated and called as such:
trie = Trie()
line = sys.stdin.readline().strip()
n = int(line)
lines = [None] * n
for i in range(n):
    lines[i] = sys.stdin.readline().strip()
    trie.insert(lines[i])

for i in xrange(n):
    tmp = trie.search(lines[i])
    words = tmp.split('/')
    newWords = ['']
    for word in words:
        if word == '':
            continue
        newWords.append(word)
    print '/'.join(newWords)
