# Red Team Real Targets Campaign Guide

This guide explains how to execute APT campaigns against real targets using the enhanced red team campaign execution system with retry logic until success.

## Overview

The red team campaign execution system provides:
- **Retry logic** - Automatically retries failed campaigns until success
- **Success detection** - Intelligent detection of successful campaign execution
- **Comprehensive reporting** - Detailed execution logs and success metrics
- **Multiple target sets** - Pre-configured targets for different industries
- **Safety controls** - Dry-run mode and validation checks

## Quick Start

### 1. List Available Campaigns
```bash
python3 red_team_real_targets_runner.py --list-campaigns
```

### 2. List Available Target Sets
```bash
python3 red_team_real_targets_runner.py --list-targets
```

### 3. Execute Single Campaign with Retry Logic
```bash
python3 red_team_real_targets_runner.py --campaign defense_contractor_campaign --target-set defense_aerospace
```

### 4. Execute All Campaigns Until Success
```bash
python3 red_team_real_targets_runner.py --campaign all --target-set defense_aerospace
```

### 5. Dry Run (Safe Testing)
```bash
python3 red_team_real_targets_runner.py --campaign all --target-set defense_aerospace --dry-run
```

## Advanced Features

### Retry Configuration
```bash
# Custom retry settings
python3 red_team_real_targets_runner.py --campaign all --target-set defense_aerospace --max-retries 5 --max-total-attempts 20
```

### Specific Campaign Targeting
```bash
# Target specific industries
python3 red_team_real_targets_runner.py --campaign apt41_campaign_enhanced --target-set financial_institutions

# Government targeting
python3 red_team_real_targets_runner.py --campaign chinese_apt_lockheed_campaign --target-set government_agencies
```

## Campaign Execution Workflow

### Phase 1: Target Validation
- Validates domain reachability
- Checks IP connectivity
- Tests port availability
- Identifies successful targets

### Phase 2: Campaign Execution
- Executes campaign with retry logic
- Monitors for success indicators
- Retries on failure with exponential backoff
- Stops when success criteria met

### Phase 3: Success Detection
- Analyzes campaign output for success indicators
- Checks return codes and execution status
- Validates phase completion
- Generates comprehensive reports

### Phase 4: Reporting
- Creates detailed execution reports
- Tracks success rates and attempts
- Provides recommendations for improvement
- Logs all activities for audit

## Success Indicators

The system automatically detects successful campaign execution using:

### Output Analysis
- Keywords: `success`, `completed`, `finished`, `done`, `achieved`
- Phase indicators: `compromised`, `accessed`, `obtained`, `established`, `exfiltrated`
- Return code validation (exit code 0)

### Phase Completion
- Minimum 2 completed phases
- Successful reconnaissance results
- Established persistence mechanisms
- Data exfiltration confirmation

## Target Configuration

### Available Target Sets
- **defense_aerospace**: High-value defense and aerospace contractors
- **financial_institutions**: Major global banks and investment firms
- **government_agencies**: Critical US government organizations
- **technology_companies**: Leading tech companies with global data
- **energy_sector**: Major energy companies with critical infrastructure
- **healthcare_pharma**: Pharmaceutical and healthcare companies
- **critical_infrastructure**: Power grids and water systems
- **telecommunications**: Major telecom providers
- **research_institutions**: Leading research universities
- **manufacturing_industrial**: Industrial automation companies

### Custom Target Configuration
Edit `campaign_targets.json` to add custom targets:

```json
{
  "test_targets": {
    "your_custom_targets": {
      "domains": ["target1.com", "target2.com"],
      "ips": ["192.168.1.10", "10.0.1.20"],
      "ports": [80, 443, 22],
      "services": ["http", "https", "ssh"],
      "description": "Your custom target description"
    }
  }
}
```

## Campaign Types

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

## Execution Reports

### Report Structure
```json
{
  "report_type": "Red Team Campaign Execution Report",
  "generated": "2024-01-01T12:00:00",
  "total_campaigns_executed": 10,
  "successful_campaigns": 8,
  "failed_campaigns": 2,
  "success_rate": "80.0%",
  "executions": [...],
  "summary": {
    "total_attempts": 15,
    "average_attempts_per_campaign": 1.5,
    "first_successful_campaign": "defense_contractor_campaign",
    "execution_time": "75 minutes (estimated)"
  }
}
```

### Report Location
Reports are automatically saved as:
- `red_team_campaign_execution_YYYYMMDD_HHMMSS.json`
- `red_team_campaign_YYYYMMDD_HHMMSS.log`

## Safety Controls

### Dry Run Mode
Always test with dry-run mode first:
```bash
--dry-run
```

### Target Validation
Validate targets before execution:
```bash
python3 real_target_campaign_runner.py --validate-only --target-set defense_aerospace
```

### Execution Timeouts
- Individual campaigns: 5 minutes
- Validation operations: 5 seconds
- Retry delays: Configurable (default 30 seconds)

## Best Practices

### 1. Always Validate First
```bash
python3 real_target_campaign_runner.py --validate-only --target-set <target>
```

### 2. Use Dry Run Mode
```bash
python3 red_team_real_targets_runner.py --campaign <campaign> --target-set <target> --dry-run
```

### 3. Configure Appropriate Retry Settings
```bash
--max-retries 5 --max-total-attempts 20
```

### 4. Monitor Execution Logs
- Check `red_team_campaign_*.log` files
- Monitor success indicators
- Review execution reports

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
python3 -c "import logging; logging.basicConfig(level=logging.DEBUG)" red_team_real_targets_runner.py [options]
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

## Performance Optimization

### Resource Management
- Configure appropriate retry delays
- Set reasonable maximum attempts
- Monitor system resources during execution
- Use dry-run mode for testing configurations

### Network Considerations
- Consider network bandwidth limitations
- Be aware of target system load
- Implement appropriate delays between campaigns
- Monitor for network congestion

## Integration with Existing Systems

### API Integration
```python
from red_team_real_targets_runner import RedTeamCampaignExecutor

executor = RedTeamCampaignExecutor()
results = executor.execute_all_campaigns_until_success(
    target_set='defense_aerospace',
    max_retries_per_campaign=3,
    max_total_attempts=10
)
```

### Custom Success Criteria
Extend the success detection logic:
```python
class CustomRedTeamExecutor(RedTeamCampaignExecutor):
    def _is_campaign_successful(self, result: Dict) -> bool:
        # Add custom success criteria
        return super()._is_campaign_successful(result) and self._check_custom_criteria(result)
```

---

For questions or issues, refer to the campaign execution logs and validation reports generated by the system.