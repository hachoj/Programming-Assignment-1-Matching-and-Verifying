from collections import deque

def gale_shapely(n, hospital_prefs, student_prefs):
    student_rank = [[0] * (n + 1) for _ in range(n + 1)]
    for s in range(1, n + 1):
        prefs = student_prefs[s - 1]
        for r, h in enumerate(prefs):
            student_rank[s][h] = r

    hospital_match = [-1] * (n + 1)
    student_match = [-1] * (n + 1)
    next_idx = [0] * (n + 1)

    free = deque(range(1, n + 1))

    while free:
        h = free.popleft()

        if hospital_match[h] != -1:
            continue

        if next_idx[h] >= n:
            continue

        s = hospital_prefs[h - 1][next_idx[h]]
        next_idx[h] += 1

        if student_match[s] == -1:
            student_match[s] = h
            hospital_match[h] = s
        else:
            cur = student_match[s]
            if student_rank[s][h] < student_rank[s][cur]:
                student_match[s] = h
                hospital_match[h] = s
                hospital_match[cur] = -1
                free.append(cur)
            else:
                if next_idx[h] < n:
                    free.append(h)

    return hospital_match[1:]
