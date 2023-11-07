text = input("Въведете текст: ")
text = text.lower()  # Превръщаме всички букви в малки, за да не зависи от големина

vowels = "aeiou"
values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

total_value = 0

for letter in text:
    if letter in vowels:
        total_value += values[letter]

print(f"Сумата на стойностите на гласните букви в текста е: {total_value}")
