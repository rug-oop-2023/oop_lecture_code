import re

DEFAULT_DECIMAL_SEPARATOR = "."
SUPPORTED_OPERATORS = ["+", "-", "*", "/"]

class StringCalculator:
    '''
    A simple calculator that takes a string as input and returns a float as output.
    The input string must be of the form "123.456 + 456.789" (or "123,456 + 456,789"
    depending on the current decimal separator).
    The operator must be separated from the numbers by means of whitespaces.
    The number is allowed to be negative.
    The number can be an integer (e.g. "123").
    A float must always have an integer part (so, "0.456" is allowed, but
    ".456" is not).
    The operator can be one of the following: "+", "-", "*", "/"
    
    The calculator can be instantiated with a custom decimal separator.
    The default separator is ".".

    Example:
        >>> calc = StringCalculator()
        >>> calc.calculate("1 + 2")
        3.0
        >>> calc.calculate("1.5 + 2.5")
        4.0
        >>> calc.set_decimal_separator(",")
        >>> calc.calculate("1,5 + 2,5")
        4.0
        >>> calc.calculate("1.5 + 2,5") # inconsistent decimal separators
        ValueError: Invalid number string '1.5'
        >>> calc.calculate("1,5 + 2.5") # inconsistent decimal separators
        ValueError: Invalid number string '2.5'
        >>> calc.calculate("1,5 + 2,5")
        4.0
        >>> calc.calculate("1,5 + 2,5 + 3,5")
        ValueError: Invalid input string '1,5 + 2,5 + 3,5': expected 3 groups, got 5
    '''
    def __init__(self, dec_separator:str = DEFAULT_DECIMAL_SEPARATOR):
        '''
        
        '''
        self.set_decimal_separator(dec_separator)
        self._previous_output = None

    def _validate_decimal_separator(self, dec_separator:str) -> bool:
        '''
        Check if the decimal separator is valid.
        Currently, only "." and "," are valid separators.

        Args:
            dec_separator (str): the decimal separator to check
        '''
        return dec_separator in [".", ","]
        
    def set_decimal_separator(self, dec_separator:str) -> None:
        '''
        Set the decimal separator for the calculator.
        If the separator is invalid, the default separator will be used instead.
        It also adapts the number regex to the new separator.

        Args:
            dec_separator (str): the decimal separator to use
        '''
        if self._validate_decimal_separator(dec_separator):
            self._dec_separator = dec_separator
        else:
            self._dec_separator = DEFAULT_DECIMAL_SEPARATOR
            print(f"Invalid decimal separator. Using default separator: {DEFAULT_DECIMAL_SEPARATOR}")
        self._number_regex = re.compile(rf"^(-?\d+){re.escape(self._dec_separator)}?(\d*)$")
        
    def _parse_number(self, number_string:str) -> float:
        '''
        Converts a string of the form "123.456" (or "123,456"
        depending on the current decimal separator) to a float.
        The number is allowed to be negative.
        The number can be an integer (e.g. "123").
        A float must always have an integer part (so, "0.456" is allowed, but
        ".456" is not).
        This rule is enforced by the following regex:
        ^(-?\d+)§?(\d*)$
        Where § is a placeholder for the decimal separator.
        The regex check is skipped if the number string is "ans", in which case
        the previous output is returned.

        Args:
            number_string (str): the number string to convert

        Returns:
            float: the converted number

        Raises:
            ValueError: if the number string is not valid
        '''
        if number_string.lower() == "ans":
            return self._previous_output

        regex_match = self._number_regex.match(number_string)
        if not regex_match:
            raise ValueError(f"Invalid number string '{number_string}'")
        integer_part = regex_match.group(1)
        decimal_part = regex_match.group(2)
        if decimal_part == "":
            return float(integer_part)
        return float(f"{integer_part}.{decimal_part}")


    def _parse_input(self, input_string:str) -> list:
        '''
        Main input parser.
        It takes a string of the form "123.456 + 456.789" and 
        converts it to a list of the form [123.456, "+", 456.789].
        The number format is the same as in _parse_number().
        The operator can be one of the following: "+", "-", "*", "/"
        The input string is first stripped of all leading and trailing whitespaces.
        Then, all intermediate whitespaces are replaced by a single whitespace.
        Finally, the string is split by the intermediate whitespaces.
        
        Args:
            input_string (str): the input string to parse
        
        Returns:
            list: the parsed input string as a list of numbers and operators
        
        Raises:
            ValueError: if the input string is not valid
        '''
        # remove all leading and trailing whitespaces (useless for computation)
        input_string = input_string.strip()
        # remove duplicate whitespaces
        input_string = re.sub(r" +", " ", input_string)
        # split input string by intermediate whitespaces
        input_groups = input_string.split(" ")
        print(input_groups)
        # group 0 and 2 should be numbers, group 1 should be an operator
        if len(input_groups) != 3:
            raise ValueError(f"Invalid input string '{input_string}': expected 3 groups, got {len(input_groups)}")
        if input_groups[1] not in SUPPORTED_OPERATORS:
            raise ValueError(f"Invalid operator '{input_groups[1]}'")
        return [self._parse_number(input_groups[0]), input_groups[1], self._parse_number(input_groups[2])]
    
    def _execute_operation(self, number1:float, operator:str, number2:float) -> float:
        '''
        Execute an operation on two numbers.
        The operator can be one of the following: "+", "-", "*", "/"

        Args:
            number1 (float): the first number
            operator (str): the operator
            number2 (float): the second number
        
        Returns:
            float: the result of the operation
        '''
        if operator == "+":
            return number1 + number2
        if operator == "-":
            return number1 - number2
        if operator == "*":
            return number1 * number2
        return number1 / number2

    def get_previous_output(self) -> float:
        '''
        Get the previous output.

        Returns:
            float: the previous output
        '''
        return self._previous_output

    def calculate(self, input_string:str) -> float:
        calc_output = self._execute_operation(*self._parse_input(input_string))
        self._previous_output = calc_output
        return calc_output


if __name__ == "__main__":
    calc = StringCalculator()
  
    
    while True:
        input_string = input("Enter an operation: ")
        output = calc.calculate(input_string)
        print(f"Output: {output}")
