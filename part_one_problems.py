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











