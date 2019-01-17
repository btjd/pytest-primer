class NumGen(object):
    def gen_odds(self, n):
        return [x for x in range(n) if x%2 != 0]

    def gen_evens(self, n):
        return [x for x in range(n) if x%2 == 0]

    def gen_squares(self, n):
        return [x**2 for x in range(n)]

class GenResults(object):
    def __init__(self):
        self.odds = None
        self.evens = None
        self.squares = None

    def __repr__(self):
        return """\n Obtained values are: 
                  \nOdds: {0} 
                  \nEvens: {1} 
                  \nSquares: {2}""".format(self.odds, self.evens, self.squares)
