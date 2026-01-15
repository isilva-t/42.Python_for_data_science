import json
import subprocess
import sys


def run_tests_from_json(test_file):
    """Run tests from a JSON file"""
    try:
        with open(test_file, 'r') as f:
            tests = json.load(f)
    except FileNotFoundError:
        print(f"❌ Test file '{test_file}' not found!")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        return

    print(f"Running tests from {test_file}")
    print("=" * 60)

    passed = 0
    total = len(tests)

    for i, test in enumerate(tests, 1):
        description = test.get("description", f"Test {i}")
        args = test.get("args", [])
        expected = test.get("expected", "")

        # Run the program
        cmd = [sys.executable, "sos.py"] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()

        # Check result
        if output == expected:
            print(f"✅ Test {i}: {description}")
            passed += 1
        else:
            print(f"❌ Test {i}: {description}")
            print(f"   Args: {args}")
            print(f"   Expected: '{expected}'")
            print(f"   Got:      '{output}'")

    print("=" * 60)
    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed!")
    else:
        print(f"⚠️  {total - passed} tests failed")


if __name__ == "__main__":
    test_file = "tests.json" if len(sys.argv) == 1 else sys.argv[1]
    run_tests_from_json(test_file)
