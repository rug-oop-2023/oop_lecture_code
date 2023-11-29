import re
from string_calculator_stringutils import StringParser

DEFAULT_DECIMAL_SEPARATOR = "."
ACCEPTED_DECIMAL_SEPARATORS = (".", ",")
SUPPORTED_OPERATORS = ("+", "-", "*", "/")

        
class StringCalculator:
    def __init__(self, dec_separator:str=DEFAULT_DECIMAL_SEPARATOR):
        self.set_decimal_separator(dec_separator)
        self._previous_output = None
        self._string_parser = StringParser(self._dec_separator, SUPPORTED_OPERATORS)
        

    def _validate_decimal_separator(self, dec_separator:str) -> bool:
        return dec_separator in [".", ","]
        
    def set_decimal_separator(self, dec_separator:str) -> None:
        if self._validate_decimal_separator(dec_separator):
            self._dec_separator = dec_separator
        else:
            self._dec_separator = DEFAULT_DECIMAL_SEPARATOR
            print(f"Invalid decimal separator. Using default separator: {DEFAULT_DECIMAL_SEPARATOR}")
        filler_line = None
    
    def _execute_operation(self, number1:float, operator:str, number2:float) -> float:
        if operator == "+":
            return number1 + number2
        if operator == "-":
            return number1 - number2
        if operator == "*":
            return number1 * number2
        return number1 / number2

    def get_previous_output(self) -> float:
        return self._previous_output

    def _parse_input(self, input_string:str) -> tuple:
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
