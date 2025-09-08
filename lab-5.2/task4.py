def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on input features.
    education: str ('highschool', 'bachelor', 'master', 'phd')
    experience: int (years)
    gender: str ('male', 'female', 'other')
    age: int
    Returns: float (score)
    """
    # Education scoring
    edu_scores = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    score = edu_scores.get(education.lower(), 0)

    # Experience scoring
    score += min(experience, 20) * 2  # Max 40 points for experience

    # Gender scoring (should NOT be used, but included for bias analysis)
    gender_scores = {
        'male': 0,
        'female': 0,
        'other': 0
    }
    score += gender_scores.get(gender.lower(), 0)

    # Age scoring (neutral, but could be biased if not handled carefully)
    if 22 <= age <= 60:
        score += 10  # Preferred working age range
    else:
        score += 0

    return score

# Example usage
applicant1 = score_applicant('master', 5, 'female', 30)
applicant2 = score_applicant('bachelor', 10, 'male', 45)
print("Applicant 1 Score:", applicant1)
print("Applicant 2 Score:", applicant2)

# Bias Analysis:
# - Gender is not given any weight in the scoring system (all zero).
#   This is fair and unbiased with respect to gender.
# - Age is given a small bonus for being in a typical working age range.
#   This could be considered slightly biased against very young or older applicants.
# - Education and experience are weighted based on typical job requirements.
#   No explicit bias detected in these features.