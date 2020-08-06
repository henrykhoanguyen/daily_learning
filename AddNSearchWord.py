'''
Problem: 211. Add and Search Word - Data structure design
Input: word: str -> to be add or search in Trie tree
Output: boolean value if such word exist in dictionary
Explanation:
    By implementing Trie tree using dictionary/hashtable,
    we will be able to add and search word in O(n) time.
    To search word, two approaches we can take are stack
    and recursion. Checking if a letter of the word exists
    as we traverse through Trie tree. Return false at any
    point if a letter isn't in tree or continue until we
    found that it is an end of a word. Space complexity
    of this problem is O(N*M) in which N is number of
    node and M is the length of string.
'''

class Node:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        wordLen = len(word)
        current = self.trie

        for i in range(wordLen):
            if word[i] not in current.children:
                current.children[word[i]] = Node()
                current = current.children[word[i]]
            else:
                current = current.children[word[i]]

        current.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        wordLen = len(word)

        # Stack approach
        '''
        stack = [(self.trie, word)]

        while stack:
            node, w = stack.pop()
            # print(w)
            if not w:
                if node.endOfWord:
                    print(True)
                    return True
            elif w[0] == ".":
                for n in node.children.values():
                    stack.append((n, w[1:]))
            else:
                if w[0] in node.children:
                    stack.append((node.children[w[0]], w[1:]))
        print(False)
        return False
        '''

        # DFS recursion approach
        self.isFound = False
        self.dfs(self.trie, word)
        print(self.isFound)
        return self.isFound


    def dfs(self, node, word) -> None:
        if not word:
            if node.endOfWord:
                self.isFound = True
            return

        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            if word[0] not in node.children:
                return
            self.dfs(node.children[word[0]], word[1:])


sol = WordDictionary()
# sol.addWord("bad")
# sol.addWord("dad")
# sol.addWord("mad")
# sol.search("pad")
# sol.search("bad")
# sol.search(".ad")
# sol.search("b..")
# sol.search("b.d")

actions = ["addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"]
params = [["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]

for i in range(len(actions)):
    if actions[i] == "addWord":
        sol.addWord(params[i][0])
    else:
        sol.search(params[i][0])

print("Expect:",True,False,True,True,True,False,True,True,False,False)