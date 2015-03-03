class Reverse_Iter:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return self

    def next(self

class Reverse_Iter_List:
    def __init__(self, lst):
        self.first_index = 0
        self.last_index = len(lst) - 1
        self.i = lst[self.first_index]

    def next(self):
        if self.first_index <= self.last_index:
            res = self.i
            self.first_index += 1
            
            return res
        else:
            raise StopIteration()


a = Reverse_Iter([1,2,3,4])

for i in a:
    print i
