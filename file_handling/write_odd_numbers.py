from pathlib import Path

OUTPUT_FILE = Path(__file__).with_name("odds.txt")


def main():
    OUTPUT_FILE.write_text(" ".join(str(i) for i in range(1, 100, 2)) + "\n",
                           encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
