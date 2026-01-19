@echo off
call .venv\Scripts\activate
pytest -s -v --html .\reports\report.html .\test_cases\full_shopping.py
