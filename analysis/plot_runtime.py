import csv
from pathlib import Path
import matplotlib.pyplot as plt

DATA = Path(__file__).parent
CSV = DATA / "results.csv"

def main():
    n = []
    matcher = []
    verifier = []

    with CSV.open() as f:
        r = csv.DictReader(f)
        for row in r:
            n.append(int(row["n"]))
            matcher.append(float(row["matcher_time"]))
            verifier.append(float(row["verifier_time"]))

    plt.plot(n, matcher, marker="o", label="Matcher")
    plt.plot(n, verifier, marker="o", label="Verifier")
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Runtime vs n")
    plt.legend()
    plt.savefig(DATA / "runtime_plot.png", dpi=200)

if __name__ == "__main__":
    main()
