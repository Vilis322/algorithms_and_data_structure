def compute_hash(string, base=256, prime_number=101) -> int:
    """Computes the hash of a given string using polynomial rolling hash.

    This function uses a base and a prime number to compute a hash value
    for the input string. Each character's ASCII value is multiplied by
    the base raised to an appropriate power, and the result is taken modulo
    a prime to keep the value within bounds.

    Args:
        string (str): The input string to hash.
        base (int): The base value for polynomial hashing (default is 256).
        prime_number (int): A prime number used for modulus (default is 101).

    Returns:
        int: The computed hash value.
    """
    hash_value = 0
    length = len(string)

    for i in range(length):
        char = string[i]
        exponent = length - i - 1
        term = (ord(char) * (base ** exponent)) % prime_number
        hash_value = (hash_value + term) % prime_number

    return hash_value


def rabin_karp(text, pattern, base=256, prime=101) -> list:
    """Finds all occurrences of a pattern string within a text using Rabin-Karp algorithm.

    The algorithm uses hashing to efficiently search for the pattern in the text.
    It computes the hash of the pattern and compares it with hashes of substrings
    of the same length in the text. When hashes match, the actual strings are
    compared to confirm a match.

    Args:
        text (str): The full text in which to search.
        pattern (str): The substring pattern to find.
        base (int): The base used for hashing (default is 256).
        prime (int): A prime number used as a modulus for hashing (default is 101).

    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)

    pattern_hash = compute_hash(pattern, base, prime)
    substring_hash = compute_hash(text[:m], base, prime)
    occurrences = []

    high_power = pow(base, m - 1, prime)

    for i in range(n - m + 1):
        if substring_hash == pattern_hash:
            if text[i:i + m] == pattern:
                occurrences.append(i)

        if i < n - m:
            old_char = ord(text[i])
            new_char = ord(text[i + m])

            substring_hash = (
                (substring_hash - old_char * high_power) * base + new_char
            ) % prime

            if substring_hash < 0:
                substring_hash += prime

    return occurrences


# example usage
text = "CODEWITHCODER"
pattern = input()
occurrences = rabin_karp(text, pattern)
if occurrences:
    print(f"The pattern found at indices: {occurrences}.")
else:
    print(f"The pattern is not present in the text.")
