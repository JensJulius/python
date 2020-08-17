
#	https://www.wikihow.com/Play-Mastermind

#	Code maker creates code (Three - six  (four) spots, Three - six  (four) colors.
#	- More than one of each color can be used
targetList = []

def createSequence(s1, s2, s3, s4):
	targetList = [s1, s2, s3, s4]

createSequence("red", "blue", "green", "blue")
print(targetList)
#	Code breaker makes first guess

# def

#	Code maker gives hints to correctness.
#	- White peg for correct color, but wrong spot
#	- Black peg for correct color correct spot
#	- Order of pegs can be random

#	Loop until max guesses have been reached or the original code has been guessed
