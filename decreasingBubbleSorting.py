# sorting in decreasing order


def bubble_sorting(my_prob):

    n = len(my_prob)
    for i in range(n):

        for j in range(0, n-i-1):

            if my_prob[j] < my_prob[j+1]:
                my_prob[j], my_prob[j+1] = my_prob[j+1], my_prob[j]


my_prob = [int(x) for x in input("Enter the numbers to be sorted with a space between them: ").split()]

bubble_sorting(my_prob)

print("Sorting array is: ")
for i in range(len(my_prob)):
    print(my_prob[i])
