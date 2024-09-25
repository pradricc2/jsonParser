import subprocess
from pathlib import Path

def run_test(file_path, expected_exit_code):
    # Run the parser.py script with the file path
    result = subprocess.run(['python3', 'parser.py', file_path], capture_output=True, text=True)
    actual_exit_code = result.returncode

    # Compare actual vs expected result
    if actual_exit_code == expected_exit_code:
        print(f"PASS: {file_path}")
    else:
        print(f"FAIL: {file_path}")
        print(f"Expected exit code: {expected_exit_code}, but got: {actual_exit_code}")
        print(f"Output: {result.stdout.strip()}")
        print()

def main():
    # Define the path to the test files
    test_folders = ["tests/step1/", "tests/step2/", "tests/step3/", "tests/step4/", "test"]

    # Dictionary of test cases with expected exit codes
    test_cases = {
        "valid.json": 0,
        "valid2.json": 0,# Expected to be valid JSON, so exit code 0
        "invalid.json": 1,   # Expected to be invalid JSON, so exit code 1
        "invalid2.json": 1,  # Expected to be invalid JSON, so exit code 1
        "fail1.json": 1,
        "fail2.json": 1,
        "fail3.json": 1,
        "fail4.json": 1,
        "fail5.json": 1,
        "fail6.json": 1,
        "fail7.json": 1,
        "fail8.json": 1,
        "fail9.json": 1,
        "fail10.json": 1,
        "fail11.json": 1,
        "fail12.json": 1,
        "fail13.json": 1,
        "fail14.json": 1,
        "fail15.json": 1,
        "fail16.json": 1,
        "fail17.json": 1,
        "fail18.json": 1,
        "fail19.json": 1,
        "fail20.json": 1,
        "fail21.json": 1,
        "fail22.json": 1,
        "fail23.json": 1,
        "fail24.json": 1,
        "fail25.json": 1,
        "fail26.json": 1,
        "fail27.json": 1,
        "fail28.json": 1,
        "fail29.json": 1,
        "fail30.json": 1,
        "fail31.json": 1,
        "fail32.json": 1,
        "fail33.json": 1,
        "pass1.json": 0,
        "pass2.json": 0,
        "pass3.json": 0
    }

    # Iterate through each test case
    for test_file, expected_exit_code in test_cases.items():
        for test_folder in test_folders:
            file_path = Path(test_folder) / test_file
            if file_path.exists():
                run_test(file_path, expected_exit_code)
            else:
                continue

if __name__ == "__main__":
    main()
