from functions.get_file_content import get_file_content


def main() -> None:
    # Test 1: lorem.txt (should be truncated)
    print("Test 1: get_file_content(\"calculator\", \"lorem.txt\")")
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print()

    # Test 2: main.py
    print("Test 2: get_file_content(\"calculator\", \"main.py\")")
    result = get_file_content("calculator", "main.py")
    print(result)
    print()

    # Test 3: pkg/calculator.py
    print("Test 3: get_file_content(\"calculator\", \"pkg/calculator.py\")")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print()

    # Test 4: /bin/cat (should return error - outside working directory)
    print("Test 4: get_file_content(\"calculator\", \"/bin/cat\")")
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print()

    # Test 5: pkg/does_not_exist.py (should return error - file not found)
    print("Test 5: get_file_content(\"calculator\", \"pkg/does_not_exist.py\")")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)


if __name__ == "__main__":
    main()