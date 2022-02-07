import sys

done = False
while not done:
    word_list = open("english3.txt", "r")

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    nonalphabet = []

    words = []

    words2 = []

    words3 = []

    words4 = []

    for word in word_list:
        words.append(word.strip())

    Input = False

    while not Input:
        try:
            anagram = input("Input your anagram: ").strip()
            if anagram.isalpha():
                Input = True
            else:
                print("Hm... just letters please. None of that stuff.")
                Input = False
        except ValueError:
            print("Hm... just letters please. None of that stuff.")
            Input = False




    anagramlen = len(anagram)
    unanagram_list = list(set(anagram))
    unanagram = ''.join(list(set(anagram)))

    try:
        anagram_position = int(words.index(anagram))
        print(anagram + " is already a word.\nHowever, it could also be an anagram for:")
    except ValueError as err:
        print("\nThat word seems to be jumbled. Those letters could be:")

    #NON LETTERS
    bad_letter = alphabet.pop()
    while bad_letter:
        failed = False
        for anagramletter in unanagram_list:
            if anagramletter == bad_letter:
                failed = True
                break
        if not failed:
            nonalphabet.append(bad_letter)
        if alphabet:
            bad_letter = alphabet.pop()
        else:
            break

    test_word = words.pop()
    while test_word:
        if len(test_word) == anagramlen:
            words2.append(test_word)
        if words:
            test_word = words.pop()
        else:
            break


    test_word2 = words2.pop()
    while test_word2:
        failed = False
        for letter in unanagram:
            if letter not in test_word2:
                failed = True
                break
        if not failed:
            words3.append(test_word2)
        if words2:
            test_word2 = words2.pop()
        else:
            break
    if words3:
        test_word3 = words3.pop()
        while test_word3:
            failed = False
            for letter2 in nonalphabet:
                if letter2 in test_word3:
                    failed = True
                    break
            if not failed:
                words4.append(test_word3)
            if words3:
                test_word3 = words3.pop()
            else:
                break

    if words4:
        for answer in words4:
            print(answer)
    else:
        print("\nHmm... something, something went wrong here\nLooks like there aren't any words that fit :/")

    word_list.close()

    Finished = input("Would you like to go again? [y] [n]")
    if Finished == "n":
        done = True
    elif Finished == "y":
        done = False
    else:
        print("That wasn't an option. Goodbye.")
        break


