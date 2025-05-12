# i probably didnt make this
class RomanNumeral:
    ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    REPEAT_NUMERALS = ["I", "X", "C", "M"]
    def __init__(self, value):
        self.value = value.upper()
        if any(numeral not in self.ROMAN.keys() for numeral in self.value):
            raise ValueError("Invalid roman numeral provided.")


    def Validator(self, check):
        #Variables
        list_numerals = []
        [list_numerals.append(numeral) for numeral in self.value]
        #First Check
        for numerals in self.ROMAN.keys():
            #Checks if a numeral in REPEAT_NUMERALS has been placed more than 3 times in the numeral the user inputted
            if numerals in self.REPEAT_NUMERALS:
                if list_numerals.count(numerals) > 3:
                    raise ValueError("Invalid roman numeral provided")
                continue
            #Checks if any numeral outside of REPEAT_NUMERALS have been placed more than once
            if list_numerals.count(numerals) > 1:
                raise ValueError("Invalid roman numeral provided")
        #Second Check
        if len(check) >= 2:
            for index in range(2, len(check)):
                if check[index - 1] < check[index]:
                    raise ValueError("Invalid roman numeral provided")


    def to_int(self):
        total = 0
        check = []
        for index, numeral in enumerate(self.value):
            decimal_value = self.ROMAN[numeral]
            # Sees if a numeral has been placed in front a numeral of higher value
            if index > 0:
                one_before = self.value[index - 1]
                if self.ROMAN[one_before] < self.ROMAN[numeral]:
                    check.append(decimal_value - (self.ROMAN[one_before]))
                    check.remove(self.ROMAN[one_before])
                    total += decimal_value - (self.ROMAN[one_before] * 2)  # Take away already added number
                    continue
            total += decimal_value
            check.append(decimal_value)
        self.Validator(check)
        return total


roman = RomanNumeral(input("Enter Roman Numeral: "))
print(roman.to_int())