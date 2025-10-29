"""
APT10 (Stone Panda) Campaign Simulation

Simulates campaigns by APT10, known for:
- Managed Service Provider (MSP) targeting
- Cloud infrastructure compromise
- Supply chain attacks through service providers
- Large-scale data theft operations
"""

import random
from dataclasses import dataclass
from typing import Dict, List, Optional, Any

from apt_toolkit.campaign import CampaignConfig, APTCampaignSimulator
from apt_toolkit.initial_access_enhanced import AdvancedSocialEngineering
from apt_toolkit.lateral_movement import LateralMover
from apt_toolkit.exfiltration import DataExfiltrator


@dataclass
class APT10CampaignConfig(CampaignConfig):
    """Extended configuration for APT10-specific campaigns."""
    
    msp_targeting: bool = True
    cloud_infrastructure: bool = True
    supply_chain_through_msp: bool = True
    large_scale_data_theft: bool = True
    custom_malware_families: List[str] = None
    
    def __post_init__(self):
        if self.custom_malware_families is None:
            self.custom_malware_families = ["RedLeaves", "ChChes", "QUASARRAT", "PoisonIvy"]


class APT10CampaignSimulator:
    """Specialized simulator for APT10 (Stone Panda) campaigns."""
    
    def __init__(self, seed: Optional[int] = None):
        self._base_seed = seed
        self._base_simulator = APTCampaignSimulator(seed=seed)
        self._social_engineering = AdvancedSocialEngineering()
        self._lateral_mover = LateralMover()
        self._exfiltrator = DataExfiltrator()
    
    def simulate_msp_compromise_campaign(self, config: Optional[APT10CampaignConfig] = None) -> Dict[str, Any]:
        """Simulate APT10's MSP compromise campaigns."""
        
        config = config or APT10CampaignConfig()
        seed = config.seed if config.seed is not None else self._base_seed
        if seed is not None:
            random.seed(seed)
        
        # APT10-specific initial access
        initial_access = self._simulate_apt10_initial_access(config)
        
        # APT10-specific lateral movement
        lateral_movement = self._simulate_apt10_lateral_movement(config)
        
        # APT10-specific exfiltration
        exfiltration = self._simulate_apt10_exfiltration(config)
        
        # Standard campaign phases
        base_campaign = self._base_simulator.simulate(config)
        
        # Merge APT10-specific results
        result = {
            "apt_group": "APT10 (Stone Panda)",
            "campaign_type": "Managed Service Provider Compromise",
            "apt10_specific": {
                "initial_access": initial_access,
                "lateral_movement": lateral_movement,
                "exfiltration": exfiltration,
                "malware_families": config.custom_malware_families,
                "msp_compromise_details": self._get_msp_compromise_details(config)
            },
            **base_campaign
        }
        
        return result
    
    def _simulate_apt10_initial_access(self, config: APT10CampaignConfig) -> Dict[str, Any]:
        """Simulate APT10's unique initial access techniques."""
        
        # MSP-specific targeting
        if config.msp_targeting:
            target_emails = [
                f"support.engineer@{config.target_domain}",
                f"system.admin@{config.target_domain}",
                f"network.operations@{config.target_domain}",
                f"cloud.architect@{config.target_domain}"
            ]
        else:
            target_emails = [f"admin@{config.target_domain}"]
        
        # APT10's social engineering themes
        social_engineering_themes = [
            "MSP service maintenance notifications",
            "Cloud infrastructure security alerts",
            "Remote access tool updates",
            "Network monitoring system alerts",
            "Backup system maintenance"
        ]
        
        # Initial access vectors
        access_vectors = [
            "Compromised remote access credentials",
            "Vulnerable management interfaces",
            "Weak authentication on admin portals",
            "Supply chain compromise through software vendors"
        ]
        
        return {
            "target_emails": target_emails,
            "social_engineering_themes": social_engineering_themes,
            "access_vectors": access_vectors,
            "msp_specific_targeting": {
                "remote_management_tools": True,
                "cloud_management_consoles": True,
                "backup_systems": True,
                "monitoring_infrastructure": True
            }
        }
    
    def _simulate_apt10_lateral_movement(self, config: APT10CampaignConfig) -> Dict[str, Any]:
        """Simulate APT10's lateral movement through MSP infrastructure."""
        
        # Network discovery through MSP tools
        network_discovery = {
            "msp_tools_used": [
                "Remote monitoring and management (RMM) software",
                "Professional services automation (PSA) platforms",
                "Network documentation systems",
                "Client management databases"
            ],
            "discovered_assets": [
                "Client network segments",
                "Cloud infrastructure mappings",
                "Administrative access points",
                "Backup and recovery systems"
            ]
        }
        
        # Lateral movement techniques
        lateral_techniques = []
        
        # Through RMM tools
        rmm_lateral = {
            "technique": "RMM Tool Abuse",
            "description": "Use legitimate RMM tools for lateral movement",
            "capabilities": [
                "Remote command execution on client systems",
                "File transfer between systems",
                "Registry modification across network",
                "Service management on remote hosts"
            ]
        }
        lateral_techniques.append(rmm_lateral)
        
        # Through shared credentials
        credential_lateral = {
            "technique": "Shared Administrative Credentials",
            "description": "Leverage shared MSP admin credentials",
            "capabilities": [
                "Access multiple client environments",
                "Cross-client network movement",
                "Centralized authentication bypass",
                "Privilege escalation through trust relationships"
            ]
        }
        lateral_techniques.append(credential_lateral)
        
        # Through cloud management
        cloud_lateral = {
            "technique": "Cloud Management Console Access",
            "description": "Move between cloud tenants and subscriptions",
            "capabilities": [
                "Cross-tenant resource access",
                "Subscription-level privilege escalation",
                "Resource group traversal",
                "Management plane compromise"
            ]
        }
        lateral_techniques.append(cloud_lateral)
        
        return {
            "network_discovery": network_discovery,
            "lateral_techniques": lateral_techniques,
            "msp_compromise_scope": {
                "multiple_clients_compromised": True,
                "central_management_infrastructure": True,
                "shared_resources": True,
                "trust_relationships_exploited": True
            }
        }
    
    def _simulate_apt10_exfiltration(self, config: APT10CampaignConfig) -> Dict[str, Any]:
        """Simulate APT10's large-scale data exfiltration."""
        
        # Data discovery through MSP access
        data_discovery = {
            "discovery_methods": [
                "MSP client database queries",
                "Network storage enumeration",
                "Cloud storage bucket discovery",
                "Backup system analysis"
            ],
            "data_types_targeted": [
                "Intellectual property",
                "Customer databases",
                "Financial records",
                "Strategic business plans",
                "Research and development data"
            ]
        }
        
        # Exfiltration techniques
        exfiltration_techniques = []
        
        # Through legitimate channels
        legitimate_channel_exfil = {
            "technique": "Legitimate Data Transfer Channels",
            "description": "Use MSP's existing data transfer mechanisms",
            "methods": [
                "Backup system data extraction",
                "Cloud synchronization services",
                "Remote access file transfers",
                "Monitoring data exports"
            ]
        }
        exfiltration_techniques.append(legitimate_channel_exfil)
        
        # Through encrypted channels
        encrypted_exfil = {
            "technique": "Encrypted Exfiltration Channels",
            "description": "Use custom encrypted channels for data theft",
            "methods": [
                "DNS tunneling for small data",
                "HTTPS with custom encryption",
                "ICMP data encapsulation",
                "Steganography in legitimate traffic"
            ]
        }
        exfiltration_techniques.append(encrypted_exfil)
        
        # Large-scale operations
        large_scale_ops = {
            "scale_characteristics": [
                "Multi-terabyte data extraction",
                "Staged exfiltration over weeks/months",
                "Compression and encryption before transfer",
                "Off-peak hours for network evasion"
            ],
            "operational_security": [
                "Mimic normal backup operations",
                "Use existing administrative traffic patterns",
                "Avoid unusual network volume spikes",
                "Rotate exfiltration endpoints"
            ]
        }
        
        return {
            "data_discovery": data_discovery,
            "exfiltration_techniques": exfiltration_techniques,
            "large_scale_operations": large_scale_ops,
            "msp_advantage": {
                "centralized_data_access": True,
                "trusted_network_position": True,
                "legitimate_traffic_cover": True,
                "multiple_exfiltration_paths": True
            }
        }
    
    def _get_msp_compromise_details(self, config: APT10CampaignConfig) -> Dict[str, Any]:
        """Define APT10's MSP compromise methodology."""
        
        msp_compromise = {
            "target_selection": {
                "criteria": [
                    "MSPs with multiple high-value clients",
                    "Cloud service providers",
                    "Managed security service providers",
                    "IT outsourcing companies"
                ],
                "reconnaissance_focus": [
                    "Client portfolio analysis",
                    "Service offering assessment",
                    "Technical infrastructure mapping",
                    "Security posture evaluation"
                ]
            },
            "compromise_techniques": {
                "technical": [
                    "Vulnerability exploitation in management systems",
                    "Credential theft from administrative staff",
                    "Supply chain attacks on MSP software",
                    "Social engineering of technical personnel"
                ],
                "operational": [
                    "Business email compromise",
                    "Third-party vendor impersonation",
                    "Fake support requests",
                    "Phishing of administrative accounts"
                ]
            },
            "post_compromise_advantages": {
                "access_scope": [
                    "Multiple client organizations simultaneously",
                    "Centralized management infrastructure",
                    "Shared administrative resources",
                    "Trust relationships between MSP and clients"
                ],
                "detection_evasion": [
                    "Legitimate administrative tool usage",
                    "Expected network traffic patterns",
                    "Trusted source IP addresses",
                    "Normal business hour operations"
                ]
            }
        }
        
        return msp_compromise
    
    def simulate_cloud_infrastructure_attack(self, config: Optional[APT10CampaignConfig] = None) -> Dict[str, Any]:
        """Simulate APT10's cloud infrastructure targeting."""
        
        config = config or APT10CampaignConfig()
        
        cloud_attack = {
            "apt_group": "APT10 (Stone Panda)",
            "attack_type": "Cloud Infrastructure Compromise",
            "target_cloud_platforms": [
                "Microsoft Azure",
                "Amazon Web Services (AWS)",
                "Google Cloud Platform (GCP)",
                "Other cloud service providers"
            ],
            "attack_vectors": [
                "Compromised management console access",
                "Abused shared responsibility model",
                "Misconfigured cloud services",
                "Stolen cloud access keys"
            ],
            "exploitation_techniques": {
                "identity_and_access": [
                    "Privilege escalation in cloud IAM",
                    "Role assumption attacks",
                    "Credential theft from cloud instances",
                    "Federation trust exploitation"
                ],
                "network_security": [
                    "Security group and NACL bypass",
                    "VPC peering exploitation",
                    "Cross-tenant network access",
                    "Private endpoint compromise"
                ],
                "data_access": [
                    "Storage account compromise",
                    "Database instance access",
                    "Backup and snapshot theft",
                    "Encryption key extraction"
                ]
            },
            "operational_advantages": {
                "scale": "Access to multiple cloud tenants and subscriptions",
                "persistence": "Difficult to detect in multi-tenant environments",
                "mobility": "Easy movement between cloud regions and services",
                "recovery": "Multiple backup and redundancy options"
            }
        }
        
        return cloud_attack