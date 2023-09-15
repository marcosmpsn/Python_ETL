linguagens = ['python', 'csharp', 'java', 'js', 'c']

print(len(linguagens))

print(sorted(linguagens))
print(linguagens)

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))