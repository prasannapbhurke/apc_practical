def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in "aeiou")

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    clean = "".join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]

def count_words(s):
    return len(s.split())

def remove_spaces(s):
    return s.replace(" ", "")
