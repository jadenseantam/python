import random

def check_guess(guess, target):
    result = ""
    for i in range(guess_len):
        if guess[i] == target[i]:
            result += GREEN + guess[i] + RESET
        elif guess[i] in target:
            result += YELLOW + guess[i] + RESET
        else:
            result += RED + guess[i] + RESET
    return result



GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[31m"
RESET = "\033[0m"

guesses = 0
attempts = 8
targets = ["NORRIS", "PIASTRI", "LECLERC", "HAMILTON", "VERSTAPPEN", "TSUNODA", "ALONSO", "STROLL", "GASLY", "DOOHAN", "COLAPINTO", "OCON", "BEARMAN", "LAWSON", "HADJAR", "ALBON", "SAINZ", "BOTTAS", "ZHOU", "BORTOLETO", "HULKENBERG", "PEREZ", "RUSSEL", "MAZEPIN", "MAGNUSSEN", "ANTONELLI", "RAIKONNEN", "SCHUMACHER", "KYVAT", "RICCARDO", "VETTEL", "GROJEAN", "DEVRIES", "KUBICA", "GIOVENAZZI"]
# targets = [
#     "ABOUT", "ABOVE", "AFTER", "AGREE", "ALWAYS", "ANOTHER", "BEFORE", "BEHIND", "BETTER", "BOTH",
#     "BRIGHT", "CANDLE", "CHANGE", "CHARGE", "COMMON", "COMPLETE", "CONDITION", "CONTROL", "DECIDE", "DEEPER",
#     "DESIGN", "DESIRE", "DIFFER", "DURING", "EFFECT", "ENCOURAGE", "EXAMPLE", "EXPLAIN", "FEEDBACK", "FEELING",
#     "FORWARD", "FRIENDS", "FUTURE", "HEALTHY", "IMAGINE", "IMPROVE", "INCLUDE", "INSIGHT", "INTEREST", "INVOLVE",
#     "JOURNEY", "LEADER", "LEARNING", "LENGTHY", "LIBRARY", "NATURAL", "NECESSARY", "OFFERING", "OPENING", "OUTCOME",
#     "OVERCOME", "PARTNER", "PERFECT", "POSSIBLE", "PROBLEM", "PROCESS", "PROGRESS", "RECEIVE", "RESEARCH", "RESULTS",
#     "SIMPLE", "SOLUTION", "SPEAKING", "STRATEGY", "STUDIES", "SUCCESS", "SUPPORT", "THOUGHT", "TOGETHER", "TRADITION",
#     "UNIQUE", "VARIOUS", "VICTORY", "WANTING", "WATERED", "WONDER", "YESTERDAY", "ACCEPT", "ACHIEVE", "ADJUST",
#     "ANALYZE", "ATTEMPT", "BALANCE", "BECAUSE", "BEFORE", "CAPTURE", "CHALLENGE", "COMMITMENT", "CONCEPT", "CRITICAL",
#     "DEVELOP", "DIFFICULT", "EFFECTIVE", "ENCOURAGE", "EQUIPMENT", "EXCITING", "EXPERIENCE", "FOCUSING", "FORMALLY",
#     "FREEDOM", "GENERATE", "IMMEDIATE", "IMPROVEMENT", "INFLUENCE", "INVESTMENT", "MAINTAIN", "MATERIALS", "NATIONAL",
#     "OBVIOUS", "PERSPECTIVE", "PREDICT", "PROFICIENT", "RECOGNIZE", "RELATIONSHIP", "SCHEDULE", "SIGNIFICANT", "SPIRITUAL",
#     "STRATEGIC", "SUGGESTION", "TECHNOLOGY", "TRANSITION", "ULTIMATE", "VALIDATE", "WILLINGNESS", "APPROACH", "AWARENESS",
#     "COLLECTIVE", "CONNECTION", "CONTRIBUTE", "CULTURAL", "DEVELOPMENT", "DIRECTION", "ELECTRIC", "EXPRESSION", "FUNDAMENTAL",
#     "GENERALLY", "HAPPINESS", "IMPARTING", "INCREASING", "INTEGRATE", "INTERACTION", "INVESTIGATE", "MANAGEMENT", "MENTALITY",
#     "NEGATIVE", "OBJECTIVE", "PARTICIPATE", "PATTERNED", "PREPARATION", "PREVIOUSLY", "PROFESSIONAL", "RECEIVING", "RELATIVE"
# ]
target = random.choice(targets).upper().strip()
print("Guess the word: ")

while True:
    guess = input().strip().upper()

    guess_len = len(guess)

    if guess_len > len(target):
        print("Your word contains too many letters!")
    elif guess_len < len(target):
        print("Your word contains too few letters!")
    else:
        result = check_guess(guess, target)
        print(result)
    
        if guess == target:
            print(f"You have guessed the word!\n\n")
            print("Press enter to play again...")
            guess = input().strip().upper()
            print("Guess the word: ")
            attempts = 10
            target = random.choice(targets).upper().strip()
    
    attempts -= 1
    print(f"You have {attempts} attempts left!")

    if attempts == 0:
        print("You lose!") 
        print(f"The word is {target}")
        print("Press enter to play again...")
        guess = input().strip().upper()
        print("Guess the word: ")
        target = random.choice(targets).upper().strip()
        attempts = 10