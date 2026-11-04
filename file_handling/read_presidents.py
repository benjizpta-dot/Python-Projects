from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.txt")


def main():
    if not DATA_FILE.is_file():
        print("data.txt does not exist. Run write_presidents.py first.")
        return
    print(DATA_FILE.read_text(encoding="utf-8").splitlines())


if __name__ == "__main__":
    main()
