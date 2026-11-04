from pathlib import Path

COUNTRIES_FILE = Path(__file__).with_name("countries.txt")


def main():
    countries = [name.strip() for name in
                 COUNTRIES_FILE.read_text(encoding="utf-8").replace(",", "\n").splitlines()
                 if name.strip()]
    countries.sort()
    COUNTRIES_FILE.write_text("\n".join(countries) + "\n", encoding="utf-8")
    print(countries)


if __name__ == "__main__":
    main()
