def remove_adjacent_duplicates(s):
    if not s:
        return s  # Base case: empty string

    if len(s) == 1:
        return s  # Base case: single character string

    if s[0] == s[1]:
        return remove_adjacent_duplicates(s[2:])  # Remove adjacent duplicates and recursively call on remaining string
    else:
        return s[0] + remove_adjacent_duplicates(s[1:])  # Keep the current character and recursively call on remaining string

# Example usage:
input_str = input()
output_str = remove_adjacent_duplicates(input_str)
print(output_str)  # Output: "ca"
