data = [i.split() for i in open('data').read().strip().split('\n')]

def computer(regs):
    stack = []
    pc = 0
    while pc < len(data):
        ins = data[pc]
        if ins[0] == 'push':
            if ins[1][-1].isnumeric():
                stack.append(int(ins[1]))
            else:
                stack.append(int(regs[ins[1]]))
            pc +=1
        if ins[0] == 'add':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
            pc += 1
        if ins[0] == 'jmpos':
            a = stack.pop()
            if a >=0:
                pc += int(ins[1])+1
            else:
                pc +=1
        if ins[0] == 'ret':
            a = stack.pop()
            return a
                
regs = {}
res = []
kaart = {}
for x in range(30):
    for y in range(30):
        for z in range(30):
            regs['X'] = x;regs['Y'] = y;regs['Z'] = z
            ans = computer(regs)
            res.append(ans)
            kaart[(x,y,z)] = ans

print(sum(res))

for x in range(30):
    for y in range(30):
        for z in range(30):
            if kaart[(x,y,z)] <= 0:
                del kaart[(x,y,z)]

dirs = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
clouds = {}
cnt = 0
while len(kaart) > 0:
    start = list(kaart.keys())[0]
    clouds[cnt] = [start]
    queue = [start]
    for x,y,z in queue:
        for dx,dy,dz in dirs:
            nx,ny,nz = x+dx,y+dy,z+dz
            if (nx,ny,nz) in kaart and (nx,ny,nz) not in clouds[cnt]:
                clouds[cnt].append((nx,ny,nz))
                queue.append((nx,ny,nz))
    for val in clouds[cnt]:
        del kaart[val]        
    cnt +=1

print(cnt)