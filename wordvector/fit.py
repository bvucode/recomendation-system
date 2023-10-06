
class Fit:
    def __init__(self, dlist, vect):
        self.dlist = dlist
        self.vect = vect

    def fit(self):
        mdict = {}
        result = []
        for i in self.dlist:
            tmplist = []
            for j in i:
                if j in self.vect.keys():
                    tmplist.append(self.vect[j])
            result.append(tmplist)
        return result
