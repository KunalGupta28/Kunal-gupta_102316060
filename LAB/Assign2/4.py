A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
unique_scores = A.union(B)
print(f"Unique scores (union): {unique_scores}")
common_scores = A.intersection(B)
print(f"Common scores (intersection): {common_scores}")
exclusive_scores = A.symmetric_difference(B)
print(f"Exclusive scores (symmetric difference): {exclusive_scores}")
is_A_subset_B = A.issubset(B)
is_B_superset_A = B.issuperset(A)
print(f"A is a subset of B: {is_A_subset_B}")
print(f"B is a superset of A: {is_B_superset_A}")
X = int(input("Enter the score to remove from set A: "))
if X in A:
    A.remove(X)
    print(f"Score {X} removed from set A.")
else:
    print(f"Score {X} is not present in set A.")
