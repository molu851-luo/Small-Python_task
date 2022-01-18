## author: luoqing
## data:20220119

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



