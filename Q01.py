# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
marks=int(input("Enter marks:"))
if(marks<0 or marks>100):
    print("Invalid score")
else:
    if 90<=marks<=100:
        print("Grade : A")
    elif 80<=marks<=89:
        print("Grade: B")
    elif 70<=marks<=79:
        print("Grade : C")
    elif 60<=marks<=69:
        print("Grade : D")
    else:
        print("Grade : F")            
