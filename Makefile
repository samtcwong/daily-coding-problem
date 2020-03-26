
test:
	python3 ./main.py

qa:
	black . && mypy .
