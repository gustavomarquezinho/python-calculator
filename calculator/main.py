from scripts.calcs import Calcs
from scripts.gui import Gui

PROGRAM_NAME = 'Calculator (2505.22)'


def results_tests():
    operations_results = {
        '2340334 + 32452 - 34647 * 2 + 3224242 - 1234 / 4':
            5527425.5,

        '23434 ÷ 345 - 23 + 23262 * 23 - 23425 - 256':
            511389.924638,

        '12324 + 1246624 + 1 / 345 - 5 * 45':
            1258723.0029,

        '13,12 * 22,34 / 46,2 + 34,57 - 2,1':
            38.8141731602,

        '23424,12 * 12 + 345 / 2 - 243 : 5':
            281213.34,
    }

    for index, (key, value) in enumerate(operations_results.items(), start=1):
        calcs = Calcs(key, True)
    
        if round(calcs.solved, 4) == round(value, 4):
            print(f'{index} - PASSED')
            continue

        print(f'{index} - FAILED')


if __name__ == '__main__':
    results_tests()

    gui = Gui(PROGRAM_NAME)
    gui.mainloop()