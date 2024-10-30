@echo off
REM This batch file will run the slave executable using MPI

REM Change the path below to the location of your slave executable
mpiexec -n 1 "%~dp0dist\slave.exe"

pause
