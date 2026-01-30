def one_to_one(match: list[int]) -> bool:
    """
    Args:
        match: list of ints corresponding to the n student

    Notes:
        because our algorithm uses hospitals ordered in 1, 2, ..., n as a post condition
        we must only check that there are no duplicates in the match list
    """
    return len(set(match)) == len(match)


def is_stable(
    all_hospital_prefs: list[list[int]],
    all_student_prefs: list[list[int]],
    match: list[int],
) -> bool:

    hospital_to_student = {h: s for h, s in enumerate(match, start=1)}
    student_to_hospital = {s: h for h, s in hospital_to_student.items()}
    student_prefs_dict = {i: l for i, l in enumerate(all_student_prefs, start=1)}
    hospital_prefs_dict = {i: l for i, l in enumerate(all_hospital_prefs, start=1)}

    for hospital, hospital_prefs in hospital_prefs_dict.items():

        # --- This works because match is listed in hospital order 0 -> n
        matched_student = hospital_to_student[hospital]

        for student in hospital_prefs:
            # --- Hospital's most preffered student is their current match ---
            if student == matched_student:
                break

            # --- Get hospital's preffered student's current match ---
            student_current_match = student_to_hospital[student]
            # --- Get hopsital's preffered student's preferences ---
            for student_pref_hospital in student_prefs_dict[student]:
                if student_pref_hospital == student_current_match:
                    break
                # --- Hospital's preffered student is not matched to them
                # but the student also preffers the hospital over it's current match
                elif student_pref_hospital == hospital:
                    return False

    return True
