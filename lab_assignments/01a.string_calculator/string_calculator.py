import re

DEFAULT_DECIMAL_SEPARATOR = "."
SUPPORTED_OPERATORS = ["+", "-", "*", "/"]

class StringCalculator:
    def __init__(self, dec_separator:str = DEFAULT_DECIMAL_SEPARATOR):
        self.set_decimal_separator(dec_separator)
        self._previous_output = None

    def _validate_decimal_separator(self, dec_separator:str) -> bool:
        return dec_separator in [".", ","]
        
    def set_decimal_separator(self, dec_separator:str) -> None:
        if self._validate_decimal_separator(dec_separator):
            self._dec_separator = dec_separator
        else:
            self._dec_separator = DEFAULT_DECIMAL_SEPARATOR
            print(f"Invalid decimal separator. Using default separator: {DEFAULT_DECIMAL_SEPARATOR}")
        self._number_regex = re.compile(rf"^(-?\d+){re.escape(self._dec_separator)}?(\d*)$")
        
    def _parse_number(self, number_string:str) -> float:
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
        input_string = input_string.strip()
        input_string = re.sub(r" +", " ", input_string)
        input_groups = input_string.split(" ")
        print(input_groups)
        # group 0 and 2 should be numbers, group 1 should be an operator
        if len(input_groups) != 3:
            raise ValueError(f"Invalid input string '{input_string}': expected 3 groups, got {len(input_groups)}")
        if input_groups[1] not in SUPPORTED_OPERATORS:
            raise ValueError(f"Invalid operator '{input_groups[1]}'")
        return [self._parse_number(input_groups[0]), input_groups[1], self._parse_number(input_groups[2])]
    
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
