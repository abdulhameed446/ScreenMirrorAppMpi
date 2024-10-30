@echo off
REM This batch file will run the master executable using MPI

REM Change the path below to the location of your master executable
mpiexec -n 4 "%~dp0dist\master.exe"

pause
