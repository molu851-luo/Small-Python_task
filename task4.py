## author: luoqing
## data:20220119

##命令行参数
import sys, getopt
def main(argv):
    inputfile=''
    outputfile=''
    try:
        opts,args=getopt.getopt(argv,"hi:o",['ifile=','ofile='])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])

##读入文件
with open('rmsd.xvg','r') as fo:
    lines=fo.readlines()

##处理文件
xaxis,yaxis="",""
time_list,rmsd_list=[],[]

##去掉空行
lines=[line for line in lines if len(line) !=0]

for line in lines:
    if line[0]=='#':
        continue
    
    if line [0]=='@':
        if 'xaxis' in line:
            xaxis=line.strip().strip('"').split('"')[-1]
        if 'yaxis' in line:
            yaxis=line.strip().strip('"').split('"')[-1]
    if not line.startswith('@') and not line.startswith('#'):
        items=line.strip().split()
        time_list.append(float(items[0]))
        rmsd_list.append(float(items[1]))

##检查time_list,rmsd_list长度
if len(time_list) !=len(rmsd_list):
    print('wrong in length of time_list')
    exit()
print(len(time_list),len(rmsd_list))

##保存CSV文件
print(xaxis,yaxis)
with open('rmsd.csv','w') as fo:
        fo.write(xaxis+","+yaxis+"\n")
        for i in range(len(time_list)):
            fo.write("{},{}\n".format(time_list[i],rmsd_list[i]))

import matplotlib.pyplot as plt

##read csv file
with open('rmsd.csv','r') as fo:
    lines=fo.readlines()

##deal with data
xname,yname=lines[0].split(",")[0],lines[0].split(",")[1].strip()
time_list,rmsd_list=[],[]
for line in lines[1:]:
    iterms=line.strip().split(",")
    time_list.append(float(iterms[0].strip()))
    rmsd_list.append(float(iterms[1].strip()))

time_list=[t/1000 for t in time_list]

##plot time vs rmsd
plt.plot(time_list,rmsd_list)
plt.xlabel("Time (ns)")
plt.ylabel(yname)
plt.savefig('./task4.png')
plt.show()
print('good day!')


