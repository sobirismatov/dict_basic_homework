def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    k=0 #harflar
    r=0 #raqamlar
    for i in txt:
        if i.isalpha():
            k+=1
        if i.isdigit():
            r+=1
    return { "LETTERS": k, "DIGITS": r}

print(count_all("salaom112"))