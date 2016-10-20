while True:
    answer = raw_input("If you can guess my secret number, you'll escape this limbo. Number is:")
    if answer == "13":
        print ("Yes, YES, YEEEEEEEEEEEEEES. You're free!")
        break

    if answer == "14" or "12":
        print ("It makes me anxious on how close you were right now!")
    
    else:
        print ("Guess again, not even close!")

    print("There is no escaping this madness without guessing my number.")
    
