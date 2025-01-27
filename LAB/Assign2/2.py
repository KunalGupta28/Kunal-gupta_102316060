scores=(45,89.5,76,45.4,89,92,58,45)
print(scores)
maximum_value=max(scores)
index= scores.index(maximum_value)
print("The maximum score is  :",maximum_value,"and it's index is :",index)
minimum_value=min(scores)
index2= scores.index(minimum_value)
print("The minimum score is  :",minimum_value,"and it's index is :",index2)
def scorestolist(scores):
  return list(scores[::-1])
reversed_list=scorestolist(scores)
print(reversed_list)

if 76 in scores:
    print(f"Score 76 found at index {scores.index(76)}")
else:
    print("Score 76 is not present in the tuple.")