import random

word_list = ["add", "after", "again", "any", "apple", "arm", "banana", "bark", "been", "being", "bent", "best", "bone", "black", "block", "blue", "bring", "brown", "bush", "came", "cane", "card", "cart", "case", "chain", "chair", "chalk", "chat", "chin", "chop", "clam", "clan", "clap", "claw", "clay", "clean", "cool", "dark", "desk", "drop", "end", "family", "fang", "fast", "fell", "few", "fill", "flag", "flat", "fool", "foot", "fort", "free", "fresh", "from","glad", "golf", "gone", "grit", "hand", "hang", "happy", "harm", "help", "here", "hide", "hill", "hint", "hope", "horn", "how", "ill", "into", "jaw", "joke", "just", "keep", "king", "last", "line", "look", "luck", "made", "many", "meal", "must", "nice", "new", "next", "odd", "put", "quit", "rang", "space", "said", "time", "was", "yard", "yarn", "baseball", "brother", "clover", "cloud", "crayon", "club", "coat", "come", "cookie", "could", "crow", "cube", "cupcake", "deal", "dew", "dime", "dine", "dirt", "doll", "door", "draw", "dream", "dress", "drink", "dull", "each", "east", "easy", "eight", "eleven", "every", "father", "field", "fine", "first", "flew", "flower", "friend", "globe", "going", "grape", "grass", "grew", "heavy", "know", "marker", "maybe", "milk", "morning", "mother", "myself", "much", "never", "notebook", "other", "over", "paper", "pencil", "pretty", "rabbit", "school", "seven", "sew", "shirt", "sister", "smell", "stray", "string", "summer", "start", "swing", "table", "thank", "thrift", "twelve", "twist", "under", "very", "water", "were", "where", "yellow", "zebra", "zero", "always", "animal", "around", "because", "before", "believe", "between", "bread", "bright", "busy", "cannot", "caught", "charge", "clapped", "clean", "chicken", "children", "doctor", "does", "goes", "everyone", "everywhere", "flight", "inside", "juice", "kitchen", "laughter", "nobody", "once", "orange", "outside", "piece", "purple", "raise", "round", "shoes", "today", "used", "weak", "week", "whale", "which", "while", "wool", "yesterday"]
# Source: https://www.kidspot.com.au/school/preschool/preschool-literacy/spelling-bee-words-78/news-story/a8744b66729527eb1c5a957b4dc0fcf6

def hangman(word):
    wrong = 0
    stages =    ["",
                "_______       ",
                "|             ",
                "|       |     ",
                "|       0     ",
                "|      /|\    ",
                "|      / \    ",
                "|             "
                ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman!")
    print(board)

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                    .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
             .join(stages[0: \
                wrong]))
        print("You lose! It was {}."
            .format(word))

hangman(word_list[random.randint(0, len(word_list))])
