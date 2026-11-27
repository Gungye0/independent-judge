import csv


def average_score(path):
    """CSV 파일의 score 열 평균을 소수 둘째 자리로 반올림해 반환한다."""
    with open(path, newline="", encoding="utf-8") as f:
        scores = [float(row["score"]) for row in csv.DictReader(f)]
    return round(sum(scores) / len(scores), 2)
