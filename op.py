class AClass():
    name = "Uasya"

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

    def __repr__(self):
        return "<class AClass()>"

    def __str__(self):
        return f"{self.name}"

    def __setattr__(self, name, value):
        print(name, value, "установка значения")
        super(). __setattr__(name, value)
        #self._dict_[name] = value








if __name__ == '__main__':
    a = AClass("A", "Object")
    b = AClass("B", "Object")
    a.attr1 = 1
    #print(dir(a))
    #print(dir(b))
    print(a.__dict__)
    #print(a.name)
    #print(b.name)
    #print(a.first_name)
    #print(b.first_name)
    #print("{}".format(a))
    #print("{}".format(b))
    #print("{!r}".format(a))
    #print("{!r}".format(b))
