"""Wimbledon Winners Summary
"""

FILENAME = "wimbledon.csv"

def main():
    data = load_wimbledon_data(FILENAME)
    champions_to_wins, countries = process_wimbledon_data(data)
    display_champions(champions_to_wins)
    display_countries(countries)

def load_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        return [line.strip().split(",") for line in in_file]

def process_wimbledon_data(data):
    champions_to_wins = {}
    countries = set()
    for row in data:
        champion, country = row[2], row[1]
        champions_to_wins[champion] = champions_to_wins.get(champion, 0) + 1
        countries.add(country)
    return champions_to_wins, countries

def display_champions(champions_to_wins):
    print("Wimbledon Champions:")
    for name, wins in champions_to_wins.items():
        print(f"{name} {wins}")

def display_countries(countries):
    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()
