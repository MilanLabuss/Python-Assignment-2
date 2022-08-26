#Milan Labus SD2 04/04/2022

def converge(val):
        while val > 1:    #keep looping while the value is greater than 1
            print(int(val))
            if (val%2) == 0:  #if the remainder is zero
                val = val/2
            else:               #else the remainder is not zero
                val = 3*val +1
        print (1)  #if we have exited the while loop its because we have a value of 1

while True:
    try:
        val = int(input("Please enter a number: "))
        break
    except:
        print("Error please enter a whole number")



converge(val)
