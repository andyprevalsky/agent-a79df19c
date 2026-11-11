def collatz(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


sequence = collatz(27)
for number in sequence:
    print(number)
print(f"Steps: {len(sequence) - 1}")
