def genQuery(username: str, password: str):
    return f"SELECT authenticate FROM password_auth WHERE username = '{username}' AND password = '{password}'"

def testValid(query_fn=genQuery):
    print("=== testValid: legitimate input ===")
    test_cases = [
        ("admin", "secret123"),
        ("user_1", "pass_word"),
        ("Test42", "abc_123"),
        ("john_doe", "mypassword"),
        ("a1_b2", "x9_y8"),
    ]
    for username, password in test_cases:
        result = query_fn(username, password)
        print(f"username={username!r}, password={password!r}")
        print(f"  -> {_format_result(result)}\n")

def testAddState(query_fn=genQuery):
    print("=== testAddState: stacked / additional statement injection ===")
    test_cases = [
        ("admin'; DROP TABLE password_auth;--", "x"),
        ("'; DELETE FROM password_auth WHERE '1'='1", "x"),
        ("x'; INSERT INTO password_auth VALUES('hacker','pass');--", "x"),
        ("user", "pass'; UPDATE password_auth SET password='hacked';--"),
    ]
    for username, password in test_cases:
        result = query_fn(username, password)
        print(f"username={username!r}, password={password!r}")
        print(f"  -> {_format_result(result)}\n")


def run_all_tests(query_fn, title: str):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70 + "\n")
    testValid(query_fn)
    testTautology(query_fn)
    testUnion(query_fn)
    testAddState(query_fn)
    testComment(query_fn)



def main_menu():
    while True:
        print("\nW06 Lab: SQL Injection Mitigation")
        print("1. Run all tests (vulnerable genQuery)")
        print("2. Run all tests (genQueryWeak)")
        print("3. Run all tests (genQueryStrong)")
        print("4. Run all three comparisons")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            run_all_tests(genQuery, "VULNERABLE: genQuery (no mitigation)")
        elif choice == "2":
            run_all_tests(genQueryWeak, "WEAK MITIGATION: genQueryWeak")
        elif choice == "3":
            run_all_tests(genQueryStrong, "STRONG MITIGATION: genQueryStrong")
        elif choice == "4":
            run_all_tests(genQuery, "VULNERABLE: genQuery (no mitigation)")
            run_all_tests(genQueryWeak, "WEAK MITIGATION: genQueryWeak")
            run_all_tests(genQueryStrong, "STRONG MITIGATION: genQueryStrong")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()

