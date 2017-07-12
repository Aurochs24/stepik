objects = [1,2,3,1,2]
ans = 0
objs = []
for obj in objects:
    ns = 0
    for o in objs:
        if obj is o:
            ns += 1
    if ns == 0:
        objs.append( obj )
        ans += 1

print(ans)
