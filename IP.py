set ip=10.65.1.
for /l %%i in (2,1,254) do (
netsh interface ip set address "Wireless Network Connection" static %ip%%%i% 255.255.254.0 10.65.0.1
timeout 5
ping -n 1 173.194.117.18 > D:\IP\%%i%.txt
)

