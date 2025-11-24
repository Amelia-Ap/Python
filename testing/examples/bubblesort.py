unsortiert = [6, 7, 3, 4, 5, 2, 7, 10]

def bubblesort(liste):
    # do it length of 'unsortiert' amount of times, so that even a fully reversed list gets sorted this way
    for j in range (len(unsortiert)):
        # compare pairs of numbers starting with first and second number
        # and going through 2nd and 3rd and so on
        for i in range(len(unsortiert) - 1):
            # for j in range(len(unsortiert) - 1):
            if liste[i] > liste[i + 1]:
                liste.insert(i, unsortiert[i + 1])
                liste.pop(i+2)
    print(liste)

print(unsortiert)
bubblesort(unsortiert)