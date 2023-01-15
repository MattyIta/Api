def partall(a: int, b: int) -> list:
    """Lag partall. Returner dem i en liste
    
    Examples:
        >>> partall(0,5)
        [0, 2, 4]
        >>> partall(1,10)
        [2, 4, 6, 8, 10]

    Args:
        a (int): Nedre grense (fra og med)

        b (int): Øvre grense (til og med)
    Returns:
        list: partall fra a til b
    """
    return [x for x in range(a, b+1) if x % 2 == 0]
