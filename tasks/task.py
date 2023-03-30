from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    new_numbers = []
    for i in sequence:
        try:
            if i == int(i):
                new_numbers.append(i)
        except TypeError:
                new_numbers += linear_seq(i)
    return new_numbers






