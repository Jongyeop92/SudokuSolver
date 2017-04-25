# -*- coding: utf8 -*-


import copy
import time


digits = "123456789"
rows   = "ABCDEFGHI"
cols   = digits

def cross(A, B):
    return [a + b for a in A for b in B]

squares = cross(rows, cols)

unitlist = [[r + c for c in cols] for r in rows] + \
           [[r + c for r in rows] for c in cols] + \
           [cross(rs, cs) for rs in ["ABC", "DEF", "GHI"] for cs in ["123", "456", "789"]]

units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)


class Sudoku:

    def __init__(self):
        self.board = dict((s, digits) for s in squares)

    def setData(self, data):
        validData = ""

        for d in data:
            if d in digits or d in ". ":
                validData += d

        assert len(validData) == 81

        for s, d in zip(squares, validData):
            if d in digits:
                self.assign(s, d)

    def assign(self, s, d):
        otherValues = self.board[s].replace(d, "")

        if all(self.eliminate(s, d2) for d2 in otherValues):
            return True

        return False

    def eliminate(self, s, d):
        if d not in self.board[s]:
            return True
        
        self.board[s] = self.board[s].replace(d, "")

        if len(self.board[s]) == 0:
            return False
        elif len(self.board[s]) == 1:
            d2 = self.board[s]
            if not all(self.eliminate(s2, d2) for s2 in peers[s]):
                return False

        for u in units[s]:
            dplaces = [s for s in u if d in self.board[s]]

            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(dplaces[0], d):
                    return False

        return True

    def isEnd(self):
        return all(len(self.board[s]) == 1 for s in squares)

    def isError(self):
        return any(len(self.board[s]) == 0 for s in squares)

    def show(self):
        width = 1 + max(len(self.board[s]) for s in squares)
        line = "+".join(["-" * (width * 3)] * 3)
        
        for r in rows:
            print "".join(self.board[r + c].center(width, ' ') + ("|" if c in "36"  else "") for c in cols)
            if r in "CF":
                print line
        print


def solve(sudoku):

    if sudoku.isEnd():
        return sudoku
    elif sudoku.isError():
        return False

    _, s = min((len(sudoku.board[s]), s) for s in squares if len(sudoku.board[s]) > 1)

    for d in sudoku.board[s]:
        copySudoku = copy.deepcopy(sudoku)

        copySudoku.assign(s, d)
        result = solve(copySudoku)

        if result:
            return result

    return False


def test():

    assert len(squares)      == 81
    assert len(unitlist)     == 27
    assert all(len(peers[s]) == 20 for s in squares)
    

    sudoku = Sudoku()
    assert sudoku.isEnd() == False
    
    sudoku.setData(".578..9.....3..2.83.8.....1289.6.51.5.3...4.6.64.5.8278.....3.57.2..5.....5..768.")
    assert sudoku.isEnd() == False

    sudoku.show()

    result = solve(sudoku)
    assert result.isEnd() == True
    result.show()
    

    print "Success"


def main():

    #data = "..7......5..32......4..9752....9......37.25......4....7429..8......74..9......4.."
    #data = "85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4."
    data = "..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."
    
    sudoku = Sudoku()
    sudoku.setData(data)

    sudoku.show()

    start = time.time()
    
    result = solve(sudoku)

    gap = time.time() - start

    if result:
        result.show()
        print "Success"
    else:
        print "Fail"

    print
    print "Time:", gap


if __name__ == "__main__":
    #test()
    main()
