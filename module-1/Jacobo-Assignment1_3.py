"""
Name: Walter Jacobo
Course: CSD325 - Advanced Python
Assignment: Module 1.3 - On the Wall
Date: October 2026
Description: Ask the user for a starting number of bottles, then use a
             function to count down to one bottle. After the song ends,
             remind the user to buy more beer.
"""


def count_bottles(bottles):
    """Print the bottle countdown, using singular wording for one bottle."""
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("Take one down and pass it around,")
        bottles -= 1
        next_bottle = "bottle" if bottles == 1 else "bottles"
        print(f"{bottles} {next_bottle} of beer on the wall.\n")

    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around,")
    print("No more bottles of beer on the wall.\n")


def main():
    """Ask for a positive bottle count, run the song, and print a reminder."""
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? "))
            if bottles > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")

    print()
    count_bottles(bottles)
    print("Time to buy more beer!")


if __name__ == "__main__":
    main()
