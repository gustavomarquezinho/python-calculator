exponents = {
    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'
}

class Calcs:
    def __init__(self, operation: str, testing: bool = False):
        self.error = None

        self.testing = testing
        self.solved = 0

        self.operators = (
            'R', '^', 'x', '*', '÷', '/', ':', '+', '-'
        )

        self.final_priority = (self.operators.index('*'), self.operators.index('+'))
        self.operation_copy = ''

        self.operation = operation
        self.operation = self.filter()
        
        if not self.is_valid_operation():
            self.show_error('Operação inválida!')
        else:
            self.operation_copy = self.operation.copy()
            self.solve()


    def filter(self) -> list:
        string = ''

        for index, char in enumerate(self.operation):
            if char in exponents.keys():
                string += exponents[char]

            elif char.isdigit() or (index == 0 and char == '-'):
                string += char

            elif char == '√':
                string += ' R '

            elif char == ',':
                string += '.'

            elif char in self.operators:
                string += ' ' + char + ' '

        print(string.split())
        return string.split()


    def is_valid_operation(self) -> bool:
        if len(self.operation) == 0:
            return False

        if self.operation[len(self.operation) - 1] in self.operators:
            return False

        if self.operation[0] in self.operators:
            return False

        for index, char in enumerate(self.operation):
            if index % 2 != 0:
                if char not in self.operators:
                    return False
        return True


    def get_operator(self) -> str:
        for item in self.operation:
            if item in self.operators[:self.final_priority[0]]:
                return item

        for item in self.operation:
            if item in self.operators[self.final_priority[0]:self.final_priority[1]]:
                return item

        for item in self.operation:
            if item in self.operators[self.final_priority[1]:]:
                return item

                
    def solve(self) -> int or float:
        while len(self.operation) > 1:
            operator = self.get_operator()
        
            if not self.testing:
                print(*self.operation)

            index = self.operation.index(operator)
            
            numbers = (
                self.get_near_number(index - 1),
                self.get_near_number(index)
            )
            
            solved = self.choose_operator(operator, numbers)
            self.solved = solved

            self.operation[index - 1] = str(solved)

        if not self.testing:
            print(self.solved)


    def get_near_number(self, index: int) -> float:
        number = self.operation[index]
        self.operation.pop(index)

        return float(number)


    def choose_operator(self, operator: str, numbers: tuple) -> float:
        match operator:
            case 'R':
                return numbers[1] ** (1 / numbers[0])

            case '^':
                return numbers[0] ** numbers[1]

            case 'x' | '*':
                return numbers[0] * numbers[1]

            case '÷' | '/' | ':':
                try:
                    return numbers[0] / numbers[1]
                except ZeroDivisionError:
                    self.show_error('Não é possível dividir por zero!')
                    return 0.0

            case '+':
                return numbers[0] + numbers[1]

            case '-':
                return numbers[0] - numbers[1]


    def get_formatted(self) -> str:
        if self.error is not None:
            return ''

        print(self.solved)

        try:
            if int(self.solved) == float(self.solved):
                return str(int(self.solved))
        except (ValueError, TypeError):
            pass

        return str(self.solved).replace('.', ',')


    def show_error(self, error: str) -> None:
        self.error = error
        print(error)


if __name__ == '__main__':
    calcs = Calcs('23434 ÷ 345 - 23 + 23262 * 23 - 23425 - 256')
    calcs = Calcs('1,123 * 2')
