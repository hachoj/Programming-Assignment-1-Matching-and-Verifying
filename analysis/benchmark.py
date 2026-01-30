import random
import subprocess
import sys
import time
from pathlib import Path

NS = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
REPEATS = 5

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
TMP_IN = ANALYSIS / "_tmp.in"
TMP_OUT = ANALYSIS / "_tmp.out"
CSV = ANALYSIS / "results.csv"


def gen_instance(n):
    lines = [str(n)]
    for _ in range(n):
        p = list(range(1, n + 1))
        random.shuffle(p)
        lines.append(" ".join(map(str, p)))
    for _ in range(n):
        p = list(range(1, n + 1))
        random.shuffle(p)
        lines.append(" ".join(map(str, p)))
    return "\n".join(lines) + "\n"


def run_matcher():
    with TMP_OUT.open("w", encoding="utf-8") as out:
        subprocess.run(
            [sys.executable, str(ROOT / "analysis/matcher_test.py"), "-i", str(TMP_IN)],
            stdout=out,
            stderr=subprocess.DEVNULL,
            check=True,
        )


def run_verifier():
    subprocess.run(
        [sys.executable, str(ROOT / "analysis/verifier_test.py"), str(TMP_IN), str(TMP_OUT)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )


def main():
    ANALYSIS.mkdir(exist_ok=True)

    with CSV.open("w", encoding="utf-8") as f:
        f.write("n,matcher_time,verifier_time\n")

        for n in NS:
            TMP_IN.write_text(gen_instance(n), encoding="utf-8")

            matcher_times = []
            verifier_times = []

            for _ in range(REPEATS):
                t0 = time.perf_counter()
                run_matcher()
                matcher_times.append(time.perf_counter() - t0)

                t1 = time.perf_counter()
                run_verifier()
                verifier_times.append(time.perf_counter() - t1)

            f.write(
                f"{n},{sum(matcher_times)/len(matcher_times)},{sum(verifier_times)/len(verifier_times)}\n"
            )


if __name__ == "__main__":
    main()
