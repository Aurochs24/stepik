class Cls:
    classes = {}

    def __init__(self, name, *ancs):
        self.dirAncs = {}
        for ancName in ancs:
            if ancName in self.classes:
                curCls = self.classes[ancName]
            else:
                curCls = Cls(ancName)
            self.dirAncs[ancName] = curCls
        self.classes[name] = self

    def Is_ancestor(ancName, clsName):
        if not clsName in Cls.classes:
            return False
        cls = Cls.classes[clsName]
        if ancName == clsName:
            return True
        if ancName in cls.dirAncs.keys():
            return True
        else:
            for anc in cls.dirAncs:
                res = Cls.Is_ancestor(ancName, anc)
                if res:
                    return True
        return False


n = int(input())
for i in range(n):
    pars = input().split()
    c = Cls(pars[0], *pars[2:])

q = int(input())
excepted = {}
for i in range(q):
    par = input()
    success = True
    for eName in excepted:
        if Cls.Is_ancestor(eName, par):
            print( par )
            success = False
            break
    if success:
        if par in Cls.classes:
            excepted[par] = Cls.classes[par]
