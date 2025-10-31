import sys
import os
import json

# Add the parent directory to the path to import apt_toolkit modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from apt_toolkit.financial_targeting import analyze_financial_targets
from apt_toolkit.financial_theft_methods import generate_financial_theft_campaign


def main():
    print("=== Financial Institution Campaign Test ===")
    print("Expanded to cover all types of financial theft methods for US and global financial institutions\n")
    
    # Step 1: Analyze financial targets
    print("Step 1: Analyzing Financial Targets")
    print("-" * 40)
    
    target_analysis = analyze_financial_targets(seed=42)
    
    print(f"Target Types: {', '.join(target_analysis['target_types'])}")
    print(f"Total Targets: {target_analysis['threat_assessment']['total_targets']}")
    print(f"Total Estimated Value: {target_analysis['threat_assessment']['total_estimated_value']['formatted']}")
    print(f"Risk Assessment: {target_analysis['threat_assessment']['risk_assessment']}")
    print(f"Recommended Approach: {target_analysis['threat_assessment']['recommended_approach']}")
    print()
    
    # Step 2: Generate financial theft campaign
    print("Step 2: Generating Financial Theft Campaign")
    print("-" * 40)
    
    institution_types = target_analysis['target_types']
    theft_campaign = generate_financial_theft_campaign(
        institution_types=institution_types,
        seed=42
    )
    
    print(f"Campaign ID: {theft_campaign['campaign_id']}")
    print(f"Target Institutions: {', '.join(theft_campaign['target_institutions'])}")
    print(f"Primary Theft Method: {theft_campaign['primary_theft_method']}")
    print(f"Estimated Success Rate: {theft_campaign['estimated_success_rate']['adjusted_rate']} ({theft_campaign['estimated_success_rate']['confidence_level']})")
    print(f"Detection Risk: {theft_campaign['detection_risk']['overall_risk']}")
    print(f"Financial Impact: {theft_campaign['financial_impact']['formatted_impact']} ({theft_campaign['financial_impact']['impact_category']})")
    print(f"Execution Timeline: {theft_campaign['execution_timeline']['estimated_duration']}")
    print()
    
    # Step 3: Display selected theft methods
    print("Step 3: Selected Theft Methods")
    print("-" * 40)
    
    for i, method in enumerate(theft_campaign['selected_methods'], 1):
        risk = theft_campaign['detection_risk']['method_risks'][method]
        print(f"{i}. {method} (Risk: {risk})")
    print()
    
    # Step 4: Display execution phases
    print("Step 4: Campaign Execution Phases")
    print("-" * 40)
    
    for i, phase in enumerate(theft_campaign['execution_timeline']['phases'], 1):
        print(f"{i}. {phase}")
    print()
    
    # Step 5: Save campaign results
    print("Step 5: Saving Campaign Results")
    print("-" * 40)
    
    campaign_results = {
        "target_analysis": target_analysis,
        "theft_campaign": theft_campaign,
        "campaign_summary": {
            "total_estimated_value": target_analysis['threat_assessment']['total_estimated_value']['formatted'],
            "financial_impact": theft_campaign['financial_impact']['formatted_impact'],
            "success_rate": theft_campaign['estimated_success_rate']['adjusted_rate'],
            "detection_risk": theft_campaign['detection_risk']['overall_risk'],
            "timeline": theft_campaign['execution_timeline']['estimated_duration']
        }
    }
    
    results_file = os.path.join(os.path.dirname(__file__), "campaign_results.json")
    with open(results_file, 'w') as f:
        json.dump(campaign_results, f, indent=2)
    
    print(f"Campaign results saved to: {results_file}")
    print()
    
    # Final summary
    print("=== Campaign Summary ===")
    print("-" * 40)
    print(f"Total Financial Targets: {target_analysis['threat_assessment']['total_targets']}")
    print(f"Target Value Range: {target_analysis['threat_assessment']['total_estimated_value']['formatted']}")
    print(f"Estimated Financial Gain: {theft_campaign['financial_impact']['formatted_impact']}")
    print(f"Success Probability: {theft_campaign['estimated_success_rate']['adjusted_rate'] * 100}%")
    print(f"Detection Risk Level: {theft_campaign['detection_risk']['overall_risk']}")
    print(f"Campaign Duration: {theft_campaign['execution_timeline']['estimated_duration']}")
    print()
    print("Campaign test completed successfully!")


if __name__ == "__main__":
    main()