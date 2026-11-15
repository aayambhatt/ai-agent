from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print("Result for current directory:")
    result1 = get_files_info("calculator", ".")
    print(result1)
    print()

    print("Result for 'pkg' directory:")
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    print()

    print("Result for '/bin' directory:")
    result3 = get_files_info("calculator", "/bin")
    print(f"    {result3}")
    print()

    print("Result for '../' directory:")
    result4 = get_files_info("calculator", "../")
    print(f"    {result4}")