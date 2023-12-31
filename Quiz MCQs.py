questions = ("How many elements are in the periodic table?: ",
                "Which animal lays the largest eggs?: ",
                "What is the most abundant gas in Earth's atmosphere?: ",
                "How many bones are in the human body?: ",
                "Which planet in the solar system is the hottest?: ",
                )

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                ("A. 206", "B. 207", "C. 208", "D. 209"),
                ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
                )

score = 0

question_num = 0

guesses = []

answers = ("C", "D", "A", "A", "B")

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Please enter the correct options(A,B,C,D) :").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
        
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is a correct answer")
    question_num += 1

print("")

print('Answer :',end=' ')
for answer in answers:
    print(answer,end=' ')

print("")

print("Guesses :",end=' ')
for guess in guesses:
    print(guess,end=' ')


print("")
print("**********************")
print("RESULT")
print("**********************")
print("The total score is "+str(score)+" out of 5 questions")
print("The total percentage is "+str(int(score/5*100))+"%")


    
















