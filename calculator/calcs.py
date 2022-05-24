class Calcs:
    def __init__(self, operation: str, testing: bool = False):
        self.solved = 0

        self.operators = (
            'x', '*', '/', '+', '-'
        )

        self.operation = operation
        self.operation = self.filter()
        
        if not self.is_valid_operation():
            raise Exception('Invalid operation')

        self.testing = testing
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
            if item in self.operators[:3]:
                return item

        for item in self.operation:
            if item in self.operators[3:]:
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

        return self.solved


    def get_near_number(self, index: int) -> float:
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
                return numbers[0] - numbers[1]

            case _:
                raise Exception('Invalid operator')


if __name__ == '__main__':
    calcs = Calcs('23434 / 345 - 23 + 23262 * 23 - 23425 - 256')
    print(calcs.solved)
