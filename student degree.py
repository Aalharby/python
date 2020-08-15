def main():
    mark1= input('Enter your mark ')
    degree=int(mark1)
    if degree<60:
        print('F')
    elif degree<65:
        print('D')
    elif degree<70:
        print('D+')
    elif degree<75:
        print('C')
    elif degree<80:
        print('C+')
    elif degree<85:
        print('B')
    elif degree<90:
        print('B+')
    elif degree<95:
        print('A')
    else: print('A+')

if __name__ == '__main__':main()
