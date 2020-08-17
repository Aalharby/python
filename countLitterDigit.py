def main():
    sentence= input('Enter the text: ')
    litter_counter = 0
    digit_counter = 0
    space_counter = 0
    for i in range(len(sentence)):
        if sentence[i].isalpha():
           litter_counter += 1
           i+=1
        elif sentence[i].isdigit():
            digit_counter += 1
            i += 1
        elif sentence[i].isspace():
            space_counter+=1
            i+=1
        else:                                #this is to avoid punctuation
            i+=1
    print('number of litters in a sentance is: '+ str(litter_counter))
    print('number of digits in a sentance is: ' + str(digit_counter))
    print('number of spaces in a sentance is: ' + str(space_counter))
    print('length of sentance with spaces and punctuation: ' + str(len(sentence)))
    print('length of sentance with spaces: ' + str(litter_counter + digit_counter + space_counter))
    print('length of sentance without spaces: ' + str(litter_counter + digit_counter))



if __name__=='__main__':main()
