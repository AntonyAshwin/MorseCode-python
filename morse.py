import winsound

# winsound is imported to produce a sine wave
# Here, di is the duration of dot and da is the duration of dash (in milliseconds)

di = 300
da = 700

# each character has been redefined in terms of duration of dots and dashes 

code = {
'a' : [di,da],
'b' : [da,di,di,di],
'c' : [da,di,da,di],
'd' : [da,di,di],
'e' : [di],
'f' : [di,di,da,di],
'g' : [da,da,di],
'h' : [di,di,di,di],
'i' : [di,di],
'j' : [di,da,da,da],
'k' : [da,di,da],
'l' : [di,da,di,di],
'm' : [da,da],
'n' : [da,di],
'o' : [da,da,da],
'p' : [di,da,da,di],
'q' : [da,da,di,da],
'r' : [di,da,di],
's' : [di,di,di],
't' : [da],
'u' : [di,di,da],
'v' : [di,di,di,da],
'w' : [di,da,da],
'x' : [da,di,di,da],
'y' : [da,di,da,da],
'z' : [da,da,di,di]
}



a = input("Enter your string with no numbers  ").lower()

words = a.split()

#first for loop selects a word from a paragraph - 53
#second for loop selects the letter from the word - 54
#letter is then replaced with the durations from the dictionary above - 55
#third for loop plays the sine wave for the duration assigned and repeats 
#it till all the durations of the letter are complete -57
#i have assigned a sine wave with 37hz (barely audible) for 1200 milliseconds once a word is complete to give a space - 58

for word in words:
    for letter in word:
        sound = code.get(letter,letter)
        for i in range(0,len(sound)):
            winsound.Beep(440,sound[i])
        winsound.Beep(37,1200)
