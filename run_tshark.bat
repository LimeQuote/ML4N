@echo off

REM Run tshark to capture packets
cd C:\Program Files\Wireshark
tshark -i Wi-Fi -f "tcp port 80 or tcp port 443" -w E:\browser_website_query_50rep\Chrome_Google_MachineLearning.pcap

REM Check if tshark command was successful
IF %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to capture packets.
    exit /b %ERRORLEVEL%
)



