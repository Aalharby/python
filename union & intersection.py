def main():
    long= int(input('what is the size of first set:\n '))
    list1= list()

    for i in range(long):
        print('enter '+str(i+1) +' of first set of element: ')
        ele=input()
        list1.append(ele)
    set1= set(list1)

    long2 = int(input('what is the size of second set:\n '))
    list2= list()
    for i in range(long2):
        print('enter ' + str(i + 1) + ' of second set of element: ')
        ele2=input()
        list2.append(ele2)
    set2= set(list2)

    print('\nthe intersection of the two sets is: '+str(set1.intersection(set2)))
    print('\nthe union of the two sets is: '+str(set1.union(set2)))

if __name__ == '__main__':main()
