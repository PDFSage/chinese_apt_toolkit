#!/usr/bin/env python3
"""
Demonstration script for running APT campaigns against real targets
This script shows how to safely execute campaigns in a controlled environment
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path

def print_banner():
    """Print banner for demo"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║           APT Campaign Real Target Execution Demo            ║
    ║                  Controlled Test Environment                 ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def demonstrate_target_validation():
    """Demonstrate target validation"""
    print("\n[1] TARGET VALIDATION DEMONSTRATION")
    print("=" * 60)
    
    from real_target_campaign_runner import TargetValidator
    
    validator = TargetValidator()
    
    # Test targets (using example domains that won't resolve)
    test_targets = {
        'domains': [
            'test.defense.example.com',
            'test.contractor.example.com'
        ],
        'ips': [
            '10.0.1.10',
            '127.0.0.1'  # localhost for testing
        ]
    }
    
    print("\nValidating test domains:")
    for domain in test_targets['domains']:
        result = validator.validate_domain(domain)
        status = "✓ Reachable" if result else "✗ Unreachable"
        print(f"  {domain}: {status}")
    
    print("\nValidating test IPs:")
    for ip in test_targets['ips']:
        if ip == '127.0.0.1':
            # Skip actual ping for localhost in demo
            print(f"  {ip}: ✓ Localhost (always reachable)")
        else:
            print(f"  {ip}: ✗ Private network (unreachable in demo)")
    
    print("\nValidation Results Summary:")
    print(json.dumps(validator.validation_results, indent=2))

def demonstrate_campaign_listing():
    """Show available campaigns"""
    print("\n[2] AVAILABLE CAMPAIGNS")
    print("=" * 60)
    
    from real_target_campaign_runner import CampaignExecutor
    
    executor = CampaignExecutor()
    campaigns = executor.list_available_campaigns()
    
    print(f"\nFound {len(campaigns)} available campaigns:")
    
    # Group campaigns by type
    campaign_types = {
        'infrastructure': [],
        'industry': [],
        'apt': [],
        'technology': [],
        'other': []
    }
    
    for campaign in campaigns:
        if 'infrastructure' in campaign or 'system' in campaign or 'plant' in campaign:
            campaign_types['infrastructure'].append(campaign)
        elif 'company' in campaign or 'firm' in campaign or 'institution' in campaign:
            campaign_types['industry'].append(campaign)
        elif 'apt' in campaign or 'chinese' in campaign:
            campaign_types['apt'].append(campaign)
        elif 'cloud' in campaign or 'iot' in campaign or 'ai' in campaign:
            campaign_types['technology'].append(campaign)
        else:
            campaign_types['other'].append(campaign)
    
    for category, items in campaign_types.items():
        if items:
            print(f"\n{category.upper()} CAMPAIGNS ({len(items)}):")
            for item in items[:5]:  # Show first 5 of each category
                print(f"  • {item}")
            if len(items) > 5:
                print(f"  ... and {len(items) - 5} more")

def demonstrate_dry_run_execution():
    """Demonstrate dry run campaign execution"""
    print("\n[3] DRY RUN CAMPAIGN EXECUTION")
    print("=" * 60)
    
    from real_target_campaign_runner import CampaignExecutor
    
    executor = CampaignExecutor()
    
    # Select a campaign to demonstrate
    campaign = 'defense_contractor_campaign'
    target_set = 'defense_contractor'
    
    print(f"\nExecuting {campaign} in DRY RUN mode")
    print(f"Target set: {target_set}")
    print("\nThis will validate targets but not execute actual payloads")
    
    result = executor.execute_campaign(campaign, target_set, dry_run=True)
    
    print("\nExecution Result:")
    print(f"  Campaign: {result.get('campaign')}")
    print(f"  Target Set: {result.get('target_set')}")
    print(f"  Status: {result.get('execution', {}).get('status')}")
    print(f"  Message: {result.get('execution', {}).get('message')}")
    
    if 'validation' in result:
        print("\n  Validation Summary:")
        for category, results in result['validation'].items():
            valid_count = sum(1 for v in results.values() if v)
            print(f"    {category}: {valid_count}/{len(results)} valid")

def demonstrate_chinese_apt_campaigns():
    """Demonstrate Chinese APT campaigns"""
    print("\n[4] CHINESE APT CAMPAIGN DEMONSTRATION")
    print("=" * 60)
    
    from campaigns.chinese_apt_real_targets import RealTargetChineseAPT
    
    runner = RealTargetChineseAPT()
    
    # Create test target set
    test_targets = {
        'domains': ['gov.example.com', 'defense.example.com'],
        'ips': ['10.0.0.1', '10.0.0.2'],
        'ports': [80, 443, 22],
        'services': ['http', 'https', 'ssh']
    }
    
    print("\nAvailable Chinese APT Groups:")
    apt_groups = ['APT41', 'APT1', 'APT10', 'APT12']
    
    for group in apt_groups:
        print(f"\n{group}:")
        if group == 'APT41':
            print("  • Focus: Gaming industry, supply chain attacks")
            print("  • TTPs: Polyglot payloads, multi-stage malware")
        elif group == 'APT1':
            print("  • Focus: Government, military, critical infrastructure")
            print("  • TTPs: Spear phishing, long-term persistence")
        elif group == 'APT10':
            print("  • Focus: Cloud providers, MSPs")
            print("  • TTPs: Cloud hopping, API key theft")
        elif group == 'APT12':
            print("  • Focus: Diplomatic targets, media, NGOs")
            print("  • TTPs: Watering hole attacks, journalist targeting")
    
    print("\n\nSimulating APT41 Gaming Campaign (Mock Execution):")
    print("-" * 40)
    
    # Mock execution results
    mock_result = {
        'campaign': 'APT41 Gaming Industry',
        'timestamp': datetime.now().isoformat(),
        'targets': test_targets,
        'phases': {
            'reconnaissance': [
                {'target': 'gov.example.com', 'status': 'scanned', 
                 'findings': 'Gaming platform identified'}
            ],
            'supply_chain': {
                'game_update_servers': 'compromised',
                'malicious_updates': 'staged',
                'backdoors_planted': 2
            },
            'data_harvest': {
                'accounts_compromised': 'simulated_1000000+',
                'payment_data': 'collected',
                'personal_info': 'exfiltrated'
            }
        }
    }
    
    print(json.dumps(mock_result, indent=2))

def demonstrate_comprehensive_reporting():
    """Demonstrate comprehensive reporting capabilities"""
    print("\n[5] COMPREHENSIVE REPORTING")
    print("=" * 60)
    
    print("\nReport Types Available:")
    print("  • Campaign Execution Reports")
    print("  • Target Validation Reports")
    print("  • Chinese APT Analysis Reports")
    print("  • Comparative Campaign Analysis")
    print("  • Impact Assessment Reports")
    
    # Create sample report structure
    sample_report = {
        'report_id': f"RPT-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        'generated': datetime.now().isoformat(),
        'executive_summary': {
            'campaigns_executed': 5,
            'targets_compromised': 12,
            'data_exfiltrated': 'Simulated 10TB+',
            'critical_findings': [
                'Supply chain vulnerabilities identified',
                'Cloud infrastructure misconfiguration',
                'Weak network segmentation'
            ]
        },
        'recommendations': [
            'Implement zero-trust architecture',
            'Enhanced monitoring for APT indicators',
            'Supply chain security audit',
            'Cloud security posture review'
        ]
    }
    
    print("\nSample Report Structure:")
    print(json.dumps(sample_report, indent=2))
    
    print("\nReport files would be saved to:")
    print(f"  • campaign_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    print(f"  • campaign_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

def main():
    """Main demonstration function"""
    print_banner()
    
    print("\nThis demonstration will show the capabilities of the APT Campaign")
    print("Real Target Execution system in a safe, controlled manner.")
    print("\nNOTE: All executions are simulated or use non-existent test targets")
    
    demonstrations = [
        ("Target Validation", demonstrate_target_validation),
        ("Campaign Listing", demonstrate_campaign_listing),
        ("Dry Run Execution", demonstrate_dry_run_execution),
        ("Chinese APT Campaigns", demonstrate_chinese_apt_campaigns),
        ("Comprehensive Reporting", demonstrate_comprehensive_reporting)
    ]
    
    for i, (name, func) in enumerate(demonstrations, 1):
        input(f"\nPress Enter to continue to demonstration {i}: {name}...")
        try:
            func()
        except Exception as e:
            print(f"\nError in {name}: {str(e)}")
            print("(This is expected if certain modules are not available)")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    
    print("\nTo run real campaigns, use:")
    print("  python3 real_target_campaign_runner.py --campaign <campaign_name> --target-set <target>")
    print("\nFor Chinese APT campaigns:")
    print("  python3 campaigns/chinese_apt_real_targets.py --campaign all --target-set <target>")
    print("\nAlways use --dry-run flag first to validate before actual execution!")

if __name__ == '__main__':
    main()