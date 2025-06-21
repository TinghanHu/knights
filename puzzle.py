from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    #Knight or Knave can't be both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)), 
    #if A is Knight then A is true
    Implication(AKnight, And(AKnight, AKnave)),
    #if A is Knave then A is lying
    Implication(AKnave, Not(And(AKnight, AKnave)))
    )

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #Knight or Knave can't be both
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    #Knight or Knave can't be both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    #if A is Knight then A is true
    Implication(AKnight, And(AKnave, BKnave)),
    #if A is Knave then A is not true
    Implication(AKnave, And(Not(AKnave, BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    #Knight or Knave can't be both
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    #Knight or Knave can't be both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    #if A is Knight then A is true
    Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    #if A is Knave then A is not true
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    #if B is Knight then B is true            
    Implication(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    #if B is Knave then B is not true  
    Implication(BKnave, Not(Or(And(AKnave, BKnight), And(AKnight, BKnave)))),        

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #Knight or Knave can't be both
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    #Knight or Knave can't be both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    #Knight or Knave can't be both
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave,  Not(Or(AKnight, AKnave))),
    #if A said A is Knight
    Implication(AKnight, AKnight),
    Implication(AKnave, Not(AKnight)),
    #if A said A is Knave
    Implication(AKnight, AKnave),
    Implication(AKnave, Not(AKnave)),
    Or(
        #if A said A is Knight
        And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight))), 
         #if A said A is Knave
        And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))  
    ),
    #if B is Knight A is Knave
    Implication(BKnight, And(AKnave, CKnave)),
    #if B is Knave A is not Knave
    Implication(BKnave, Not(And(AKnave, CKnave)),
    #if C is Knight A is Knave
    Implication(CKnight, AKnight),          
    #if C is Knight A is  not Knave   
    Implication(CKnave , Not(AKnight))        
    )            


)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
