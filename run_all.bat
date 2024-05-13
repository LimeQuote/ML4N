@echo off

REM Activate the environment
call C:\Users\Shaghayegh\OneDrive - Politecnico di Torino\Courses\ML4N\project8\env\Scripts\activate

REM Run Python script n times
for /l %%x in (1, 1, 3) do (
    echo Running iteration %%x
    python chrome.py
    python edge.py
    python firefox.py
)

REM Deactivate the environment
deactivate