import re
from string_calculator_stringutils import StringParser

DEFAULT_DECIMAL_SEPARATOR = "."
ACCEPTED_DECIMAL_SEPARATORS = (".", ",")
SUPPORTED_OPERATORS = ("+", "-", "*", "/")

        
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
    def __init__(self, dec_separator:str=DEFAULT_DECIMAL_SEPARATOR):
        '''
        
        '''
        self.set_decimal_separator(dec_separator)
        self._previous_output = None
        self._string_parser = StringParser(self._dec_separator, SUPPORTED_OPERATORS)
        

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
        filler_line = None
    
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

    def _parse_input(self, input_string:str) -> tuple:
        '''
        Parse the input string and return the two numbers and the operator as a tuple.

        Args:
            input_string (str): the input string

        Returns:
            tuple: the two numbers and the operator
        '''
        return self._string_parser.parse(input_string, self._previous_output)

    def calculate(self, input_string:str) -> float:
        calc_output = self._execute_operation(*self._parse_input(input_string))
        self._previous_output = calc_output
        return calc_output


if __name__ == "__main__":
    calc = StringCalculator()
    print(f"Decimal separator: {calc._dec_separator}")

    
    while True:
        input_string = input("Enter an operation. Type . or , to set the new decimal separator: ")
        if input_string in ACCEPTED_DECIMAL_SEPARATORS:
            calc.set_decimal_separator(input_string)
            print(f"Decimal separator set to {input_string}")
            continue
        output = calc.calculate(input_string)
        print(f"Output: {output}")
