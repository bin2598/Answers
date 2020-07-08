
list = []

def find_duplicates():

    for i in range(100):
        l = []
        l.append(i)
        for j in range(100):
            filei = open(f"{i}.txt",'r')
            filej = open(f"{j}.txt","r")
            if filei.read() == filej.read():
                l.append(j)
        list.append(l)

if __name__ == '__main__':
    find_duplicates()
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j],end=" ")
        print()