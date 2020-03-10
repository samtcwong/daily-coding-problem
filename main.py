from src.solutions import solution001


def main():
    run_tests(solution001.tests, solution001.solver)


def run_tests(tests, solver):
    num_tests_passed = 0
    num_tests_failed = 0
    for test_index, test in enumerate(tests):
        inputs, expected_output = test
        actual_output = solver(*inputs)
        passed = actual_output == expected_output
        if passed:
            num_tests_passed += 1
        else:
            num_tests_failed += 1
            print(
                f'Failed test #{test_index + 1}'
                + f'\n  Input: {inputs}'
                + f'\n  Expected: {expected_output}'
                + f'\n  Received: {actual_output}'
                + f'\n'
            )

    if num_tests_passed != len(tests):
        print(f'Failed {num_tests_failed}/{len(tests)} tests')


if __name__ == '__main__':
    main()
