#Magic 8-Ball

#generating a random number
import random
random_number = random.randint(1, 13)
#print(random_number)

question = "Is there life in Mars?"
#print(question)
answer = ""
#print(answer)
name = ""
#print(name)
if len(name) == 0:
    print("Question:", question)
elif len(question) == 0:
    print("No question, no future")
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer:" + answer, end=' ')

if random_number == 1:
    print("Yes, definitely", answer)
elif random_number == 2:
    print("It is decidedly so", answer)
elif random_number == 3:
    print("Without a doubt", answer)
elif random_number == 4:
    print("Reply hazy, try again", answer)
elif random_number == 5:
    print("Ask again later", answer)
elif random_number == 6:
    print("Better not tell you know", answer)
elif random_number == 7:
    print("My sources say so", answer)
elif random_number == 8:
    print("Outlook not so good", answer)
elif random_number == 9:
    print("Very doubtful", answer)
elif random_number == 10:
    print("There is certainly a chance", answer)
elif random_number == 11:
    print("If I were you, I would be worried", answer)
elif random_number == 12:
    print("No such a thing", answer)
elif random_number == 13:
    print("Certainly there is a chance", answer)
else:
    print("Error")
