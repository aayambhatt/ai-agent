from functions.get_files_info import get_files_info

if __name__ == "__main__":
    # Test Case 1: Valid directory (should succeed)
    result1 = get_files_info("calculator", ".")
    print(f"Test 1 result: {result1}")
    
    # Test Case 2: Outside working directory (should fail)
    result2 = get_files_info("calculator", "/bin")
    print(f"Test 2 result: {result2}")
    
    # Test Case 3: Outside working directory with ../ (should fail)
    result3 = get_files_info("calculator", "../")
    print(f"Test 3 result: {result3}")
    
    # Test Case 4: Not a directory (should fail)
    result4 = get_files_info("calculator", "main.py")
    print(f"Test 4 result: {result4}")