from sys import stdin
import io
stdin = io.StringIO("""4
0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2""")
#for line in stdin.readlines():
#    print(line)
sq=[line.strip("\n").split(" ") for line in stdin.readlines()[1:]]
print(sq)
maxv=-1000
current=-1
size=len(sq)
for l in range (size):
        for w in range(size):
            val=0
            print(f"ancho= {size-w}")
            print(f"largo= {size-l}")
            for i in range (size-w):
                val+=int(sq[l][w+i])
                maxv= maxv if maxv>val else val
                #print(sq[l][w+i])
            val=0
            for i in range (size-l):
                #print(sq[l+i][w])
                val+=int(sq[l+i][w])
                maxv= maxv if maxv>val else val
            val=0
            for i in range (size-l):
                for j in range (size-w):
                    val+=int(sq[l+i][w+j])
                    print(int(sq[l+i][w+j]))
            maxv= maxv if maxv>val else val
            #print(f"value={val}")
            val=0



            #print(val)
            maxv= maxv if maxv>val else val
for l in range (size):
        for w in range(size):
            print(f"ancho= {size-w}")
            print(f"largo= {size-l}")
            val=0
            for i in range (l):
                for j in range (w):
                    val+=int(sq[i][j])
                    print(int(sq[i][j]))
            maxv= maxv if maxv>val else val
            #print(f"value={val}")
            val=0

        


print(maxv)

