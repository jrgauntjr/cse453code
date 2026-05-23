def run_non_homograph_tests():
    """Executes validation against paths meant to resolve to distinct files."""
    print("\nRunning non-homograph tests...\n")
    
    canonicalize_path(forbidden, cwd)

    for test in non_homograph_test_cases:
        print(f"Test path: {test}")
        print(f"Canonical test: {canonicalize_path(test, cwd)}")
        print(f"Canonical forbidden: {canonicalize_path(forbidden, cwd)}")

        if not are_homograph_paths(test, forbidden, cwd):
            print(f"PASS: {test} is NOT a homograph.\n")
        else:
            print(f"FAIL: {test} IS a homograph.\n")
    print()