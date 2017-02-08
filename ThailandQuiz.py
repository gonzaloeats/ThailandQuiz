#!/usr/bin/env python

# String questions for game play 
easyQuiz = '''___1___ is the capital of Thailand. If you find yourself there you might end up partying on ___2___ road. 
Thailand is a constitutional ___3___ with a rich and colorful history. The Thai flag
is colored ___4___ , white, and blue. '''

mediumQuiz = '''A ___1___ is a type of Buddhist temple, before 1939 Thailand was called ___2___. ___3___ borders 
Thailand in the South. You'll want to make sure you have enough ___4___ during your stay to buy souvenirs. '''

hardQuiz = '''Mango and sticky rice is made of ___1___ milk and ___2___ rice, it's a favorite desert all over the country. Thai soups and curry
have a delicious ingredient know as Thai ginger but also knows locally as, ___3___ . You will be eating a lot of tasty food, remember to say ___4___ if you find it particularly delicious!'''

# Strings to search for in string questions 
question_number  = ["___1___", "___2___", "___3___", "___4___"]

# Strings for answer keys
answer_easy = ["bangkok", "khosan", "monarchy", "red"]
answer_medium = ["watt", "siam", "malaysia", "baht"]
answer_hard = ["condensed", "glutinous", "galangal", "aroy"]

# prints out quiz based on what quizSelector assigns to variable quizLevel
def printQuiz(quizLevel):
    if quizLevel == "easy":
        return easyQuiz
    if quizLevel == "medium":
        return mediumQuiz
    if quizLevel == "hard":
        return hardQuiz                                       

#validates user imput for number of tires
def validNumbOfTries():
    while True:
        try:
        	number = int(raw_input("How many attempts would you like?: "))
        	if number < 0:
        		print "Sorry, you must provide a postive number, try again"
        		continue
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
# prints quiz with you current correct answers
# prints if you have won or lost
def playGame(quizLevel):
    replaced =[]
    quizString = printQuiz(quizLevel)
    replaced = quizString
    currentQuestionIndex = 0
    numberOfAttempts = validNumbOfTries()
    print printQuiz(quizLevel)
    while numberOfAttempts > 0 and currentQuestionIndex <=3:
        replacement = question_number[currentQuestionIndex]
        userAnswer = raw_input("\nWhat should be substituted for: " + replacement + " ").lower()
        if userAnswer == answerKey(quizLevel)[currentQuestionIndex]:
            quizString = quizString.replace(replacement,userAnswer)
            print "\n" + quizString
            currentQuestionIndex += 1
        else:
            numberOfAttempts -= 1
            print "\nWrong answer, try again. You have " + str(numberOfAttempts) + " attempts left"
            print "\n" + quizString
    else:
        if numberOfAttempts == 0:
            return "\nGame Over"
        else:
            return "\nYou Won!!!"


print """
  _____ _           _ _                 _    ___        _     _ 
 |_   _| |__   __ _(_) | __ _ _ __   __| |  / _ \ _   _(_)___| |
   | | | '_ \ / _` | | |/ _` | '_ \ / _` | | | | | | | | |_  / |
   | | | | | | (_| | | | (_| | | | | (_| | | |_| | |_| | |/ /|_|
   |_| |_| |_|\__,_|_|_|\__,_|_| |_|\__,_|  \__\_\\__,_|_/___(_)
                                                                """

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
	
print playGame(quizLevel)