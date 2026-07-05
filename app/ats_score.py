def calculate_ats_score(similarity, matched, total):
    if total == 0:
        return 0

    skill_score = (matched / total) * 100

    ats = (0.6 * similarity) + (0.4 * skill_score)

    return round(ats, 2)