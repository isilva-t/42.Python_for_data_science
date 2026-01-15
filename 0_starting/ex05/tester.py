import subprocess
import sys


def run_test(args, expected_lines, test_name, stdin_input=None):
    """Run building.py with given args and check output"""
    cmd = [sys.executable, "building.py"] + args
    result = subprocess.run(cmd, capture_output=True,
                            text=True, input=stdin_input)
    output_lines = result.stdout.strip().split('\n')

    passed = True
    if len(output_lines) != len(expected_lines):
        passed = False
    else:
        for i, (expected, actual) in enumerate(zip(expected_lines, output_lines)):
            if expected != actual:
                passed = False
                break

    if passed:
        print(f"✅ {test_name}")
    else:
        print(f"❌ {test_name}")
        print(f"   Expected:")
        for line in expected_lines:
            print(f"     '{line}'")
        print(f"   Got:")
        for line in output_lines:
            print(f"     '{line}'")
    return passed


def main():
    print("Testing building.py\n" + "="*60)

    tests_passed = 0
    total_tests = 0

    # Test 1: Example from exercise
    total_tests += 1
    text = "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
    expected = [
        "The text contains 171 characters:",
        "2 upper letters",
        "121 lower letters",
        "7 punctuation marks",
        "26 spaces",
        "15 digits"
    ]
    if run_test([text], expected, "Test 1: Long text from exercise"):
        tests_passed += 1

    # Test 2: Simple text
    total_tests += 1
    text = "Hello World!"
    expected = [
        "The text contains 12 characters:",
        "2 upper letters",
        "8 lower letters",
        "1 punctuation marks",
        "1 spaces",
        "0 digits"
    ]
    if run_test([text], expected, "Test 2: Hello World!"):
        tests_passed += 1

    # Test 3: Only digits
    total_tests += 1
    text = "123456"
    expected = [
        "The text contains 6 characters:",
        "0 upper letters",
        "0 lower letters",
        "0 punctuation marks",
        "0 spaces",
        "6 digits"
    ]
    if run_test([text], expected, "Test 3: Only digits"):
        tests_passed += 1

    # Test 4: Only uppercase
    total_tests += 1
    text = "HELLO"
    expected = [
        "The text contains 5 characters:",
        "5 upper letters",
        "0 lower letters",
        "0 punctuation marks",
        "0 spaces",
        "0 digits"
    ]
    if run_test([text], expected, "Test 4: Only uppercase"):
        tests_passed += 1

    # Test 5: Only lowercase
    total_tests += 1
    text = "hello"
    expected = [
        "The text contains 5 characters:",
        "0 upper letters",
        "5 lower letters",
        "0 punctuation marks",
        "0 spaces",
        "0 digits"
    ]
    if run_test([text], expected, "Test 5: Only lowercase"):
        tests_passed += 1

    # Test 6: Punctuation mix
    total_tests += 1
    text = "Hello, World! How are you?"
    expected = [
        "The text contains 26 characters:",
        "3 upper letters",
        "16 lower letters",  # ← Fixed from 17
        "3 punctuation marks",
        "4 spaces",  # ← Fixed from 3
        "0 digits"
    ]
    if run_test([text], expected, "Test 6: Mixed with punctuation"):
        tests_passed += 1

    # Test 7: Empty string
    total_tests += 1
    text = ""
    expected = [
        "The text contains 0 characters:",
        "0 upper letters",
        "0 lower letters",
        "0 punctuation marks",
        "0 spaces",
        "0 digits"
    ]
    if run_test([text], expected, "Test 7: Empty string"):
        tests_passed += 1

    # Test 8: Only spaces
    total_tests += 1
    text = "     "
    expected = [
        "The text contains 5 characters:",
        "0 upper letters",
        "0 lower letters",
        "0 punctuation marks",
        "5 spaces",
        "0 digits"
    ]
    if run_test([text], expected, "Test 8: Only spaces"):
        tests_passed += 1

    # Test 9: Multiple arguments (error)
    total_tests += 1
    expected = [
        "AssertionError: more than one argument is provided"
    ]
    if run_test(["Hello", "World"], expected, "Test 9: Multiple arguments"):
        tests_passed += 1

    # Test 10: No argument with input
    total_tests += 1
    stdin_text = "Test Input!"
    expected = [
        "What is the text to count?",
        "The text contains 11 characters:",
        "2 upper letters",
        "7 lower letters",
        "1 punctuation marks",
        "1 spaces",
        "0 digits"
    ]
    if run_test([], expected, "Test 10: No args with stdin", stdin_input=stdin_text):
        tests_passed += 1

    # Test 11: From subject - with newline counted as space
    total_tests += 1
    stdin_text = "Hello World!\n"
    expected = [
        "What is the text to count?",
        "The text contains 13 characters:",
        "2 upper letters",
        "8 lower letters",
        "1 punctuation marks",
        "2 spaces",
        "0 digits"
    ]
    if run_test([], expected, "Test 11: Subject example with newline", stdin_input=stdin_text):
        tests_passed += 1

    print("\n" + "="*60)
    print(f"Results: {tests_passed}/{total_tests} tests passed")

    if tests_passed == total_tests:
        print("🎉 All tests passed!")
    else:
        print(f"⚠️  {total_tests - tests_passed} tests failed")


if __name__ == "__main__":
    main()
