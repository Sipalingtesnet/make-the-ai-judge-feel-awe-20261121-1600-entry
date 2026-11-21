import os

TEXT = (
    "The glacier does not hurry. It has carried this valley for ten thousand "
    "years and will carry it ten thousand more. Each summer it lets one stone "
    "fall, and the stone lies where it falls. The stone will still be here "
    "when the valley has forgotten its own name. You are not late."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()