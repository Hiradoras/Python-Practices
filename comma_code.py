animals = ['cat', 'dog', 'bird', 'mantis', 'fish']
emptyList = []


def commaCode(list):
    if len(list) == 0:
        print("List is empty")
    else:
        for i in range(0,len(list)):
            if i == len(list)-1:
                print('and', list[i])
            else:
                print(list[i], end = ", ")


commaCode(animals)
commaCode(emptyList)
