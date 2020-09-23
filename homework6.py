class Human:
    _name=""
    _gender=0
    _height=0
    _weught=0
    def __init__(self,name,gender,height,weight):
        self._name=name
        self._gender=gender
        self._height=height
        self._weight=weight

    def sing(self):
        print(self._name+"sing")

    def dance(self):
        print(self._name+"dance")

H1=Human("Benson",1,197,71)
H1.sing()
H2=Human("Emily",2,169,65)
H2.dance()