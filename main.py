from time import *
import random

def mistake(conttext, usertext):
    error = 0
    for i in range(len(conttext)):
        try:
            if conttext[i] != usertext[i]:
                error = error + 1
        except :
            error = error
    return error

def speed_check(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_round = round(time_delay, 2)
    speed = len(user_input)/time_round
    return round(speed)


text = ['I am a programmer and i choose first languege as python',
'my name is vikas i lived in mohan garden new delhi',
'i am in collage right now in 1st year']

text2 = random.choice(text)
print("***** Type this para ******")
print()
print(text2)
print()
time_1 = time()
text_input = input("Enter : ")
time_2 = time()

print("Speed : ", speed_check(time_1, time_2, text_input))
print("Error : ", mistake(text2, text_input))