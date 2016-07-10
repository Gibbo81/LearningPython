class Set():
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def union(self, other):
        data = self.data.copy()     #self.data[:] it's the same
        for x in other.data:
            if not x in data:
                data.append(x)
        return Set(data)

    def intersect(self, other):
        data = []
        for x in self.data:
            if x in other.data:
                data.append(x)
        return Set(data)

    def __and__(self, other): return self.intersect(other)

    def __or__(self, other): return self.union(other)

    def __iter__(self) : return iter(self.data)

    def __repr__(self):
        return str(self.data)

if __name__=='__main__':
    a = Set([1,2,3,4,5,6,7]) 
    print(a)
    b = Set([5,6,7,8,9,10,11]) 
    print(b)
    c = a.union(b)
    print("Union: %s" % c)
    c = b.intersect(a)
    print("Intersect: %s" % c)

    print(a | Set([4,5,6,7])) 
    print(a & Set([4,5,6,7])) 