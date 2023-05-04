"""YT: https://youtu.be/sra7rd64PDY
Showing a functional but wild way to print a line in python.
"""

print(*["=" for _ in range(80)], sep="")  # initial statement
print(''.join(["=" for _ in range(80)]))  # removing separator
print('=' * 80)  # simpler version ¯\_(ツ)_/¯
