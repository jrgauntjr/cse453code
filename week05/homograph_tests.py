# --- Test Environment Configuration ---
# Relative paths that should successfully resolve to EQUAL the forbidden file
homograph_tests = [
    r"C:\Users\Kimberly\secret\password.txt",
    r"c:\users\kimberly\secret\password.txt",       # Case variation
    r"C:\USERS\KIMBERLY\SECRET\PASSWORD.TXT",       # Case variation
    r"C:/Users/Kimberly/secret/password.txt",       # Forward slash variation
    r"C:\Users\Kimberly\.\secret\password.txt",     # Inline current-dir dot
    r"C:\Users\Kimberly\secret\.\password.txt",     # Inline current-dir dot
    r"C:\Users\Kimberly\Documents\..\secret\password.txt",  # Trailing dot-dot cancellation
    r"C:\Users\Kimberly\secret\backup\..\password.txt",     # Trailing dot-dot cancellation
    r"C:\\Users\\Kimberly\\secret\\password.txt",   # Malformed duplicate slashes
    r".\secret\password.txt",                       # Relative path
    r"secret\password.txt",                         # Implicit relative path
]

def run_homograph_tests():
    """Executes validation against paths meant to resolve to the identical forbidden file path"""
    print("\nRunning homograph tests...\n")

    for test_path in homograph_tests:
        print(f"Test path: {test_path}")
        print(f"Canonical test: {canonicalization(test_path, cwd)}")
        print(f"Canonical forbidden: {canonicalization(forbidden, cwd)}")

        if are_homographs(test_path, forbidden, cwd):
            print("PASS: This is equivalent to the forbidden path.\n")
        else:
            print("FAIL: This is NOT equivalent to the forbidden path.\n")