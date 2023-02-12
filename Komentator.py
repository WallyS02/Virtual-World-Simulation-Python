class Komentator:
    def __init__(self):
        self.text = ""

    def addComment(self, comment):
        self.text += comment + '\n'

    def getText(self):
        return self.text

    def eraseComments(self):
        self.text = ""
