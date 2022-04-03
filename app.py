def string_calculator(numbers: str) -> int:
    """
        To calculate sum of numbers passed as a delimited string
        :numbers: delimited string of numbers
        :return: sum of numbers passed in delimited string
    """
    numbers = sanitize_delimited_string(numbers)
    if len(numbers) == 0:
        return 0

    return calculate_delimited_string_sum(numbers, ',')


def sanitize_delimited_string(string: str) -> str:
    """
        To clean the delimited string to only contain , as delimiter
        :string: delimited string of numbers
        :return: delimited string with only , as delimiter
    """
    delimiter = ','
    if string.startswith("//"):
        end_index = string.find('\n')
        delimiter = string[2:end_index]
        string = string[end_index+1:]

    return string.replace('\n', ',').replace(delimiter, ',').strip(',')


def calculate_delimited_string_sum(string: str, delimiter: str) -> int:
    """
        To calculate sum of a delimiter seperated string
        :string: string of numbers
        :delimiter: string to used as delimiter
        :return: sum of numbers passed in string
    """
    numbers = list(map(int, string.split(delimiter)))
    return sum(numbers)
