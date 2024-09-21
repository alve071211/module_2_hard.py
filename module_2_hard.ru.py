numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

n = int(input("Введите число от 3 до 20: "))

pairs = set()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if n % (numbers[i] + numbers[j]) == 0:
            pairs.add((numbers[i], numbers[j]))
            sorted_pairs = sorted(pairs)

result = sorted_pairs

print(f"Нужный пароль: {result}")