import subprocess
import sys


def run_test(args, expected_output, test_name):
    cmd = [sys.executable, "whatis.py"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()

    if output == expected_output:
        print(f"✅  {test_name}")
    else:
        print(f"❌ {test_name}")
        print(f"    Expected:   {expected_output}")
        print(f"    Got:        {output}")
    return output == expected_output


def main():
    print("Testing whatis.py\n" + "="*50)

    tests_passed = 0
    total_tests = 0

    # Test 1: Even number
    total_tests += 1
    if run_test(["14"], "I'm Even.", "Test 1: Even number (14)"):
        tests_passed += 1

    # Test 2: Odd number
    total_tests += 1
    if run_test(["-5"], "I'm Odd.", "Test 2: Odd number (-5)"):
        tests_passed += 1

    # Test 3: Zero (even)
    total_tests += 1
    if run_test(["0"], "I'm Even.", "Test 3: Zero"):
        tests_passed += 1

    # Test 4: No argument (empty output)
    total_tests += 1
    if run_test([], "", "Test 4: No argument"):
        tests_passed += 1

    # Test 5: Non-integer
    total_tests += 1
    if run_test(["Hi!"], "AssertionError: argument is not an integer",
                "Test 5: Non-integer"):
        tests_passed += 1

    # Test 6: Multiple arguments
    total_tests += 1
    if run_test(["13", "5"], "AssertionError: more than one argument is provided",
                "Test 6: Multiple arguments"):
        tests_passed += 1

    # Test 7: Another even
    total_tests += 1
    if run_test(["100"], "I'm Even.", "Test 7: Large even (100)"):
        tests_passed += 1

    # Test 8: Another odd
    total_tests += 1
    if run_test(["99"], "I'm Odd.", "Test 8: Large odd (99)"):
        tests_passed += 1

    # Test 9: Float string
    total_tests += 1
    if run_test(["3.14"], "AssertionError: argument is not an integer",
                "Test 9: Float string"):
        tests_passed += 1

    print("\n" + "="*50)
    print(f"Results: {tests_passed}/{total_tests} tests passed")

    if tests_passed == total_tests:
        print("🎉 All tests passed!")
    else:
        print(f"⚠️  {total_tests - tests_passed} tests failed")


if __name__ == "__main__":
    main()
