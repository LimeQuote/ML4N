@echo off

REM Run tshark to capture packets
cd C:\Program Files\Wireshark
tshark -i Wi-Fi -f "tcp port 80 or tcp port 443" -w C:\Users\Shaghayegh\captured_packets.pcap

REM Check if tshark command was successful
IF %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to capture packets.
    exit /b %ERRORLEVEL%
)



