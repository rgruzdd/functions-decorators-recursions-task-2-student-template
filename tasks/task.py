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
            for k in i:
                try:
                    if k == int(k):
                        new_numbers.append(k)
                except TypeError:
                    for f in k:
                        new_numbers.append(f)
    return new_numbers

sequence = [1,2,3,[4,5, (6,7)]]
print(linear_seq(sequence))


