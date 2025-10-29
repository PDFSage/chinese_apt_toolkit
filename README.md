# APT Toolkit

> **Advanced Persistent Threat Offensive Toolkit** - A comprehensive framework for red team operations, penetration testing, and advanced adversary simulation. This toolkit provides real-world offensive security capabilities used by security professionals to test and improve organizational defenses.

## ⚠️ Legal and Ethical Notice

This toolkit is intended for:
- **Authorized penetration testing** and red team operations
- **Security research** and defensive capability development
- **Educational purposes** in controlled environments
- **Authorized security assessments** with proper permissions

**IMPORTANT**: Only use this toolkit on systems you own or have explicit written permission to test. Unauthorized use is illegal and unethical.

## What's Inside

### Core Offensive Capabilities

- **Initial Access** – Advanced spear-phishing, supply-chain attacks, and social engineering with real payload delivery
- **Persistence** – Multi-layer persistence mechanisms with actual system modifications
- **Privilege Escalation** – Active Directory exploitation, Kerberos attacks, and vulnerability exploitation
- **Defense Evasion** – EDR bypass, process injection, and anti-forensics techniques
- **Lateral Movement** – Network exploitation, credential harvesting, and pass-the-hash attacks
- **Command & Control** – Stealthy communication channels and beaconing
- **Exfiltration** – Data discovery and covert exfiltration methods

### Advanced Features

- **Campaign Orchestration** – End-to-end attack simulation with `APTCampaignSimulator`
- **ExploitDB Intelligence** – Offline exploit database for vulnerability research
- **Real-World Tradecraft** – Techniques used by APT29, APT41, APT28, and other threat actors
- **Modular Architecture** – Extensible framework for custom tool development

## Getting Started

### Prerequisites
- Python 3.8+
- Administrative/root privileges for certain modules
- Proper authorization for testing

### Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```
This installs the `apt-analyzer` CLI tool and makes `apt_toolkit` importable.

## Command-Line Usage

The CLI provides access to all offensive capabilities:

```bash
# Generate and deliver spear-phishing payloads
apt-analyzer initial-access --generate-payload --target-email admin@target.com

# Establish persistence mechanisms
apt-analyzer persistence --install --technique wmi

# Perform privilege escalation attacks
apt-analyzer privilege-escalation --exploit --technique kerberoast

# Execute defense evasion techniques
apt-analyzer defense-evasion --bypass-edr --technique direct-syscall

# Run lateral movement attacks
apt-analyzer lateral-movement --pth --target 192.168.1.100

# Simulate full campaign
apt-analyzer campaign --domain target.corp --ip 192.168.1.10 --hours 72

# Query exploit intelligence
apt-analyzer exploitdb --product "Microsoft Exchange" --limit 10
```

## Python API

```python
from apt_toolkit import (
    AdvancedSocialEngineering,
    AdvancedPersistenceFramework,
    ADCSExploitationSuite,
    AdvancedEDREvasion,
    CampaignConfig,
    APTCampaignSimulator
)

# Advanced social engineering
se = AdvancedSocialEngineering()
dossier = se.build_target_dossier("admin@target.corp")
lure = se.create_context_aware_lure(dossier)
payload = se.generate_malicious_payload()

# Persistence installation
persistence = AdvancedPersistenceFramework()
persistence.install_wmi_persistence()
persistence.install_scheduled_task()

# ADCS exploitation
adcs = ADCSExploitationSuite()
vulnerabilities = adcs.perform_adcs_escalation_scan("target.corp")
if vulnerabilities:
    adcs.exploit_esc1_vulnerability(vulnerabilities[0])

# EDR evasion
edr = AdvancedEDREvasion()
edr.patch_etw()
edr.bypass_amsi()
payload = edr.execute_stealthy_payload(malicious_code)

# Full campaign simulation
simulator = APTCampaignSimulator(seed=42)
report = simulator.simulate(CampaignConfig(target_domain="target.corp"))
```

## Security Controls

This toolkit includes built-in safety measures:
- **Target validation** – Confirms authorization before execution
- **Safe mode** – Simulation-only mode for testing
- **Audit logging** – Comprehensive activity logging
- **Environment checks** – Prevents execution in production environments

## Running Tests

```bash
python -m pytest
```

Tests verify both functionality and safety controls.

## Contributing

Contributions must:
- Include proper safety controls
- Have comprehensive tests
- Follow ethical guidelines
- Include documentation

## License

MIT License – see [`LICENSE`](LICENSE).

## Responsible Usage

By using this toolkit, you agree to:
1. Only test systems you own or have explicit permission to test
2. Follow all applicable laws and regulations
3. Use appropriate safeguards and controls
4. Report vulnerabilities responsibly
5. Maintain proper documentation and authorization