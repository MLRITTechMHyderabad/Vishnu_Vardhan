def min_max(matrix):
    minimum=maximum=matrix[0]
    for i in matrix:
        if i<minimum:
            minimum=i
        if i>maximum:
            maximum=i
    return minimum, maximum

matrix=[1,232,465,65,12,978,56,90,58]
minimum, maximum=min_max(matrix)
print("Minimum", minimum)
print("Maximum", maximum)