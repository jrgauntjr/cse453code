"""Unsafe query generation. Accepts two strings as parameters 
   'username' and 'password'. It is unsafe because it directly
   inserts user input into the SQL command.
"""
def generate_query(username, password):
    return("SELECT * FROM users"
            f"WHERE username = '{username}'"
            f"AND password = '{password}';"
            )

"""Normal input example"""
def run_normal_input():
    print("\nNormal input example.")
    username = "kimberly_01"
    password = "password_123"
    query = generate_query(username, password)
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Generated Query: {query}")
    print()

"""Valid test cases use only letters, numbers, and underscores"""
valid_test_cases = [
    ("kimberly_01", "BlueSky123"),
    ("joseph_02", "Secure_123"),
    ("jacob_03", "Login_2025")
]

"""Function to run valid test cases. Test cases run through
    query generator to prove it works under normal conditions.
"""
def run_valid_test_cases():
    print("\nValid input tests")
    print("-" * 60)

    for username, password in valid_test_cases:
        query = generate_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()

"""Vulnerability test cases. These cases show the query generator
    is vulnerable to the four SQL attack types. Tautology, Comment,
    UNION, and Add Statement.
"""
tautology_test_cases = [
    ("admin' OR '1' = '1'", "anything"),
    ("user' OR 'x' = 'x'", "nopasswd"),
    ("admin' OR 'a' = 'a'", "nothing"),
]

comment_test_cases = [
    ("admin' --", "anything"),
    ("user' #", "nothing"),
    ("student' --", "tester"),
]

union_test_cases = [
    ("admin' UNION SELECT username, password FROM users --", "anything"),
    ("student' UNION SELECT grades, entry FROM accounts --", "nothing"),
    ("guest' UNION SELECT admin, roles FROM accounts --", "anything")
]

added_statement_test_cases = [
    ("user'; DROP TABLE users; --", "anything"),
    ("admin'; DELETE FROM users; --", "nothing"),
    ("student'; INSERT INTO users; --", "something")
]

"""Function to run tautology_test_cases. This function shows
    that the SQL query in generate_query() is vulnerable to 
    a tautology attack.
"""
def run_tautology_test_cases():
    print("\nTautology attack example.")
    print("-" * 60)

    for username, password in tautology_test_cases:
        query = generate_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()

"""Function to run comment_test_cases. This function shows
    that the SQL query in generate_query() is vulnerable to 
    a comment attack.
"""
def run_comment_test_cases():
    print("\nComment attack example.")
    print("-" * 60)

    for username, password in comment_test_cases:
        query = generate_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()

def run_union_test_cases():
    print("\nUNION attack example.")
    print("-" * 60)

    for username, password in union_test_cases:
        query = generate_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()

def run_added_statement_test_cases():
    print("\nAdded Statement attack example.")
    print("-" *60)

    for username, password in added_statement_test_cases:
        query = generate_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()

"""Weak Mitigation: filters input manually"""
def weak_sanitizer(user_input):
    blocked_terms = [
        "'", "--", "#", ";", "OR", "or", "UNION", "union",
        "DROP", "drop", "DELETE", "delete"
    ]

    sanitized = user_input

    for term in blocked_terms:
        sanitized = sanitized.replace(term, "")

    return sanitized

"""Strong mitigation: parameterize queries"""
def generate_strong_mitigated_query(username, password):
    query = (
        "SELECT * FROM users "
        "WHERE username = ?"
        "AND password = ?;"
    )

    parameters = (username, password)
    return query, parameters

"""Strong mitigation output function that runs test cases
    for UNION, added statement, comment, and tautology attacks
"""
def run_test_cases_against_strong_mitigation():
    print("\nStrong Mitigation Output for all attacks.")
    print("-" * 60)

    print("\nAdded Statement Attack: Strong Mitigation\n")
    print("-" * 60)
    for username, password in added_statement_test_cases:
        query = generate_strong_mitigated_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()

    print("-" * 60)
    print("\nUNION Attack: Strong Mitigation\n")
    print("-" * 60)

    for username, password in union_test_cases:
        query = generate_strong_mitigated_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()

    print("-" * 60)
    print("\nTautology Attack: Strong Mitigation\n")
    print("-" * 60)    
    for username, password in tautology_test_cases:
        query = generate_strong_mitigated_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()


    print("-" * 60)
    print("\nComment Attack: Strong Mitigation\n")
    print("-" * 60)
    for username, password in comment_test_cases:
        query = generate_strong_mitigated_query(username, password)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Generated Query: {query}")
        print()



"""Menu"""
"""Main execution loop providing a CLI wrapper for the test suites."""
def menu():
    
    # Dictionary dispatch pattern acting as a scalable alternative to switch/if-elif chains
    options = {
        "1": run_normal_input,
        "2": run_valid_test_cases,
        "3": run_union_test_cases,
        "4": run_added_statement_test_cases,
        "5": run_comment_test_cases,
        "6": run_tautology_test_cases,
        "7": run_test_cases_against_strong_mitigation,
    }

    while True:
        print("SQL Query Generator")
        print("1. Normal input")
        print("2. Valid test cases")
        print("3. UNION test cases")
        print("4. Added Statement test cases")
        print("5. Comment test cases")
        print("6. Tautology test cases")
        print("7. All attack test cases against strong mitigation")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice in options:
            options[choice]()   # Dynamically fetch an execute target function
        elif choice == "8":
            print("Thank you for using Homograph Tester! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4\n")

if __name__ == "__main__":
    menu()