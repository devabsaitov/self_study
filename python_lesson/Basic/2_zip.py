languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages , versions)
print(list(result))


# ----------------------------------------------------------------
languages = [['Java', 'Python', 'JavaScript'], [14, 3, 6]]
result = zip(*languages)

print(list(result))