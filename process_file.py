import output_file
import input_file
 
newList = input_file.createData()
n = input()
x = int(n[0:10])
lst = []
#date = 0

for i in newList:
    if x in i:
        date = i[2]
for i in range(len(newList)):
    if date <= newList[i][2]:
            lst.append([newList[i][0],newList[i][1]])
            
outputList = []

def process(x,list):
    size = len(list)
    if size == 0:
        return
    else:
        for i in list:
            if x in i:
              i.remove(x)
              a = i[0]
              outputList.append(str(a)+'\n')
              lst.remove(i)
              process(x,lst)
              process(i[0],lst)

process(x,lst)
output_file.report(outputList)
