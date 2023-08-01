# Fermat's Last Theorem Near Miss Finder
# File Name: fermat_near_miss.py
# Programmers: Rohith ch
# Date: 31-072023
# Description: This program finds near misses for Fermat's Last Theorem.

def main():
    # Get user input for n and k
    n = int(input("Enter a value for n (2 < n < 12): "))
    k = int(input("Enter a value for k (k > 10): "))

    smallest_relative_miss = float('inf')
    best_combination = ()

    for x in range(10, k+1):
        for y in range(10, k+1):
            sum_xy = x**n + y**n
            z = int(sum_xy**(1/n))
            
            # Calculate the two possible misses
            miss1 = abs(sum_xy - z**n)
            miss2 = abs((z+1)**n - sum_xy)

            # Determine the smaller miss
            if miss1 < miss2:
                actual_miss = miss1
                z_value = z
            else:
                actual_miss = miss2
                z_value = z + 1

            relative_miss = actual_miss / sum_xy

            # Update the smallest relative miss if necessary
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_combination = (x, y, z_value)

                # Display the current best combination
                print(f"x: {x}, y: {y}, z: {z_value}, Actual Miss: {actual_miss}, Relative Miss: {relative_miss:.2%}")

    # Display the final best combination
    print(f"Best Combination: {best_combination}, Smallest Relative Miss: {smallest_relative_miss:.2%}")

if __name__ == "__main__":
    main()
