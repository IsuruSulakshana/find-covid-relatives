list = []
newList = []

def createData():
	file1 = open('data.txt', 'r')
	while True:
		line = file1.readline()
		if not line:
			break
		list.append(line.strip())
	file1.close()
	return convertData(list)

def convertData(list):
	global newList
	for i in list:
		newList.append([int(i[0:10]),int(i[11:21]),int(i[22:24])])
	return newList

if __name__ == '__main__':
	createData()
 
