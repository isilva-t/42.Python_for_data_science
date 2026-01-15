import json
import sys


def run_tests_from_json(test_file):
    """Run tests for ft_filter from a JSON file"""
    from ft_filter import ft_filter

    try:
        with open(test_file, 'r') as f:
            tests = json.load(f)
    except FileNotFoundError:
        print(f"❌ Test file '{test_file}' not found!")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        return

    print(f"Running ft_filter tests from {test_file}")
    print("=" * 60)

    passed = 0
    total = len(tests)

    for i, test in enumerate(tests, 1):
        description = test.get("description", f"Test {i}")
        func_str = test.get("function")
        iterable = test.get("iterable", [])

        # Convert function string to actual function
        func = None if func_str is None else eval(func_str)

        # Get results from both implementations
        try:
            ft_result = ft_filter(func, iterable)
            builtin_result = list(filter(func, iterable))
        except Exception as e:
            print(f"❌ Test {i}: {description}")
            print(f"   Error: {e}")
            continue

        # Check result
        if ft_result == builtin_result:
            print(f"✅ Test {i}: {description}")
            passed += 1
        else:
            print(f"❌ Test {i}: {description}")
            print(f"   Function: {func_str}")
            print(f"   Iterable: {iterable}")
            print(f"   Expected: {builtin_result}")
            print(f"   Got:      {ft_result}")

    print("=" * 60)
    print(f"Results: {passed}/{total} tests passed")

    # Test docstring
    print("\n" + "=" * 60)
    print("Docstring check:")
    if ft_filter.__doc__ == filter.__doc__:
        print("✅ Docstring matches filter.__doc__")
    else:
        print("❌ Docstring mismatch!")
        print(f"   Expected:\n{filter.__doc__}")
        print(f"   Got:\n{ft_filter.__doc__}")


if __name__ == "__main__":
    test_file = "tests1.json" if len(sys.argv) == 1 else sys.argv[1]
    run_tests_from_json(test_file)
