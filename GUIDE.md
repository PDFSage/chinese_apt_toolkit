# APT Toolkit - Operational Guide for American Targets

## Quick Start

### Installation
```bash
git clone https://github.com/PDFSage/apt_toolkit
cd apt_toolkit
pip install -e .
```

### Basic Usage
```bash
# Analyze American targets
apt-analyzer american targets

# Generate social engineering campaigns
apt-analyzer initial-access --generate-email

# Analyze persistence techniques
apt-analyzer persistence --analyze
```

## American Target Analysis

### Target Categories
- **Government**: .mil, .gov domains
- **Defense Contractors**: Northrop Grumman, Lockheed Martin, Boeing
- **Critical Infrastructure**: Energy, Finance, Transportation

### CLI Commands
```bash
# Comprehensive analysis
apt-analyzer american targets --json

# Social engineering
apt-analyzer initial-access --generate-email

# Persistence analysis
apt-analyzer persistence --analyze

# Privilege escalation
apt-analyzer privilege-escalation --ad-enum
```

## Advanced Techniques

### Social Engineering
```python
from apt_toolkit import AdvancedSocialEngineering

se = AdvancedSocialEngineering()
dossier = se.build_target_dossier("security.admin@dod.mil")
lure = se.create_context_aware_lure(dossier)
```

### Persistence
```python
from apt_toolkit import AdvancedPersistenceFramework

framework = AdvancedPersistenceFramework()
persistence = framework.install_multi_layer_persistence({
    "edr_present": True,
    "target_environment": "government_network"
})
```

### Privilege Escalation
```python
from apt_toolkit import ADCSExploitationSuite

adcs = ADCSExploitationSuite()
scan = adcs.perform_adcs_escalation_scan("dod.mil")
```

## Operational Security

### OPSEC Measures
- Use legitimate traffic patterns
- Operate during business hours
- Rotate C2 infrastructure
- Implement counter-forensics

### Legal Requirements
- Only use on authorized systems
- Maintain proper documentation
- Follow responsible disclosure
- Comply with all applicable laws

## Troubleshooting

### Common Issues
```bash
# Reinstall if needed
pip uninstall apt-toolkit
pip install -e .

# Check Python version
python --version
```

### Debug Mode
```python
import logging
logging.basicConfig(level=logging.DEBUG)

from apt_toolkit import analyze_advanced_social_engineering
result = analyze_advanced_social_engineering()
```

## Full Documentation

For complete documentation, see:
- README.md - Overview and installation
- ENHANCEMENTS_SUMMARY.md - Technical details
- examples/ - Usage examples
- tests/ - Test suite

## Legal Notice

This toolkit is for educational and authorized testing purposes only. Users are responsible for obtaining proper authorization and complying with all applicable laws.