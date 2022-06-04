
from deck import *
from victories import Estate

if __name__ == "__main__":
    print("1. Demonstrate deck construction and draw.")
    rat = Deck("Lord Rattington")
    print("===========================================")
    print("Original deck:")
    print(rat)
    print("===========================================")
    print("After initial draw:")
    rat.drawHand()
    print(rat)
    input("\n(Press ENTER to continue.)")
    while len(rat.drawPile) > 0:
        print("After next draw:")
        rat.draw()
        print(rat)
        input("\n(Press ENTER to continue.)")

    print("\n\n")
    print("2. Calculate empirical probability of 3/4 vs. 2/5 initial split.")
    NUM_TRIALS = 100000
    two_fives = 0
    three_fours = 0
    for _ in range(NUM_TRIALS):
        deck = Deck("test")
        deck.drawHand()
        num_estates = sum([ type(x) is Estate for x in deck.hand ])
        if num_estates in [0,3]:
            two_fives += 1
        elif num_estates in [1,2]:
            three_fours += 1
        else:
            stop(f"WHOA! Got {num_estates} estates in initial draw.")
    print(f"There were {(two_fives/NUM_TRIALS*100):.1f}% 2/5 splits.")
