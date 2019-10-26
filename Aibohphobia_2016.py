test1 = "aibohphobia"
test2 = "foobar"
test3 = "abba"
test4 = "aabaa"
test5 = "aba"
tests = [test1, test2, test3, test4, test5]


def palindrome_recursive_test(word):
    if len(word) == 1:
        return None

    if len(word) == 2:
        if word[0] == word[-1]:
            return None
        else:
            return "NOT PALINDROME"

    if word[0] == word[-1]:
        palindrome_recursive_test(word[1:-1])
    else:
        return "NOT PALINDROME"

for t in tests:
    out = palindrome_recursive_test(t)
    if out is None:
        print("PALINDROME")
    else:
        print("NOT PALINDROME")
