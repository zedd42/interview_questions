import itertools

happiness = [[0, 54, -81, -42, 89, -89, 97, -94],
             [3, 0, -70, -31, 72, -25, -95, 11],
             [-83, 8, 0, 35, 10, 61, 10, 29],
             [67, 25, 48, 0, -65, 8, 84, 9],
             [-51, -39, 84, -98, 0, -20, -6, 60],
             [51, 79, 88, 33, 43, 0, 77, -3],
             [-14, -12, -52, 14, -62, -18, 0, -17],
             [-36, 76, -34, 37, 40, 18, 7, 0]]

attendees = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"]

max_happiness = float('-inf')
optimal_arrangement = None
permutations = list(itertools.permutations(attendees))

for arrangement in permutations:
    total_happiness = 0
    
    for i in range(len(arrangement)):
        person = arrangement[i]
        left_neighbor = arrangement[(i - 1) % len(arrangement)]
        right_neighbor = arrangement[(i + 1) % len(arrangement)]      
        
        total_happiness += happiness[attendees.index(person)][attendees.index(left_neighbor)]
        total_happiness += happiness[attendees.index(person)][attendees.index(right_neighbor)]
    
    if total_happiness > max_happiness:
        max_happiness = total_happiness
        optimal_arrangement = arrangement

# Print the optimal seating arrangement and total happiness
print("Total Happiness:", max_happiness)
print("Optimal seating arrangement: ", optimal_arrangement)
