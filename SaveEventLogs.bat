@echo off
setlocal enabledelayedexpansion

set "LOGFOLDER=%~dp0EventLogs"
set "ZIPFILE=%~dp0EventLogs.zip"

REM Create a directory to store the exported logs
if not exist "%LOGFOLDER%" mkdir "%LOGFOLDER%"

REM Export each log file
for /f "tokens=*" %%a in ('wevtutil el') do (
    set "LOGNAME=%%a"
    set "LOGNAME=!LOGNAME::=!"
    wevtutil epl "%%a" "%LOGFOLDER%\!LOGNAME!.evtx"
)

REM Zip the exported logs
tar -a -c -f "%ZIPFILE%" "%LOGFOLDER%"

REM Clean up the exported log files
rmdir /s /q "%LOGFOLDER%"

echo Event logs have been exported and zipped.
pause
