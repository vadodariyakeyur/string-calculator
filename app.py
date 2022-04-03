def string_calculator(numbers: str) -> int:
    """
        To calculate sum of numbers passed as a delimited string
        :numbers: delimited string of numbers
        :return: sum of numbers passed in delimited string
    """
    if len(numbers) == 0:
        return 0
    numbers = numbers.replace('\n', ',').strip(',')
    total = calculate_delimited_string_sum(numbers, ',') 
    return total

def calculate_delimited_string_sum(string: str, delimiter: str) -> int:
    """
        To calculate sum of a delimiter seperated string
        :string: string of numbers
        :delimiter: string to used as delimiter
        :return: sum of numbers passed in string
    """
    numbers = list(map(int, string.split(delimiter)))
    return sum(numbers)
