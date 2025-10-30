#!/usr/bin/env python3
"""
Quick demonstration of real target campaign execution
"""

import json
import sys
from datetime import datetime

def demo_target_validation():
    """Demonstrate target validation"""
    print("\n[1] TARGET VALIDATION")
    print("=" * 50)
    
    from real_target_campaign_runner import TargetValidator
    
    validator = TargetValidator()
    
    # Test with localhost (should be reachable)
    print("\nValidating localhost:")
    result = validator.validate_domain('localhost')
    print(f"  localhost: {'✓ Reachable' if result else '✗ Unreachable'}")
    
    # Test with non-existent domain
    result = validator.validate_domain('nonexistent-test-domain-12345.example.com')
    print(f"  nonexistent-test-domain-12345.example.com: {'✓ Reachable' if result else '✗ Unreachable'}")
    
    print("\nValidation complete!")

def demo_campaign_listing():
    """Show available campaigns"""
    print("\n[2] AVAILABLE CAMPAIGNS")
    print("=" * 50)
    
    from real_target_campaign_runner import CampaignExecutor
    
    executor = CampaignExecutor()
    campaigns = executor.list_available_campaigns()
    
    print(f"\nFound {len(campaigns)} campaigns:")
    
    # Show some examples
    sample_campaigns = [
        c for c in campaigns 
        if any(keyword in c for keyword in ['defense', 'financial', 'government', 'apt', 'chinese'])
    ][:10]
    
    for campaign in sample_campaigns:
        print(f"  • {campaign}")
    
    if len(campaigns) > 10:
        print(f"  ... and {len(campaigns) - 10} more")

def demo_dry_run():
    """Demonstrate dry run execution"""
    print("\n[3] DRY RUN EXECUTION")
    print("=" * 50)
    
    from real_target_campaign_runner import CampaignExecutor
    
    executor = CampaignExecutor()
    
    print("\nExecuting defense_contractor_campaign in DRY RUN mode...")
    
    result = executor.execute_campaign(
        'defense_contractor_campaign',
        'defense_contractor',
        dry_run=True
    )
    
    print(f"\nResult: {result.get('execution', {}).get('status')}")
    print(f"Message: {result.get('execution', {}).get('message')}")
    
    if 'validation' in result:
        print("\nValidation Summary:")
        for category, results in result['validation'].items():
            valid_count = sum(1 for v in results.values() if v)
            print(f"  {category}: {valid_count}/{len(results)} valid")

def demo_chinese_apt():
    """Demonstrate Chinese APT campaigns"""
    print("\n[4] CHINESE APT CAMPAIGNS")
    print("=" * 50)
    
    print("\nAvailable APT Groups:")
    print("  • APT41 (Winnti) - Gaming industry, supply chain")
    print("  • APT1 (Comment Crew) - Government, military")
    print("  • APT10 (Cloud Hopper) - Cloud providers, MSPs")
    print("  • APT12 (Numbered Panda) - Diplomatic, media")
    
    print("\nSample Campaign Output (Simulated):")
    sample_result = {
        'campaign': 'APT41 Gaming Industry',
        'timestamp': datetime.now().isoformat(),
        'phases': {
            'reconnaissance': 'Complete',
            'supply_chain': 'Compromised',
            'data_harvest': '1M+ accounts'
        }
    }
    print(json.dumps(sample_result, indent=2))

def main():
    """Main demonstration"""
    print("\n" + "="*60)
    print("APT CAMPAIGN REAL TARGET EXECUTION DEMONSTRATION")
    print("="*60)
    
    print("\nThis demo shows the capabilities of the campaign execution system.")
    print("All operations are simulated or use safe test targets.\n")
    
    demonstrations = [
        ("Target Validation", demo_target_validation),
        ("Campaign Listing", demo_campaign_listing),
        ("Dry Run Execution", demo_dry_run),
        ("Chinese APT Campaigns", demo_chinese_apt)
    ]
    
    for name, func in demonstrations:
        print(f"\n{name}:")
        print("-" * len(name))
        try:
            func()
        except Exception as e:
            print(f"  Error: {str(e)}")
            print("  (This is expected for some modules in demo mode)")
    
    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("="*60)
    
    print("\nUsage Commands:")
    print("  python3 real_target_campaign_runner.py --list-campaigns")
    print("  python3 real_target_campaign_runner.py --campaign defense_contractor_campaign --target-set defense_contractor --dry-run")
    print("  python3 campaigns/chinese_apt_real_targets.py --campaign apt41 --target-set defense_contractor")

if __name__ == '__main__':
    main()