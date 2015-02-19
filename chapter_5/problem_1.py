class Reverse_Iter:
    def __init__(self, lst):
        self.first_index = 0
        self.last_index = len(lst) - 1
        self.i = lst[self.first_index]
        self.n = lst[self.last_index]

    def __iter__(self):
        return Reverse_Iter_List(self)

class Reverse_Iter_List(self, lst)
    def next(self):
        if self.first_index <= self.last_index:
            i = self.i
            self.first_index += 1
            
            return i
        else:
            raise StopIteration()


a = Reverse_Iter([1,2,3,4])

print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
