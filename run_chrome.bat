@echo off
for /l %%x in (1, 1, 100) do (
    echo Running iteration %%x
    python chrome.py
)
