@echo off
call venv\scripts\activate
pytest -s -v -m "sanity" --html .\reports\test_report.html --browser firefox
rem pytest -s -v -m "regression" --html .\reports\test_report.html --browser firefox
rem pytest -s -v -m "sanity and regression" --html .\reports\test_report.html --browser firefox
rem pytest -s -v -m "sanity or regression" --html .\reports\test_report.html --browser firefox

pause
