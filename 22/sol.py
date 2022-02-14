class AABB:
    def __init__(self, xs, xe, ys, ye, zs, ze):    
        self.xs, self.xe = sorted([xs, xe])    
        self.ys, self.ye = sorted([ys, ye])    
        self.zs, self.ze = sorted([zs, ze])    

    def __iter__(self):
        yield self.xs
        yield self.xe    
        yield self.ys
        yield self.ye    
        yield self.zs
        yield self.ze    

    def __eq__(self, other):
        x = self.xs == other.xs and self.xe == other.xe
        y = self.ys == other.ys and self.ye == other.ye
        z = self.zs == other.zs and self.ze == other.ze
        return x and y and z

    def __repr__(self):
        return f"x={self.xs}..{self.xe}, y={self.ys}..{self.ye}, z={self.zs}..{self.ze}"      

    def __hash__(self):
        return hash(repr(self))    

    def intersects(self, other):
        sxs, sxe, sys, sye, szs, sze = self  
        oxs, oxe, oys, oye, ozs, oze = other  

        return sxs <= oxe and sxe >= oxs and sys <= oye and sye >= oys and szs <= oze and sze >= ozs

    def overlap(self, other):
        if not self.intersects(other):    
            return None    

        xs = max(self.xs, other.xs)
        xe = min(self.xe, other.xe)

        ys = max(self.ys, other.ys)
        ye = min(self.ye, other.ye)

        zs = max(self.zs, other.zs)
        ze = min(self.ze, other.ze)
        return AABB(xs, xe, ys, ye, ze, zs)       

    def volume(self):
        return (self.xe - self.xs) * (self.ye - self.ys) * (self.ze - self.zs)    

    def remove(self, other):
        if (ol := self.overlap(other)) is None:
            return None 

        xs, xe, ys, ye, zs, ze = other
        ixs, ixe, iys, iye, izs, ize = ol
        
        res = []
        # we should return 26!!!
        # bounding boxes jeez
        # well lets get to work 

        # we do one  face
        res.append(AABB(xs, ixs, ys, iys, zs, izs))
        res.append(AABB(ixs, ixe, ys, iys, zs, izs))
        res.append(AABB(ixe, xe, ys, iys, zs, izs))
        res.append(AABB(xs, ixs, iys, iye, zs, izs))
        res.append(AABB(ixs, ixe, iys, iye, zs, izs))
        res.append(AABB(ixe, xe, iys, iye, zs, izs))
        res.append(AABB(xs, ixs, iye, ye, zs, izs))
        res.append(AABB(ixs, ixe, iye, ye, zs, izs))
        res.append(AABB(ixe, xe, iye, ye, zs, izs))
        
        # now we do the same face, moving z
        res.append(AABB(xs, ixs, ys, iys, izs, ize))
        res.append(AABB(ixs, ixe, ys, iys, izs, ize))
        res.append(AABB(ixe, xe, ys, iys, izs, ize))
        res.append(AABB(xs, ixs, iys, iye, izs, ize))
        #res.append(AABB(ixs, ixe, iys, iye, izs, ize)) # mr intersection itself!
        res.append(AABB(ixe, xe, iys, iye, izs, ize))
        res.append(AABB(xs, ixs, iye, ye, izs, ize))
        res.append(AABB(ixs, ixe, iye, ye, izs, ize))
        res.append(AABB(ixe, xe, iye, ye, izs, ize))
        
        # last z    
        res.append(AABB(xs, ixs, ys, iys, ize, ze))
        res.append(AABB(ixs, ixe, ys, iys, ize, ze))
        res.append(AABB(ixe, xe, ys, iys, ize, ze))
        res.append(AABB(xs, ixs, iys, iye, ize, ze))
        res.append(AABB(ixs, ixe, iys, iye, ize, ze))
        res.append(AABB(ixe, xe, iys, iye, ize, ze))
        res.append(AABB(xs, ixs, iye, ye, ize, ze))
        res.append(AABB(ixs, ixe, iye, ye, ize, ze))
        res.append(AABB(ixe, xe, iye, ye, ize, ze))

        return ([c for c in res if c.volume() > 0], ol)

def parse_line(s):
    xt, yt, zt = s.split(",")                
    oper, xt = xt.split(" ", 1)   
    xs, xe = map(int, xt[2:].split(".."))
    ys, ye = map(int, yt[2:].split(".."))
    zs, ze = map(int, zt[2:].split(".."))
    return (oper, AABB(xs, xe, ys, ye, zs, ze))    

with open("input.txt", "r") as f:
    txt = f.read()    
    steps = [parse_line(l) for l in txt.splitlines()]        

def part1(steps):
    s = set()    
    target = AABB(-50, 50, -50, 50, -50, 50)
    for op, c in steps:
        if (ol := c.overlap(target)) is not None:
            xs, xe, ys, ye, zs, ze = ol
            for x in range(xs, xe + 1):
                for y in range(ys, ye + 1):    
                    for z in range(zs, ze + 1):    
                        if op == "on":    
                            s.add((x, y, z))
                        else:
                            s.discard((x, y, z))        
    return len(s)  

def part2(steps):
    lit = set()
    for op, c in steps:
        xs, xe, ys, ye, zs, ze = c
        c = AABB(xs-0.5,xe+0.5,ys-0.5,ye+0.5,zs-0.5,ze+0.5)
        print(op, c)
        for cc in lit.copy():
            if (r := c.remove(cc)) is not None:                                    
                lit.remove(cc)    
                lit.update(rr for rr in r[0]) 
        if op == "on":    
            lit.add(c)    
    return sum(c.volume() for c in lit)
