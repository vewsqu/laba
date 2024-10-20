numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
incorrect_word = numbers[4]
summary = sum((numbers[:4] + (numbers[5:])))
length = len(numbers)
correct_word = summary / length
numbers[4] = correct_word
print("Измененный список:", numbers)


