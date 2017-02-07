#!/usr/bin/env python

# Strings questions for game play 
easyQuiz = '''___1___ is the capital of Thailand. If you find yourself there you might end up partying on ___2___ road. 
Thailand is a constitutional ___3___ with a rich and colorful history. The Thai flag
is colored ___4___ , white, and blue. '''

mediumQuiz = '''A ___1___ is a type of Buddhist temple, before 1939 Thailand was called ___2___. ___3___ borders 
Thailand in the South. You'll want to make sure you have enough ___4___ during your stay to buy souvenirs. '''

hardQuiz = '''Mango and sticky rice is made of ___1___ milk and ___2___ rice, it's a favorite desert all over the country. Thai soups and curry
have a delicious ingredient know as Thai ginger but also knows locally as, ___3___ . You will be eating a lot of tasty food, remember to say ___4___ if you find it particularly delicious!'''

# Strings to search for in string questions 
question_number  = ["___1___", "___2___", "___3___", "___4___"]

# Strings that provide answer keys
answer_easy = ["bangkok", "khosan", "monarchy", "red"]
answer_medium = ["watt", "siam", "malaysia", "baht"]
answer_hard = ["condensed", "glutinous", "galangal", "aroy"]

# just prints out quiz based on what quizSelector assigns to variable quizLevel
def printQuiz(quizLevel):
    if quizLevel == "easy":
        return easyQuiz
    if quizLevel == "medium":
        return mediumQuiz
    if quizLevel == "hard":
        return hardQuiz

# find blanks that need to be replaced in the quiz string
def blankInQuizString(blank,question_number):
    for num in question_number:
        if num in blank:
            return num
    return None

#validates user imput for number of tires
def validNumbOfTries():
    while True:
        try:
        	number = int(raw_input("How many tries would you like?: "))
        	return abs(int(number))
        except ValueError:
            print "Not a valid response, please type a postive integer" 

# slects answer key
def answerKey(quizLevel):
	if quizLevel == "easy":
		return answer_easy
	if quizLevel == "medium":
		return answer_medium
	if quizLevel == "hard":
		return answer_hard
		
# Checks answer and keeps track of attempts as well as current question
# prints if you have won or lost
def CheckAnswer(quizLevel):
	replaced =[]
	quizString = printQuiz(quizLevel)
	quizString = quizString.split()
	currentQuestionIndex = 0
	numberOfAttempts = validNumbOfTries()
	print printQuiz(quizLevel)
	while numberOfAttempts > 0 and currentQuestionIndex <=3:
		blank = question_number[currentQuestionIndex]
		replacement = blankInQuizString(blank,question_number)
		userAnswer = raw_input("What should be substituted for: " + replacement + " ").lower()
		if userAnswer == answerKey(quizLevel)[currentQuestionIndex]:
			blank = blank.replace(replacement, userAnswer)
			replaced.append(blank)
			replaced =" ".join(replaced)
			print replaced
			currentQuestionIndex += 1
		else:
			numberOfAttempts -= 1
			print "Wrong answer, try again. You have " + str(numberOfAttempts) + " attempts left"
	else:
		if numberOfAttempts == 0:
			print "Game Over"
		else:
			print "You win!!!"


print """
  _____ _           _ _                 _    ___        _     _ 
 |_   _| |__   __ _(_) | __ _ _ __   __| |  / _ \ _   _(_)___| |
   | | | '_ \ / _` | | |/ _` | '_ \ / _` | | | | | | | | |_  / |
   | | | | | | (_| | | | (_| | | | | (_| | | |_| | |_| | |/ /|_|
   |_| |_| |_|\__,_|_|_|\__,_|_| |_|\__,_|  \__\_\\__,_|_/___(_)
                                                                """
#replaced = []

# user selects the quiz level they want to play, user input is converted to lowercase and if value isn't valid it cycles the function until valid

def quizSelector():
    quizLevel = raw_input("Please select game level by typing easy, medium, or hard: ").lower()
    while True:
        if quizLevel == "easy":
            return quizLevel
        if quizLevel == "medium":
            return quizLevel
        if quizLevel == "hard":
            return quizLevel
        else:
            print "Not a valid response, please try again" 
            return quizSelector()

quizLevel = quizSelector()

def playGame():
	#print printQuiz(quizLevel)
	#print list(answerKey(quizLevel))
	print CheckAnswer(quizLevel)

print playGame()


# Things to do:
# appending replacment word everytime user imput is correct


