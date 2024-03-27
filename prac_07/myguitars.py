from prac_07.guitar import Guitar

def main():
    guitars = []
    answer = input("Add a new guitar? (Y/N): ").upper()
    while answer != "N":
        guitar_name = input("Guitar name: ")
        guitar_year = int(input("Guitar year: "))
        guitar_cost = float(input("Guitar cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        answer = input("Add more? (Y/N): ").upper()


    in_file = open("guitars.csv", "r")
    for line in in_file:
        words = line.strip().split(",")
        guitar = Guitar(words[0], int(words[1]), float(words[2]))
        guitars.append(guitar)
    guitars.sort()

    for guitar in guitars:
        print(guitar)
    in_file.close()

    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        print(guitar, file=out_file)
    out_file.close()

main()