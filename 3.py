def co ( n, k ):
    if n < k:
        return 0
    elif k == 0:
        return 1
    else:
        return co( n - 1, k ) + co( n - 1, k - 1 )

#n, k = map(int, input().split())
n = 10
k = 5
print ( co( n, k ) )

spaces = { "global":{'*': None } }

def get ( namespace, var ):
    global spaces
    
    if namespace in spaces:
        if var in spaces[namespace]:
            print( namespace )
        elif (spaces[namespace])['*'] == None:
            print( 'None' )
        else:
            get( (spaces[namespace])['*'], var )
    else:
        print( 'None' )

n = int(input())
for i in range( n ):
    cmd, par1, par2 = input().split()
    if cmd == "create":
        if par2 in spaces:
            spaces[par1] = { '*': par2 }
    elif cmd == "add":
        if par1 in spaces:
            (spaces[par1])[par2] = None
    elif cmd == "get":
        get( par1, par2 )
    else:
        pass
        
        
class Buffer:
    def __init__(self):
        # ??????????? ??? ??????????
        self.rest = []

    def add(self, *a):
        # ???????? ????????? ????? ??????????????????
        for par in a:
            self.rest.append( par )
            if len( self.rest ) >= 5:
                sum = 0
                for elem in self.rest:
                    sum += elem
                print( sum )
                self.rest = []

    def get_current_part(self):
        # ??????? ??????????? ? ??????? ?????? ???????? ?????????????????? ? ???????, ? ??????? ??? ???? ?????????
        return  self.rest
        
 
 
class Cls:
    classes = {}
    
    def __init__ ( self, name, *ancs ):
        self.dirAncs = {}
        for ancName in ancs:
            if ancName in self.classes:
                curCls = self.classes[ancName]
            else:
                curCls = Cls( ancName )
            self.dirAncs[ancName] = curCls
        self.classes[name] = self
        
    def Is_ancestor ( ancName, clsName ):
        if not clsName in Cls.classes:
          return False
        cls = Cls.classes[clsName]
        if ancName == clsName:
          return True
        if ancName in cls.dirAncs.keys():
          return True
        else:
          for anc in cls.dirAncs:
            res = Cls.Is_ancestor( ancName, anc )
            if res:
                return True
        return  False

n = int(input())
for i in range( n ):
    pars = input().split()
    c = Cls( pars[0], *pars[2:] )
    
q = int(input())
for i in range( q ):
    pars = input().split()
    if Cls.Is_ancestor( pars[0], pars[1] ):
        print( "Yes" )
    else:
        print( "No" )


class LoggableList ( list, Loggable ):
    def append( self, v ):
        list.append( self, v )
        self.log( str( v ) )
