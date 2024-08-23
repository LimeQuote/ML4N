@echo off
REM =====================================================================================
REM Batch File: run_tshark.bat
REM Description:
REM This batch file is used to capture network traffic using T-shark, a command-line network 
REM protocol analyzer from the Wireshark suite. The script specifically captures TCP traffic 
REM on ports 80 (HTTP) and 443 (HTTPS) over a Wi-Fi interface. The captured traffic is saved 
REM as a .pcap file for further analysis. It also includes error handling to ensure the 
REM capturing process completes successfully.
REM 
REM Author: Shaghayegh Samadzadeh
REM Date: July 2024
REM =====================================================================================


REM Run tshark to capture packets
cd C:\Program Files\Wireshark
tshark -i Wi-Fi -f "tcp port 80 or tcp port 443" -w E:\browser_website_query_100rep\Edge_Bing_Python_100.pcap

REM Check if tshark command was successful
IF %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to capture packets.
    exit /b %ERRORLEVEL%
)



