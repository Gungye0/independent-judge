# independent-judge

작업 결과물을 원래 요구사항에만 비추어 독립적으로 평가하는 Claude 스킬입니다. 결과물을 만든 과정(추론, 대화 기록)은 보지 않고, **요구사항**과 **결과물** 두 가지만 입력으로 받습니다.

- 요구사항을 체크리스트 항목으로 분해
- 항목마다 충족 / 부분 충족 / 미충족 판정, 결과물의 구체적인 부분을 인용해 근거 제시
- 수정이 필요한 항목을 우선순위(P1~P3) 순으로 정리
- 결과물을 직접 고치지 않음

## 설치

복사:

```bash
mkdir -p ~/.claude/skills && cp -r independent-judge ~/.claude/skills/independent-judge
```

또는 git clone:

```bash
git clone https://github.com/<사용자>/independent-judge.git ~/.claude/skills/independent-judge
```

프로젝트 단위로 쓰려면 `~/.claude/skills/` 대신 프로젝트의 `.claude/skills/`에 넣습니다.

## 사용 예시

```
independent-judge로 평가해 줘.
요구사항: docs/spec.md
결과물: src/stats.py
```

출력은 [references/checklist-template.md](references/checklist-template.md) 형식의 보고서입니다.

```
| # | 요구사항 항목 | 요구사항 원문 | 판정 | 근거 (결과물 인용) | 부족한 부분 |
| 3 | 빈 데이터에서 ValueError | "데이터 행이 하나도 없으면 ValueError" | 미충족 | 없음. 찾아본 곳: stats.py 전체 | 빈 목록 검사와 raise 없음 |
```

독립성을 높이려면 결과물을 만든 대화와 다른 새 세션이나 서브에이전트에서 실행하세요. 같은 대화 안에서 부르면 모델이 이미 본 생성 과정을 완전히 잊게 할 수는 없습니다.

## 테스트

```bash
python3 tests/test_frontmatter.py
```

`tests/case1-missing`(명백한 누락)와 `tests/case2-partial`(부분 충족)에 샘플, 요구사항, 기대 결과(`expected.md`)가 있습니다. 실제 실행 결과는 [tests/results.md](tests/results.md)에 있습니다.

## 한계

- 판정은 모델의 판단입니다. 인용을 강제해 반박할 수 있게 했지만, 판정이 틀릴 수 있으니 근거를 직접 확인하세요.
- 코드를 실행해 동작을 확인하지 않습니다. 결과물의 텍스트만 근거로 씁니다.
- 요구사항이 모호하면 분해 결과가 평가자마다 다를 수 있습니다.
- 같은 대화 안에서 실행하면 생성 과정의 영향을 완전히 막을 수 없습니다.

## 라이선스

MIT. [LICENSE](LICENSE) 참고.
