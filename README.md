### Python - fastAPI

> fastAPI가 얼마나 빠르고 쉬운지 채감해보기 위해 공부를 시작해보자

1. **가상환경 관련**

```
1) Python 설치
brew install python@3.12

2) 가상환경 생성
python3.12 -m venv .venv
source .venv/bin/activate

3) fastAPI 설치
pip install "fastapi[standard]"

3-1) 프로젝트에서 사용하는 의존성 대로 사용할 경우
pip install -r requirements.txt

3-2) 가상환경에 설치된 라이브러리 파일로 저장
pip freeze > requirements.txt
```

2. 프로젝트 구조

```
app/
├── __init__.py
├── main.py
├── api/routes/       # Controller
├── schemas/          # DTO
├── services/         # Service
└── repositories/     # Repository
```
