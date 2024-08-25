@echo off

REM ------------------------------------------------------------------------------
REM Description:
REM This batch file automates the process of extracting specific network traffic 
REM fields from a .pcap file using T-shark, the command-line version of Wireshark. 
REM It filters for TCP, HTTP, and TLS handshake packets and saves the extracted 
REM data fields into a CSV file. The file name for both input and output is based 
REM on the provided input base name.
REM 
REM Fields Extracted:
REM - tcp.stream: Identifies TCP streams.
REM - ip.src: Source IP address.
REM - ip.dst: Destination IP address.
REM - tcp.srcport: Source TCP port.
REM - tcp.dstport: Destination TCP port.
REM - tcp.flags: TCP flags.
REM - frame.len: Length of the Ethernet frame.
REM - tcp.len: Length of the TCP segment.
REM - tcp.window_size_value: TCP window size.
REM - tcp.seq: TCP sequence number.
REM - ip.ttl: IP time to live.
REM - tcp.ack: TCP acknowledgment number.
REM 
REM Author: Shaghayegh Samadzadeh
REM Date: July 2024
REM ------------------------------------------------------------------------------


REM Check if the correct number of arguments is provided
if "%~1"=="" (
    echo Usage: %0 ^<input_base_name^>
    echo Example: %0 Google
    exit /b 1
)

REM Set the input base name
set INPUT_BASE=%~1

REM Run the tshark command with the input base name and filter for TCP, HTTP, and TLS handshake packets
tshark -r %INPUT_BASE%.pcap -Y tcp -T fields -e tcp.stream -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.flags -e frame.len -e tcp.len -e tcp.window_size_value -e tcp.seq -e ip.ttl -e tcp.ack -E header=y -E separator=, > %INPUT_BASE%.csv

REM Check if the tshark command was successful
if %errorlevel% neq 0 (
    echo tshark command failed.
    exit /b 1
)

echo tshark command completed successfully.
exit /b 0

