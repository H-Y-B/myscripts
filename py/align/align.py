import sys
# for verilog signals

left_num   = 0
right_num   = 0
left_max   = 0
mid_max   = 0


with open(sys.argv[1]) as f:
    lines = f.readlines()

out=open("align_"+sys.argv[1],"w")

for line in lines:
    if ')' in line and '(' in line: 
        left_num= line.find('(')  #
        if left_max < left_num:
            left_max=left_num

        right_num= line.find(')')
        if mid_max < (right_num-left_num):
            mid_max = right_num-left_num

for line in lines:
    linelist= list(line)
    if ')' in line and '(' in line: 
        left_num= line.find('(')
        for i in range(left_max-left_num):
            linelist.insert(left_num,' ')

        right_num=linelist.index(')')
        for i in range(left_max+mid_max - right_num):
            linelist.insert(right_num,' ')
        
    out.writelines(linelist)

out.close()

