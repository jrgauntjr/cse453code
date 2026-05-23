def canonicalize_path(path: str, cwd_context: str) -> str:
    if not path:
        return ""
    # Normalize path by replacing '/' with '\\' and converting to lowercase for case-insensitivity
    normalized = path.replace('/', '\\').lower()
    normalized_cwd = cwd_context.replace('/', '\\').lower()
    
    # Handle drive letters and absolute vs relative paths

    # Based off of Windows path, they normally look like C:\Path, C:Path or relative \path
    has_drive = len(normalized) >= 2 and normalized[1] == ':' and normalized[0].isalpha()

    if has_drive:
        drive = normalized[:2]
        rest_of_path = normalized[2:]

        # If it's C:Path, it's relative to the C drives current directory
        # We assume absolute C:\ style or fix the missing slash
        if not rest_of_path.startswith('\\'):
            rest_of_path = '\\' + rest_of_path
            
    else:
        
        # If no drive letter given, we assume it's relative to the current working drive
        drive = normalized_cwd[:2]

        if normalized.startswith('\\'):
            # Path starts from root of current drive
            rest_of_path = normalized

        else:
            # Path is entirely relative
            rest_of_path = '\\' + normalized

    # Split into segments and strip out empty segments caused by multiple slashes
    raw_segments = rest_of_path.split('\\')
    segments = [seg for seg in raw_segments if seg != '']
    
    resolved_stack = []

    for segment in segments:
        if segment == '.':
            continue
        elif segment == '..':
            if resolved_stack:
                resolved_stack.pop()
            # Navigating above root is ignored and keeps us at root on Windows
        else:
            resolved_stack.append(segment)
    
    # Return reconstructed final Windows canonical path
    return drive + '\\' + '\\'.join(resolved_stack)

    
def are_homograph_paths(path1: str, path2: str, cwd_context: str) -> bool:
    return canonicalize_path(path1, cwd_context) == canonicalize_path(path2, cwd_context)


def main_menu():
    print("Homograph Detection Tool")
    print("1. Automated Test Cases")
    print("2. Manual 2 Path Comparison")
    choice = input("Select an option (1-2): ")

    if choice == '1':
        print("REPLACE WITH AUTO TEST CASE FUNCTION NAME")
    elif choice == '2':
        p1 = input("Specify the first filename: ")
        p2 = input("Specify the second filename: ")
        cwd_context = input("Specify the cwd context (example: C:\\Users\\Jacob): ")

        homograph_result = are_homograph_paths(p1, p2, cwd_context)
        if homograph_result:
            print("The paths are homographs")
        else:
            print("The paths are not homographs")

if __name__ == "__main__":
    main_menu()
