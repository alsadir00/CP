# Sometimes some words like “localization” or “internationalization” are so long that writing them many times is tiresome.
# Let's consider a word too long if its length is strictly more than 10 characters.
# All too long words should be replaced with a special abbreviation:

# The abbreviation consists of:

# The first letter of the word,

# The number of letters between the first and last letter,

# The last letter of the word.

# For example:

# "localization" → "l10n"

# "internationalization" → "i18n"

# Words of length 10 or less are left unchanged.

# 📥 Input

# The first line contains an integer n — the number of words.

# Each of the next n lines contains one word.

# 📤 Output

# Print n lines.
# The i-th line should contain the abbreviation of the i-th word (or the same word if it's short enough).


n = int(input())
for _ in range(n):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)

#  or

n = int(input())
for i in range(n):
    inpt = input()
    print(inpt[0] + str(len(inpt) - 2) + inpt[-1] if len(inpt) > 10 else inpt)
