# inheritance
from pythonBasics.oops import Calculator


class childImp(Calculator): # call the parent class name
    num2 = 200

    def __init__(self): # call the parent constructor name
        Calculator.__init__(self, 2, 10)

    def getcompleteData(self):
        return self.num2 + self.num + self.summation()


obj = childImp()
print(obj.getcompleteData())
