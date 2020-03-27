import importlib
import json

from typing import Any

from src import solutions

NUM_SOLUTIONS = 16


def main() -> None:
    for solution_id in range(1, NUM_SOLUTIONS + 1):
        module_name = f"solution{str(solution_id).zfill(3)}"
        module = load_module_from_path(
            f"src.solutions.{module_name}", package=module_name
        )
        run_tests(solution_id, module.tests, module.solver)


def run_tests(solution_id: int, tests, solver) -> None:
    if tests is None or solver is None:
        print(f"No tests and/or solver provided for problem {solution_id}")
        return

    num_tests_passed = 0
    num_tests_failed = 0
    for test_index, test in enumerate(tests):
        inputs, expected_output = test
        try:
            actual_inputs = json.loads(json.dumps(inputs))
        except Exception:
            actual_inputs = None

        actual_output = solver(*inputs)
        passed = actual_output == expected_output
        if passed:
            num_tests_passed += 1
        else:
            num_tests_failed += 1
            print(
                f"Failed test #{test_index + 1}"
                + f"\n  Input: {actual_inputs}"
                + f"\n  Expected: {expected_output}"
                + f"\n  Received: {actual_output}"
                + f"\n"
            )

    if num_tests_passed != len(tests):
        print(f"Failed {num_tests_failed}/{len(tests)} tests")


def load_module_from_path(file_path: str, package: str) -> Any:
    module = importlib.import_module(file_path, package=package)
    return module


if __name__ == "__main__":
    main()
