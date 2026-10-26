"""Read programming languages from a CSV file."""

from programming_language import ProgrammingLanguage


def main():
    """Load programming language objects and display them."""
    languages = load_languages("languages.csv")
    for language in languages:
        print(language)


def load_languages(filename):
    """Read a CSV file and return a list of language objects."""
    languages = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            reflection = parts[2] == "Yes"
            year = int(parts[3])
            pointer_arithmetic = parts[4] == "Yes"
            language = ProgrammingLanguage(
                parts[0], parts[1], reflection, year, pointer_arithmetic
            )
            languages.append(language)
    return languages


main()
