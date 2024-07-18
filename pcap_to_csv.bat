@echo off
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

