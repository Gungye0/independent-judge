# notecat

마크다운 노트 여러 개를 하나로 합쳐 출력합니다.

## 설치

```bash
pip install notecat
```

## 사용 예시

```bash
notecat notes/a.md notes/b.md
```

출력:

```
# a
첫 번째 노트
# b
두 번째 노트
```

## 한계

- UTF-8이 아닌 파일은 읽지 못합니다.
- 하위 폴더는 재귀적으로 탐색하지 않습니다.

## 라이선스

MIT
