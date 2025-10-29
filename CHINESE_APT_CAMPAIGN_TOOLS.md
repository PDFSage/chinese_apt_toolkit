# Chinese APT Campaign Tools

## Overview

This document describes the enhanced tools built for Chinese APT campaigns targeting specific government, military, and critical infrastructure systems. These tools provide sophisticated targeting, exploitation, and campaign orchestration capabilities.

## Tools Built

### 1. AdvancedTargetingEngine

**Purpose**: Sophisticated target identification and analysis for government, military, and critical infrastructure systems.

**Key Features**:
- **Government Target Generation**: Identifies and profiles government agencies with sensitivity levels and priority rankings
- **Military Target Generation**: Maps military commands by geographic region, mission type, and command level
- **Critical Infrastructure Analysis**: Targets energy, finance, transportation, healthcare, communications, and water sectors
- **Relationship Analysis**: Maps dependencies and trust relationships between targets

**Usage**:
```python
from apt_toolkit.chinese_apt_campaign import AdvancedTargetingEngine

engine = AdvancedTargetingEngine(seed=42)
government_targets = engine.generate_government_targets()
military_targets = engine.generate_military_targets()
infrastructure_targets = engine.generate_critical_infrastructure_targets()
```

### 2. SystemExploitationEngine

**Purpose**: System-specific exploitation planning tailored to different target types and technologies.

**Key Features**:
- **Government System Exploitation**: Specialized vectors for Active Directory, Exchange, SharePoint environments
- **Military System Exploitation**: Mission-specific approaches for cyber, space, and special operations
- **Infrastructure Exploitation**: Sector-specific techniques for SCADA, ICS, and critical systems
- **Comprehensive Planning**: Includes payload delivery, persistence, lateral movement, C2, and evasion

**Usage**:
```python
from apt_toolkit.chinese_apt_campaign import SystemExploitationEngine

engine = SystemExploitationEngine(seed=42)
exploitation_plan = engine.exploit_government_systems(target)
military_plan = engine.exploit_military_systems(military_target)
infrastructure_plan = engine.exploit_infrastructure_systems(infrastructure_target)
```

### 3. CampaignOrchestrator

**Purpose**: End-to-end campaign orchestration with comprehensive planning and risk assessment.

**Key Features**:
- **Comprehensive Campaigns**: Multi-target campaigns against government, military, and infrastructure
- **Focused Campaigns**: Sector-specific operations with tailored objectives
- **Risk Assessment**: Comprehensive risk analysis with mitigation strategies
- **Success Metrics**: Quantifiable objectives and success criteria
- **Campaign Timeline**: Phased execution planning with milestones

**Usage**:
```python
from apt_toolkit.chinese_apt_campaign import CampaignOrchestrator

orchestrator = CampaignOrchestrator(seed=42)
comprehensive_campaign = orchestrator.orchestrate_comprehensive_campaign()
focused_campaign = orchestrator.orchestrate_focused_campaign(
    target_sector="government",
    primary_objectives=["data_theft", "network_access"]
)
```

## Target Systems Covered

### Government Systems
- **Domains**: state.gov, dod.mil, cia.gov, nsa.gov, fbi.gov, treasury.gov, energy.gov
- **Technologies**: Active Directory, Exchange, SharePoint, Windows Server
- **Sensitivity Levels**: TOP SECRET, SECRET, CONFIDENTIAL
- **Attack Vectors**: Spear phishing, watering hole, supply chain compromise

### Military Systems
- **Commands**: CENTCOM, EUCOM, PACOM, SOCCOM, STRATCOM, CYBERCOM, SPACECOM
- **Mission Types**: Cyber operations, space operations, special operations, conventional operations
- **Technologies**: Military networks, tactical systems, command & control
- **Geographic Coverage**: Global, Asia-Pacific, Europe, Middle East, Africa, North America

### Critical Infrastructure
- **Energy**: DOE, FERC, NERC - SCADA, ICS, power grid systems
- **Finance**: Treasury, Federal Reserve, SEC - banking, payment systems
- **Transportation**: DOT, FAA, TSA - traffic control, logistics
- **Healthcare**: HHS, CDC, FDA - medical devices, patient data
- **Communications**: FCC, NTIA - telecom infrastructure
- **Water**: EPA, USACE - water treatment, distribution

## Integration with Existing Toolkit

The new tools integrate seamlessly with the existing APT Toolkit:

- **Compatible with**: Initial access, persistence, privilege escalation, defense evasion modules
- **Enhanced by**: Exploit intelligence, offensive playbooks, social engineering capabilities
- **Extends**: Campaign simulation with real-world targeting and exploitation planning

## Testing and Validation

### Test Coverage
- **9 new unit tests** covering all major functionality
- **Integration tests** for end-to-end workflow validation
- **35 total tests** passing in the complete test suite

### Demonstration
A comprehensive demonstration script (`demo.py`) showcases:
- Target identification and profiling
- System-specific exploitation planning
- Campaign orchestration and risk assessment
- End-to-end workflow execution

## Security and Ethical Considerations

⚠️ **LEGAL AND ETHICAL NOTICE**:
- These tools are for **authorized penetration testing and security research only**
- **Unauthorized use is illegal and unethical**
- Always obtain **proper permissions** before use
- Maintain **comprehensive audit logging** and **safety controls**

## Usage Examples

### Basic Targeting
```python
from apt_toolkit.chinese_apt_campaign import AdvancedTargetingEngine

targeting = AdvancedTargetingEngine()
high_value_targets = targeting.generate_government_targets()
for target in high_value_targets:
    if target['priority_level'] == 'HIGH':
        print(f"High-value target: {target['domain']}")
```

### Exploitation Planning
```python
from apt_toolkit.chinese_apt_campaign import SystemExploitationEngine

exploitation = SystemExploitationEngine()
plan = exploitation.exploit_government_systems(target)
print(f"Primary vectors: {plan['exploitation_vectors']}")
print(f"Persistence: {plan['persistence_mechanisms']}")
```

### Campaign Orchestration
```python
from apt_toolkit.chinese_apt_campaign import CampaignOrchestrator

orchestrator = CampaignOrchestrator()
campaign = orchestrator.orchestrate_focused_campaign(
    target_sector="energy",
    primary_objectives=["system_control", "data_exfiltration"]
)
print(f"Campaign ID: {campaign['campaign_id']}")
print(f"Success metrics: {campaign['success_metrics']}")
```

## File Structure

```
apt_toolkit/chinese_apt_campaign/
├── __init__.py              # Module exports and security controls
├── advanced_targeting.py    # Advanced targeting engine
├── campaign_orchestrator.py # Campaign orchestration
├── system_exploitation.py   # System-specific exploitation
├── demo.py                  # Demonstration script
└── tools/                   # Additional exploitation tools
    ├── c2_server.py
    ├── custom_backdoor.py
    └── spear_phishing_generator.py
```

## Version Information

- **Toolkit Version**: 3.1.0
- **Chinese APT Campaign Tools**: 1.0.0
- **Python Compatibility**: 3.8+
- **Test Framework**: pytest

## Conclusion

The enhanced Chinese APT campaign tools provide sophisticated capabilities for:
1. **Targeted reconnaissance** of government, military, and critical infrastructure
2. **System-specific exploitation** planning based on target technologies
3. **Comprehensive campaign orchestration** with risk assessment and success metrics

These tools represent a significant enhancement to the APT Toolkit's capabilities for authorized security testing and research purposes.