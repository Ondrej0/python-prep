#Task 1
def get_grade(score):
    if score >= 70:
        return "First"
    elif score >= 60:
        return "2:1"
    elif score >= 50:
        return "2:2"
    elif score >= 40:
        return "Third"
    else:
        return "Fail"

scores = [83, 67, 52, 44, 32]

for score in scores:
    print(f"{score}: {get_grade(score)}")