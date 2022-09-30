print("hello, world", 4)
print(type(3.5))

def vowel_count(s) : 
    count = 0
    vowel = "aeiou"
    for l in s :
        if l in vowel:
            count += 1

    return count

vowel_count("caenncniewwx")

vowel = "aeiou"
s="bobjojbobkjskbob"
count = 0
bob = "bob"
for l in s :
    if l in vowel:
        count += 1

print("Number of vowels:", count)  


s = "bobcencebobsknw"
i = 0
count = 0

for letter in s:
    if str[i:i+3] == "bob":
        count += 1
        print("hshs")
    i += 1
    
print("Number of times bob occurs is: ", count)

s = "gcncnoencoocnwow"
alph = ""
j=0
thislist=[]

for letter in s:
    alph=""
    print(letter, "letter")
    for i in range(j,len(s)-1):
        # print(len(s), s[i], i,s[i+1], "first loop", alph)

        if ord(s[i]) <= ord(s[i+1]):
            if i ==j:
                alph += s[i]
                
            alph += s[i+1]
            if i == len(s)-2 :
                thislist.append(alph)
                j+=1

                

        else: 
            if alph:
                thislist.append(alph)
            j+=1
            break
            
print(thislist)        

if len(thislist)==0:
    print("Longest substring in alphabetical order is: ", s[0])
else:
    print("Longest substring in alphabetical order is: ", max(thislist, key=len))





x = 23
epsilon = 0.1
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        print(guess)
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))


# Bisection Search, Guess My Number


max = 100
min = 0
success = False
print("Please think of a number between 0 and 100!")


while not success:
    guess = (max + min)//2
    print("Is your secret number", guess, "?")  
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response=='h': 
        max = guess
    elif response == "l":
        min = guess
    elif response == "c":
        success= True
    else: 
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ', guess)


def iterPower(base, exp):
    result = 1
    if exp == 0:
        return result

    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    for i in range(1, exp+1):
        result = result * base
    return result
    
print(iterPower(2,4))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base*recurPower(base, exp-1)

print(iterPower(2,4))

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare, i):
    # print(i, n, "at the top")
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to, 2)
        # print("in second place", i, n)
        Towers(1, fr, to, spare,i)
        
        Towers(n-1, spare, to, fr, 3)

# Examples of calling Towers()
# Towers(1, 'f', 't', 's')
# Towers(2, 'f', 't', 's')
Towers(4, 'f', 't', 's', 0)



def gcdIter(a, b):


    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    for i in range(max(a,b), 0, -1):
        if a % i == 0 and b% i ==0:
            return i


print(gcdIter(17, 3))

print(180%36)

def gcdRecur(a, b):
    print(a,b)
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)



print(gcdRecur(36, 180))






print(5//2)

def isIn(char, aStr):
    middle = len(aStr)//2
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    if char == aStr[middle]:
        return True
    if char > aStr[middle]:
        return isIn(char, aStr[middle+1:])
    else: 
        return isIn(char, aStr[:middle])


print(isIn('f', 'bdffiimrt'))
    

