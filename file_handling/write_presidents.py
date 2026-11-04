from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.txt")


def main():
    presidents = ["George Washington", "Bill Clinton", "Ronald Reagan",
                  "Barack Obama", "Franklin Roosevelt"]
    DATA_FILE.write_text("\n".join(presidents) + "\n", encoding="utf-8")
    print(f"Wrote {DATA_FILE.name}")


if __name__ == "__main__":
    main()
