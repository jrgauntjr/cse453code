# --- Test Environment Configuration ---
# Target file representing a restricted assert in a security context
forbidden = r"C:\Users\Kimberly\secret\password.txt"
cwd = r"C:\Users\Kimberly"

# Paths that should successfully resolve to a DIFFERENT location than the forbidden file
non_homograph_test_cases = [
    r"C:\Users\Kimberly\secret\notes.txt",
    r"C:\Users\Kimberly\public\password.txt",
    r"C:\Users\Kimberly\secret\password.docx",
    r"C:\Users\Kimbelry\secret\password.txt",
    r"D:\Users\Kimberly\secret\password.txt",
    r".\public\password.txt"
]

def run_non_homograph_tests():
    """Executes validation against paths meant to resolve to distinct files."""
    print("\nRunning non-homograph tests...\n")

    for test in non_homograph_test_cases:
        if not are_homographs(test, forbidden, cwd): # The name of the Homograph function needs to replace are_homographs, then the function will work.
            print(f"PASS: {test} is NOT a homograph.")
        else:
            print(f"FAIL: {test} IS a homograph.")
    print()