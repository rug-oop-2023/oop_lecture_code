import re
from typing import List

class StringNumberParser:
    def __init__(self, decimal_separator:str) -> None:
        self._parsing_regex = rf"^(-?\d+){re.escape(decimal_separator)}?(\d*)"
    
    def _compose_number(self, integer_part:str, decimal_part:str):
        if decimal_part == "":
            return float(integer_part)
        return float(f"{integer_part}.{decimal_part}")

    def parse(self, string:str, previous_output:float=None) -> float:
        if string.lower() == "ans":
            return previous_output
        match = re.match(self._parsing_regex, string)
        if match:
            return self._compose_number(*match.groups())
        else:
            raise ValueError(f"Invalid number string '{string}'")
        
class StringParser:
    def __init__(self, decimal_separator:str, supported_operators:List[str]=["+", "-", "*", "/"]) -> None:
        self._number_parser = StringNumberParser(decimal_separator)
        self._supported_operators = supported_operators
    
    def parse(self, string:str, previous_output:float=None) -> float:
        preprocessed_string = string.strip()
        preprocessed_string = re.sub(r" +", " ", preprocessed_string)
        preprocessed_string = preprocessed_string.split()
        if len(preprocessed_string) != 3:
            raise ValueError(f"Invalid input string '{string}': expected 3 groups, got {len(preprocessed_string)}")
        if preprocessed_string[1] not in self._supported_operators:
            raise ValueError(f"Invalid operator '{preprocessed_string[1]}'")
        return [
            self._number_parser.parse(preprocessed_string[0], previous_output),
            preprocessed_string[1],
            self._number_parser.parse(preprocessed_string[2], previous_output)
            ]

        