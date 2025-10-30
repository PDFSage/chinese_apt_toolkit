# Real Target Campaign Execution Guide

This guide explains how to execute APT campaigns against real targets using the enhanced campaign execution system.

## Overview

The real target campaign execution system provides:
- **Target validation** before campaign execution
- **Safety controls** including dry-run mode
- **Comprehensive reporting** with detailed execution logs
- **Chinese APT campaign support** for APT41, APT1, APT10, and APT12
- **Multiple target sets** for different industries and sectors

## Quick Start

### 1. List Available Campaigns
```bash
python3 real_target_campaign_runner.py --list-campaigns
```

### 2. List Available Target Sets
```bash
python3 real_target_campaign_runner.py --list-targets
```

### 3. Validate Targets (No Execution)
```bash
python3 real_target_campaign_runner.py --validate-only --target-set defense_contractor
```

### 4. Dry Run Campaign
```bash
python3 real_target_campaign_runner.py --campaign defense_contractor_campaign --target-set defense_contractor --dry-run
```

### 5. Execute Campaign
```bash
python3 real_target_campaign_runner.py --campaign defense_contractor_campaign --target-set defense_contractor
```

### 6. Execute All Campaigns
```bash
python3 real_target_campaign_runner.py --campaign all --target-set defense_contractor --dry-run
```

## Chinese APT Campaigns

### Execute Specific APT Group
```bash
python3 campaigns/chinese_apt_real_targets.py --campaign apt41 --target-set defense_contractor
```

### Execute All Chinese APT Campaigns
```bash
python3 campaigns/chinese_apt_real_targets.py --campaign all --target-set defense_contractor
```

## Target Configuration

Targets are configured in `campaign_targets.json`. The system includes predefined test targets:

- **defense_contractor**: Test defense industry targets
- **financial_institution**: Banking and finance targets
- **government_agency**: Government and agency targets
- **healthcare**: Medical and healthcare targets
- **energy_sector**: Power and energy infrastructure

### Example Target Configuration
```json
{
  "test_targets": {
    "defense_contractor": {
      "domains": ["test.defense.example.com", "test.contractor.example.com"],
      "ips": ["10.0.1.10", "10.0.1.11"],
      "ports": [80, 443, 8080],
      "services": ["http", "https", "ssh"],
      "description": "Test defense contractor targets"
    }
  }
}
```

## Campaign Execution Phases

Each campaign executes through these phases:

1. **Target Validation** - Verify targets are reachable
2. **Reconnaissance** - Gather information about targets
3. **Initial Access** - Establish foothold in target environment
4. **Persistence** - Maintain access across reboots
5. **Privilege Escalation** - Gain higher privileges
6. **Defense Evasion** - Avoid detection
7. **Lateral Movement** - Move through the network
8. **Collection** - Gather target data
9. **Command & Control** - Maintain communication
10. **Exfiltration** - Transfer data out

## Safety Controls

### Dry Run Mode
Always use dry-run mode first to validate without execution:
```bash
--dry-run
```

### Target Validation
Validate targets before execution:
```bash
--validate-only
```

### Execution Timeouts
Campaigns have built-in timeouts to prevent hanging:
- Individual campaigns: 5 minutes
- Validation operations: 5 seconds

## Output and Reporting

### Execution Reports
Campaigns generate detailed JSON reports:
- `campaign_execution_YYYYMMDD_HHMMSS.json`
- `campaign_run_YYYYMMDD_HHMMSS.log`

### Report Structure
```json
{
  "execution_timestamp": "2024-01-01T12:00:00",
  "total_campaigns": 5,
  "executions": [
    {
      "campaign": "defense_contractor_campaign",
      "target_set": "defense_contractor",
      "status": "completed",
      "phases": {...}
    }
  ],
  "validator_results": {...}
}
```

## Available Campaigns

### Infrastructure Campaigns
- `defense_contractor_campaign` - Defense industry targeting
- `financial_institution_campaign` - Banking and finance
- `government_agency_campaign` - Government organizations
- `energy_company_campaign` - Power infrastructure
- `telecommunications_campaign` - Communication networks

### Industry Campaigns
- `aerospace_company_campaign` - Aerospace industry
- `automotive_company_campaign` - Automotive manufacturers
- `pharmaceutical_company_campaign` - Pharmaceutical companies
- `healthcare_campaign` - Healthcare providers
- `manufacturing_company_campaign` - Manufacturing sector

### Technology Campaigns
- `cloud_infrastructure_campaign` - Cloud service providers
- `ai_company_campaign` - Artificial intelligence companies
- `iot_botnet_campaign` - Internet of Things devices
- `quantum_computing_campaign` - Quantum computing research

### Chinese APT Campaigns
- `apt41_campaign_enhanced` - Gaming industry and supply chain
- `chinese_apt_lockheed_campaign` - Defense contractor targeting
- `chinese_apt_real_targets.py` - Comprehensive APT execution

## Chinese APT Groups Supported

### APT41 (Winnti Group)
- **Focus**: Gaming industry, supply chain attacks
- **TTPs**: Polyglot payloads, multi-stage malware
- **Targets**: Game developers, publishers, virtual economies

### APT1 (Comment Crew)
- **Focus**: Government, military, critical infrastructure
- **TTPs**: Spear phishing, long-term persistence
- **Targets**: Defense contractors, government agencies

### APT10 (Cloud Hopper)
- **Focus**: Cloud providers, managed service providers (MSPs)
- **TTPs**: Cloud hopping, API key theft
- **Targets**: Cloud infrastructure, MSP customers

### APT12 (Numbered Panda)
- **Focus**: Diplomatic targets, media, NGOs
- **TTPs**: Watering hole attacks, journalist targeting
- **Targets**: Embassies, think tanks, media organizations

## Best Practices

### 1. Always Validate First
```bash
python3 real_target_campaign_runner.py --validate-only --target-set <target>
```

### 2. Use Dry Run Mode
```bash
python3 real_target_campaign_runner.py --campaign <campaign> --target-set <target> --dry-run
```

### 3. Review Reports
Always examine execution reports before proceeding to actual execution.

### 4. Monitor Execution
Campaigns generate detailed logs - monitor them for any issues.

### 5. Use Appropriate Target Sets
Match campaign types with appropriate target sets for realistic simulations.

## Troubleshooting

### Common Issues

1. **"No valid targets found"**
   - Check target configuration in `campaign_targets.json`
   - Verify network connectivity to test targets
   - Use `--validate-only` to debug target reachability

2. **Campaign execution timeout**
   - Check if campaign scripts are properly configured
   - Verify all required dependencies are installed
   - Review campaign logs for specific errors

3. **Import errors**
   - Ensure all campaign dependencies are available
   - Check Python path and module imports
   - Verify campaign scripts are in correct locations

### Debug Mode
Enable debug logging for detailed troubleshooting:
```bash
python3 -c "import logging; logging.basicConfig(level=logging.DEBUG)" real_target_campaign_runner.py [options]
```

## Security Considerations

⚠️ **IMPORTANT**: This system is designed for authorized testing and research only.

- Only execute against targets you own or have explicit permission to test
- Use test targets in controlled environments for development
- Never execute campaigns against production systems without authorization
- Always use dry-run mode first to validate operations
- Monitor all campaign activities and maintain detailed logs

## Legal and Ethical Use

This tool is intended for:
- Security research and education
- Authorized penetration testing
- Red team exercises with proper scope
- Defensive security training

Unauthorized use against systems you do not own or have explicit permission to test is illegal and unethical.

---

For questions or issues, refer to the campaign execution logs and validation reports generated by the system.