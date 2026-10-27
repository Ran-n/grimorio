@echo off
setlocal

set "FLAG=%~1"
set "FILE=%~2"

if "%FLAG%"=="" set "FLAG=-h"

if "%FLAG%"=="-h" (
    set "ACTION=help"
) else if "%FLAG%"=="-v" (
    set "ACTION=show"
) else if "%FLAG%"=="-m" (
    set "ACTION=edit"
) else if "%FLAG%"=="-c" (
    set "ACTION=create"
) else if "%FLAG%"=="-d" (
    set "ACTION=remove"
) else (
    echo Unknown flag: %FLAG% 1>&2
    exit /b 1
)

if not "%ACTION%"=="help" if "%FILE%"=="" (
    echo Missing file argument 1>&2
    exit /b 1
)

python "%~dp0metadata_core.py" %ACTION% %FILE%
endlocal
