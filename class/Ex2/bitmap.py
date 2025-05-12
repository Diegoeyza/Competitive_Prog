from sys import stdin
import io
import math

stdin = io.StringIO("""D  15   8
DDDD101D010D11D010D0001DD1011D01DD00D011D1D101D01D001D01D1D011D10DD10D01D10DD10110D0010D0D1011DD0D0111DD1001D10DD01111D0D0110
#
""")

def type_B_to_D(bmap, r, c):
    r, c = int(r), int(c)
    bitmap = []
    for i in range(r):
        bitmap.append(bmap[i*c:(i+1)*c])
    def convert_region(row_start, row_end, col_start, col_end):
        all_ones=True
        all_zeros=True
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                if bitmap[i][j]=='0':
                    all_ones = False
                if bitmap[i][j]=='1':
                    all_zeros=False
        if all_ones:
            return "1"
        elif all_zeros:
            return "0"
        else:
            result = "D"
            rows=row_end-row_start
            cols= col_end- col_start
            
            if rows ==1 and cols==1:
                return bitmap[row_start][col_start]
            
            if rows==1:
                mid_col=col_start+(cols+1)// 2
                result+=convert_region(row_start, row_end, col_start, mid_col)
                result+=convert_region(row_start, row_end, mid_col, col_end)
                return result
            
            if cols==1:
                mid_row=row_start + (rows + 1) // 2
                result+=convert_region(row_start, mid_row, col_start, col_end)
                result+=convert_region(mid_row, row_end, col_start, col_end)
                return result
            
            mid_row=row_start+(rows + 1) // 2
            mid_col=col_start+(cols + 1) // 2
            result+=convert_region(row_start, mid_row, col_start, mid_col)
            result += convert_region(row_start, mid_row, mid_col, col_end)
            result += convert_region(mid_row, row_end, col_start, mid_col)
            result += convert_region(mid_row, row_end, mid_col, col_end)
            return result
    return convert_region(0, r, 0, c)
def type_D_to_B(bmap, r, c):
    r, c = int(r), int(c)
    bitmap=[[''] * c for aux in range(r)]
    index = [0]  
    def parse_region(row_start, row_end, col_start, col_end):
        if index[0]>=len(bmap):
            return
        char = bmap[index[0]]
        index[0] += 1
        
        if char=='1':
            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    bitmap[i][j]='1'
        elif char=='0':
            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    bitmap[i][j] = '0'
        elif char=='D':
            rows = row_end - row_start
            cols = col_end - col_start
            if rows == 1 and cols == 1:
                return

            if rows==1:
                mid_col=col_start + (cols + 1) // 2
                parse_region(row_start, row_end, col_start, mid_col)
                parse_region(row_start, row_end, mid_col, col_end)
                return
            
            if cols==1:
                mid_row = row_start + (rows + 1) // 2
                parse_region(row_start, mid_row, col_start, col_end)
                parse_region(mid_row, row_end, col_start, col_end)
                return
            
            mid_row=row_start+(rows + 1)//2
            mid_col= col_start+(cols+ 1)//2
            parse_region(row_start, mid_row, col_start, mid_col)
            parse_region(row_start, mid_row, mid_col, col_end)
            parse_region(mid_row, row_end, col_start, mid_col)
            parse_region(mid_row, row_end, mid_col, col_end)
    parse_region(0, r, 0, c)
    result = ""
    for i in range(r):
        result+=''.join(bitmap[i])
    return result

format = stdin.readline().split()
while format[0] != "#":
    t, row, col = format
    bmap=stdin.readline().strip()
    # trying to fix the mf input constrainttttt
    while len(bmap) < int(row) * int(col):
        bmap+=stdin.readline().strip()
    if t=="B":
        print(f"D {row} {col}")
        result = type_B_to_D(bmap, row, col)
        for i in range(0, len(result), 50):
            print(result[i:i+50])
    else:
        print(f"B {row} {col}")
        result=type_D_to_B(bmap, row, col)

        for i in range(0, len(result), 50):
            print(result[i:i+50])
    
    format = stdin.readline().split()
