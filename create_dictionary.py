def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
 
    k=dict(zip(key,value))
    return k 
print(create_dictionary(["ism","yosh"],["kamron","24"]))