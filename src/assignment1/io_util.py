class InputError(Exception):
    pass

def _parse_ints(line):
    parts = line.strip().split()
    if not parts:
        return []
    try:
        return [int(x) for x in parts]
    except ValueError:
        raise InputError("Non-integer token found.")

def _check_perm(vals, n, who, idx):
    if len(vals) != n:
        raise InputError(f"{who} preference line {idx} has wrong length.")
    s = set(vals)
    if len(s) != n:
        raise InputError(f"{who} preference line {idx} has duplicates.")
    if min(s) < 1 or max(s) > n:
        raise InputError(f"{who} preference line {idx} has out-of-range values.")
    if s != set(range(1, n + 1)):
        raise InputError(f"{who} preference line {idx} is not a permutation.")

def read_preferences(path):
    try:
        raw = open(path, "r", encoding="utf-8").read().splitlines()
    except FileNotFoundError:
        raise InputError("File not found.")
    if len(raw) == 0 or all(line.strip() == "" for line in raw):
        raise InputError("Empty input.")
    lines = [ln for ln in raw if ln.strip() != ""]
    n_list = _parse_ints(lines[0])
    if len(n_list) != 1:
        raise InputError("First line must be a single integer.")
    n = n_list[0]
    if n <= 0:
        raise InputError("n must be positive.")
    prefs = lines[1:]
    if len(prefs) != 2 * n:
        raise InputError("Wrong number of preference lines.")
    hospital_prefs = []
    student_prefs = []
    for i in range(n):
        vals = _parse_ints(prefs[i])
        _check_perm(vals, n, "Hospital", i + 1)
        hospital_prefs.append(vals)
    for i in range(n):
        vals = _parse_ints(prefs[n + i])
        _check_perm(vals, n, "Student", i + 1)
        student_prefs.append(vals)
    return n, hospital_prefs, student_prefs
