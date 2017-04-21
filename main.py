# -*- coding: utf8 -*-


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
digits   = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

class Sudoku:

    def __init__(self):
        self.boardKeyList = [a + d for a in alphabet
                                   for d in digits]

        self.board = dict


    def setData(self, data):
        pass

    def isEnd(self):
        return None


def test():

    sudoku = Sudoku()

    assert len(sudoku.boardKeyList) == 81

    print sudoku.boardKeyList
    
    sudoku.setData('')

    assert sudoku.isEnd() == True

    print "Success"


def main():

    pass


if __name__ == "__main__":
    test()
    #main()
