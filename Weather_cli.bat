@echo off
start powershell -NoExit -Command "cd '%~dp0src'; python weather_cli.py"
exit
