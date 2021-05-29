#Student name : Daniel Fox
#COMP517 Assignment 3 - Cache Management

requests=[]
cache=[] #only holds 8 ints cause 1int =1 page
def main():

    cache.clear()
    requests.clear()

    print("\n*****************************************************************************************")
    print("*************************Cache Management System ****************************************")
    print("*****************************************************************************************\n")

    mainInput=input("Cache Management Options:\nEnter 1 for First In First Out (FIFO)\nEnter 2 for Least Frequently Used (LFU):\nEnter Input:")
    while mainInput not in ('1', '2','q','Q'):
        mainInput = input("\nInvalid Input!\nPlease Enter 1 or 2 or Q>> \n")
        
    if (mainInput=="1"):
        inputRequests()
        fifo()
    if (mainInput=="2"):
        inputRequests()
        lfu()
    if (mainInput=="q" or mainInput=='Q'):
        print("Ending program...")
        return 0


def inputRequests():
    print("Please enter reqested numbers for the cache system\nEnter Numbers: ")
    while True:
        elements=input()
        global requests
        if elements.isnumeric() or elements.lstrip('-').isnumeric():#if negatives are allowed inclide the "-"
            elements=int(elements)
            requests.append(elements)
        else:
            print("\nPlease try again and enter a valid number!\n")
        
        if elements==0:
            del requests[-1] #stops 0 being in list
            print("Loading cache management...")
            return 0

def fifo():
    global cache
    global requests

    print("\n*************First In First Out Cache Managment.*************\nPrinting reqests:")
    print (requests)

    print("\nSorting requests into cahce...")
    for i in requests:
        if not i in cache:
            print("Page Not present...")
            print("Miss: "+str(i)+"")
            cache.insert(0,i) #Moves the newest element to the start of list
        else:
            print("Page present...")
            print("Hit: "+str(i)+"")

        while len(cache)>8:
            print("Cache size greater than 8.Removing longest element from cache..\n", str(cache[-1]))
            del cache[-1] #removes longest standing element from list
            if len(cache)<=8:
                break

    print ("Printing cache..")        
    print(cache)
    print("Returning to Main..")
    return main()

def lfu():
    global cache
    global requests
    

    print("*************Least Frequently Used Cache*************\n")
    print ("Printing reqests:")
    print (requests)

    temp=[]#store last deleted variable incase it needs to be added back
    freq = {} 
    for i in requests:
        if i in freq.keys():
            #If seen,increase frequency by 1 
            freq[i] += 1
            print("Hit", i)
        else:
            #If not, set frequency to 1
            freq[i] = 1
            print("Miss", i)

        #if while loop changed to >=8 then it would delete extra value result in incorrect values sometimes
        while len(freq)>7:
            removeValue = min(freq,key=lambda k:(freq[k],k))
            temp=removeValue#to store last deleted value and insert later if needed
            print("Removing least frequent value:",removeValue)
            del freq[removeValue]
        
    cache=[int(x) for x in freq.keys()]#placing dictionary keys into list

    #Had a bug which didnt give the correct answer for certain conditions, had to include this and alter my while loop above
    if len(freq)==7 and len(requests)>=8:
        cache.insert(7,temp) #insert at the end of the list
    
    print ("\nPrinting cache..")
    print(cache)
    print("Returning to main..")
    return main()


if __name__ == '__main__':
    main()

