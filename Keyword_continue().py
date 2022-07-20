# Python continue Keyword

# Example
# Skip the iteration if the variable i is 3, but continue with the next iteration:

for i in range(9):
  if i == 3:
    continue
  print(i)

# Definition and Usage
# The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

# More Examples
# Example
# Use the continue keyword in a while loop:

i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)

# Related Pages
# Use the break keyword to end the loop completely.
# Read more about for loops in our Python For Loops Tutorial.
# Read more about while loops in our Python While Loops Tutorial.


