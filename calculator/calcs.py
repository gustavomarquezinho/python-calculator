class Calcs:
    def __init__(self, operation: str):
        self.solved = 0

        self.operators = (
            'x', '*', '/', '+', '-'
        )

        self.operation = operation
        self.operation = self.filter()
        
        if not self.is_valid_operation():
            raise Exception('Invalid operation')

        self.solve()


    def filter(self) -> list:
        string = ''

        for index, char in enumerate(self.operation):
            if char.isdigit() or (index == 0 and char in self.operators):
                string += char

            elif char in self.operators:
                string += ' ' + char + ' '

        return string.split()


    def is_valid_operation(self) -> bool:
        if self.operation[len(self.operation) - 1] in self.operators:
            return False

        if self.operation[0] in self.operators:
            return False

        for index, char in enumerate(self.operation):
            if index % 2 != 0:
                if char not in self.operators:
                    return False
        return True


    def solve(self) -> float:
        for operator in self.operators:

            while operator in self.operation:
                index = self.operation.index(operator)
                
                numbers = (
                    self.get_number(index - 1),
                    self.get_number(index)
                )
                
                solved = self.choose_operator(operator, numbers)

                self.operation[self.operation.index(operator)] = str(solved)
                self.solved += solved

        return self.solved


    def get_number(self, index: int) -> float:
        number = self.operation[index]
        self.operation.pop(index)
        return float(number)


    def choose_operator(self, operator: str, numbers: tuple) -> float:
        match operator:
            case '*' | 'x':
                return numbers[0] * numbers[1]

            case '/':
                return numbers[0] / numbers[1]

            case '+':
                return numbers[0] + numbers[1]

            case '-':
                return -(numbers[0] - numbers[1])

            case _:
                raise Exception('Invalid operator')


if __name__ == '__main__':
    calcs = Calcs('12324 + 1246624 + 1 / 345 - 5 * 45')

    # 12324 + 1246624 + 1 / 345 - 5 * 45
    # 12324 + 1246624 + 1 / 345 - 225
    # 12324 + 1246624 + 0.00289 - 225
    # 1.259.012