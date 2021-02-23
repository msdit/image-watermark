@echo off
set /P year=Enter YEAR (1399):
set /P month=Enter MONTH (05):
set /P day=Enter DAY (09):
set /P hour=Enter HOUR (14):
echo %year%/%month%/%day% %hour% > input.txt
%LOCALAPPDATA%\Programs\Python\Python39\python "./app.py"