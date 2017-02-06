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




# user selects the quiz level they want to play, user input is converted to lowercase and if value isn't valid it cycles the function until valid

# quizLevel = raw_input("Please select game level by typing easy, medium, or hard: ").lower()
# while True:
#         if quizLevel == "easy":
#             return quizLevel
#         if quizLevel == "medium":
#             return quizLevel
#         if quizLevel == "hard":
#             return quizLevel
#         else:
#             print "Not a valid response, please try again" 
#             return quizSelector()

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

# slects answer key
def answerKey(quizLevel):
	if quizLevel == "easy":
		return answer_easy
	if quizLevel == "medium":
		return answer_medium
	if quizLevel == "hard":
		return answer_hard
		
# Checks answer and keeps track of attempts as well as current question
# then print if you have won or lost
def CheckAnswer(answerKey):
	# replaced =[]
	# quizString = quizString.split()
	currentQuestionIndex = 0
	numberOfAttempts = 3
	while numberOfAttempts > 0 and currentQuestionIndex <=3:
		print printQuiz(quizLevel)
		blank = question_number[currentQuestionIndex]
		replacement = blankInQuizString(blank,question_number)
		userAnswer = raw_input("What should be substituted for: " + replacement + " ")
		if userAnswer == answer_easy[currentQuestionIndex]:
			blank = blank.replace(replacement, userAnswer)
			# replaced.append(blank)
			# replaced =" ".join(replaced)
			# print replaced
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
replaced = []
quizLevel = raw_input("Please select game level by typing easy, medium, or hard: ").lower()
# while True:
#         if quizLevel == "easy":
#             return quizLevel
#         if quizLevel == "medium":
#             return quizLevel
#         if quizLevel == "hard":
#             return quizLevel
#         else:
#             print "Not a valid response, please try again" 
#             return quizSelector()
	# quizString = printQuiz(quizSelector())
	# #quizString = printQuiz(quizSelector())
	# print quizString
	# quizString = quizString.split()
	# CheckAnswer(answerKey)
	# for blank in quizString:
	# # 	replacement = blankInQuizString(blank,question_number)
	# #	if replacement != None:
	# # 		user_input = raw_input("What should be substituted for: " + replacement + " ")
	# 		blank = blank.replace(replacement, user_input)
	# 		replaced.append(blank)
	# 	else:
	# 		replaced.append(blank)
	# replaced = " ".join(replaced)
	# return replaced
	#correctAnswer = 0
	# while correctAnswer >5:
	# 	if#print the question to user and ask for answer:
	# 		return #fill in the blank
	# 	else:
	# 		print "You win!!!!!!!!"

def playGame():
	print printQuiz(quizLevel)
	print answerKey(quizLevel)
	print CheckAnswer(quizLevel)

print playGame()



## setting quizLevel as a golbal variable helped tremendously 
#all that is left is creating an answer key basked on quizLevel
#also appending the replacment work everytime user imput is correct
