#!/usr/bin/env python3
"""
Advanced APT Analysis Example

This example demonstrates the enhanced APT toolkit capabilities with sophisticated
real-world tradecraft used by major APT groups against US targets.
"""

import json
from apt_toolkit import (
    APTCampaignSimulator,
    CampaignConfig,
    AdvancedSocialEngineering,
    PolyglotPayloadEngine,
    AdvancedPersistenceFramework,
    ADCSExploitationSuite,
    AdvancedKerberosAttacks,
    AdvancedEDREvasion,
    AdvancedProcessInjection,
    ExploitDBIndex,
    ExploitDBNotAvailableError,
    analyze_advanced_social_engineering,
    analyze_advanced_persistence,
    analyze_advanced_privilege_escalation,
    analyze_advanced_edr_evasion
)


def demonstrate_advanced_social_engineering():
    """Demonstrate AI-enhanced social engineering techniques."""
    print("\n" + "="*60)
    print("ADVANCED SOCIAL ENGINEERING ANALYSIS")
    print("="*60)
    
    se = AdvancedSocialEngineering()
    
    # Build comprehensive target dossier
    target_dossier = se.build_target_dossier("security.admin@dod.mil")
    
    # Create context-aware lure
    lure = se.create_context_aware_lure(target_dossier)
    
    print("\n[+] Target Dossier Analysis:")
    print(f"   - Professional Role: {target_dossier['professional']['job_title']}")
    print(f"   - Company: {target_dossier['professional']['company']}")
    print(f"   - Technical Skills: {', '.join(target_dossier['technical']['programming_languages'])}")
    print(f"   - Optimal Engagement: {target_dossier['engagement_windows']['optimal_engagement']}")
    
    print("\n[+] Generated Lure:")
    print(f"   - Subject: {lure['subject']}")
    print(f"   - Sender: {lure['sender']}")
    print(f"   - Attachment: {lure['attachment']}")
    print(f"   - Timing: {lure['timing']}")


def demonstrate_advanced_persistence():
    """Demonstrate sophisticated persistence mechanisms."""
    print("\n" + "="*60)
    print("ADVANCED PERSISTENCE ANALYSIS")
    print("="*60)
    
    persistence_analysis = analyze_advanced_persistence()
    
    print("\n[+] Multi-Layer Persistence Framework:")
    layers = persistence_analysis['multi_layer_persistence']['persistence_layers']
    for layer_name, layer_info in layers.items():
        if layer_name != 'stealth':
            print(f"   - {layer_name.title()}: {layer_info['technique']}")
            print(f"     Stealth Level: {layer_info['stealth_level']}")
            print(f"     APT Reference: {layer_info['apt_reference']}")
    
    print("\n[+] Fileless Persistence Techniques:")
    fileless = persistence_analysis['fileless_techniques']['fileless_techniques']
    for technique, info in fileless.items():
        print(f"   - {technique}: {info['method']}")
        print(f"     Activation: {info['activation']}")


def demonstrate_adcs_exploitation():
    """Demonstrate ADCS exploitation techniques."""
    print("\n" + "="*60)
    print("ADCS EXPLOITATION ANALYSIS")
    print("="*60)
    
    adcs = ADCSExploitationSuite()
    scan_results = adcs.perform_adcs_escalation_scan("dod.mil")
    
    print(f"\n[+] ADCS Vulnerability Scan for {scan_results['domain']}:")
    print(f"   - Total Vulnerabilities: {scan_results['total_vulnerabilities']}")
    print(f"   - Risk Assessment: {scan_results['risk_assessment']['risk_level']}")
    
    if scan_results['adcs_escalation_paths']:
        print("\n[+] Found Escalation Paths:")
        for vuln_type, details in scan_results['adcs_escalation_paths']:
            print(f"   - {vuln_type}: {details}")
    
    # Show exploitation guidance for critical vulnerabilities
    if scan_results['risk_assessment']['risk_level'] == "Critical":
        print("\n[+] Critical Vulnerability Exploitation Guidance:")
        for vuln_type, guidance in scan_results['exploitation_guidance'].items():
            print(f"   - {vuln_type}: {guidance['technique']}")
            print(f"     Tools: {', '.join(guidance['tools'])}")


def demonstrate_kerberos_attacks():
    """Demonstrate advanced Kerberos attack techniques."""
    print("\n" + "="*60)
    print("KERBEROS ATTACK ANALYSIS")
    print("="*60)
    
    kerberos = AdvancedKerberosAttacks()
    attack_results = kerberos.perform_kerberos_attack_suite("dod.mil")
    
    print(f"\n[+] Kerberos Attack Suite for {attack_results['domain']}:")
    
    for attack_name, result in attack_results['kerberos_attack_results'].items():
        if result.get('success_rate') in ["High", "Medium"]:
            print(f"\n   - {attack_name.replace('_', ' ').title()}:")
            print(f"     Success Rate: {result['success_rate']}")
            print(f"     Detection Risk: {result['detection_risk']}")
            print(f"     APT Reference: {result['apt_reference']}")
    
    print(f"\n[+] Defense Evasion Measures:")
    evasion = attack_results['defense_evasion']['evasion_techniques']
    for technique in evasion[:3]:  # Show first 3 techniques
        print(f"   - {technique}")


def demonstrate_edr_evasion():
    """Demonstrate advanced EDR evasion techniques."""
    print("\n" + "="*60)
    print("ADVANCED EDR EVASION ANALYSIS")
    print("="*60)
    
    edr_analysis = analyze_advanced_edr_evasion()
    
    print("\n[+] EDR Evasion Techniques:")
    techniques = edr_analysis['edr_evasion_analysis']['techniques_applied']
    for technique in techniques:
        print(f"   - {technique.replace('_', ' ').title()}")
    
    print(f"\n[+] Detection Risk: {edr_analysis['edr_evasion_analysis']['detection_risk']}")
    
    print("\n[+] Real-World APT References:")
    for apt_group, description in edr_analysis['real_world_apt_references'].items():
        print(f"   - {apt_group.upper()}: {description}")


def demonstrate_polyglot_payloads():
    """Demonstrate advanced polyglot payload creation."""
    print("\n" + "="*60)
    print("POLYGLOT PAYLOAD ANALYSIS")
    print("="*60)
    
    engine = PolyglotPayloadEngine()
    polyglot = engine.create_advanced_polyglot({"office_software": True})
    
    print("\n[+] Polyglot Payload Configuration:")
    config = polyglot['polyglot_config']
    print(f"   - Primary Format: {config['primary_format']}")
    print(f"   - Embedded Formats: {', '.join(config['embedded_formats'])}")
    print(f"   - Exploit Chain: {', '.join(config['exploit_chain'])}")
    
    print("\n[+] Detection Evasion:")
    evasion = polyglot['detection_evasion']['techniques_applied']
    for technique in evasion[:3]:  # Show first 3 techniques
        print(f"   - {technique}")


def demonstrate_full_campaign():
    """Run the orchestrated campaign simulator and highlight key milestones."""
    print("\n" + "="*60)
    print("FULL CAMPAIGN SIMULATION")
    print("="*60)

    simulator = APTCampaignSimulator(seed=42)
    report = simulator.simulate(CampaignConfig(seed=42))

    print("\n[+] Campaign Timeline Highlights:")
    for phase in report["campaign_timeline"]:
        primary = phase["techniques"][0]
        print(f"   - {phase['phase']}: {primary}")

    print("\n[+] Key Takeaways:")
    for takeaway in report["key_takeaways"][:4]:
        print(f"   - {takeaway}")

    print("\n[+] Sample PTH Outcome:")
    sample_attempt = report["lateral_movement"]["pass_the_hash_attempts"][0]
    print(
        f"   - Target {sample_attempt['target_ip']} success={sample_attempt['success']}"
    )


def demonstrate_exploit_intelligence():
    """Showcase offline ExploitDB enrichment for a well-known product."""
    print("\n" + "="*60)
    print("EXPLOITDB INTELLIGENCE")
    print("="*60)

    try:
        index = ExploitDBIndex()
    except ExploitDBNotAvailableError as exc:  # pragma: no cover - depends on local snapshot
        print(f"[!] {exc}")
        return

    report = index.analyze_exploit_surface("microsoft exchange", limit=5)

    print("\n[+] Module Alignment:")
    for module, count in report["module_alignment"].items():
        print(f"   - {module}: {count}")

    if report["recommended_detection_focus"]:
        print("\n[+] Detection Focus Recommendations:")
        for focus in report["recommended_detection_focus"][:3]:
            print(f"   - {focus}")

    if report["matched_exploits"]:
        sample = report["matched_exploits"][0]
        print("\n[+] Sample Exploit:")
        print(f"   - {sample.description} ({sample.type})")
        if sample.codes:
            print(f"     Codes: {', '.join(sample.codes)}")


def main():
    """Main demonstration function."""
    print("ADVANCED APT TOOLKIT DEMONSTRATION")
    print("Real-World Tradecraft Analysis for US Target Scenarios")
    print("="*60)
    
    # Demonstrate various advanced techniques
    demonstrate_advanced_social_engineering()
    demonstrate_advanced_persistence()
    demonstrate_adcs_exploitation()
    demonstrate_kerberos_attacks()
    demonstrate_edr_evasion()
    demonstrate_polyglot_payloads()
    demonstrate_full_campaign()
    demonstrate_exploit_intelligence()

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print("\nThis demonstration showcases sophisticated APT tradecraft including:")
    print("• AI-enhanced social engineering with behavioral analysis")
    print("• Multi-layer persistence mechanisms")
    print("• ADCS exploitation (ESC1-ESC8 vulnerabilities)")
    print("• Advanced Kerberos attacks (Golden/Diamond Tickets)")
    print("• EDR evasion through direct syscalls and hook bypass")
    print("• Polyglot payloads with multiple exploitation paths")
    print("\nThese techniques represent real-world methodologies used by APT groups")
    print("like APT29, APT41, and APT28 in campaigns against US targets.")


if __name__ == "__main__":
    main()
