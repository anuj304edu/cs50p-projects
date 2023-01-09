import random


def main():
    l = get_level()
    score_n, problem_n, wrong_n = 0, 0, 0
    while True:
        x, y = generate_integer(l)
        try:
            result_add = int(input(f"{x} + {y} = "))
            if problem_n >= 9:
                score_n = score_n + 1
                print("score:", score_n)
                exit(0)
            elif result_add != x + y:
                wrong_n = wrong_n + 1
                problem_n = problem_n + 1
                print("EEE")
                while True:
                    try:
                        result_add = int(input(f"{x} + {y} = "))
                        if wrong_n >= 2:
                            print(f"{x} + {y} = ", (x + y))
                            wrong_n = 0
                            break
                        elif result_add == x + y:
                            score_n = score_n + 1
                            wrong_n = 0
                            break
                        elif result_add != x + y:
                            wrong_n = wrong_n + 1
                            print("EEE")
                            continue
                    except ValueError:
                        wrong_n = wrong_n + 1
                        problem_n = problem_n + 1
                        print("EEE")
                        pass
            elif result_add == x + y:
                problem_n = problem_n + 1
                score_n = score_n + 1
        except ValueError:
            wrong_n = wrong_n + 1
            problem_n = problem_n + 1
            print("EEE")
            while True:
                try:
                    result_add = int(input(f"{x} + {y} = "))
                    if wrong_n >= 2:
                        print(f"{x} + {y} = ", (x + y))
                        wrong_n = 0
                        break
                    elif result_add == x + y:
                        wrong_n = 0
                        break
                    elif result_add != x + y:
                        wrong_n = wrong_n + 1
                        print("EEE")
                        continue
                except ValueError:
                    wrong_n = wrong_n + 1
                    print("EEE")
                    pass


def get_level():
    while True:
        try:
            n = int(input())
            if n in [1, 2, 3]:
                return n
            else:
                pass
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randrange(0, 10)
        y = random.randrange(0, 10)
    else:
        x = random.randrange(10 ** (level - 1), 10**level)
        y = random.randrange(10 ** (level - 1), 10**level)
    return x, y


if __name__ == "__main__":
    main()
