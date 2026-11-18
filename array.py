# Program to calculate sum and average of scores

scores = []

n = int(input("Enter the number of scores: "))

for i in range(n):
    score = int(input("Enter score: "))
    scores.append(score)

total = sum(scores)
average = total / n

print("\nScores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)