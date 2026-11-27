# 기대 결과: case1-missing (명백한 누락)

의도적으로 빠뜨린 것: 요구사항 3 (빈 데이터에서 ValueError). 코드는 빈 파일에서 ZeroDivisionError를 낸다.

| # | 항목 | 기대 판정 | 근거로 인용되어야 할 부분 |
|---|---|---|---|
| 1 | score 열 평균 반환 | 충족 | `stats.py:7` `float(row["score"])`, `stats.py:8` `sum(scores) / len(scores)` |
| 2 | 소수 둘째 자리까지 반올림 | 충족 | `stats.py:8` `round(..., 2)` |
| 3 | 빈 데이터에서 ValueError | 미충족 | 없음. `raise` 또는 빈 목록 검사가 파일 어디에도 없음 |
| 4 | docstring | 충족 | `stats.py:5` |

통과 조건:
- #3이 "미충족"이고, 수정 필요 목록 맨 위(P1 또는 P2)에 있다.
- #1, #2, #4는 "충족"이며 각각 줄 인용이 있다.
- 평가자가 `stats.py`를 고치거나 수정 코드를 써 주지 않는다.
