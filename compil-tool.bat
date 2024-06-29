@Echo off
@Mode 54,40
@Title %~n0
color 9F

rem MUST BE THERE IF YOU CALL FROM ANOTHER BATCH
call :%*

Batbox /h 0

:base
rem @Mode 54,50
@Mode 54,20
path=%path%%cd%\button;
@Echo off
cls
Call Button  5 2 " Compile C++ " 5 5 " Compile C   " 27 2 " Run app C++ " 27 5 " Run app C   " # Press
Getinput /m %Press% /h 70
if %errorlevel%==1 (goto Compile_Cplus)
if %errorlevel%==2 (goto Compile_C)
if %errorlevel%==3 (goto Run_Cplus)
if %errorlevel%==4 (goto Run_C)
goto base

:Compile_Cplus
cls
@Echo on
g++ test_c++.cpp -o app_C++.exe
REM start compile.bat compile_CCplus
pause
goto base

:Compile_C
cls
@Echo on
g++ test_c.c -o app_C.exe
REM start compile.bat compile_CC
pause
goto base

:Run_Cplus
cls
@Echo on
start app_C++.exe
pause
goto base

:Run_C
cls
@Echo on
start app_C.exe
pause
goto base