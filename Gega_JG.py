def list_elements() :

    while True :

        numb=input('Please enter number of elements for the list :')

        if not numb.isdigit() :

            print('\nOnly numbers !\n')

            continue 

        numb=int(numb)

        if numb < 2 or numb > 20 :

            print('\nPlease enter between 1 ans 20\n')

            continue 
        else :

            list_generator(numb)

            break


def list_generator(a) :
    
    
    list_1=[]

    for i in range(a) :

        list_1.append(input(f"Enter {i+1} element :"))

    print('List is generated :',list_1)


list_elements()