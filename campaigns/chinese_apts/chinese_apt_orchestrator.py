"""
Chinese APT Campaign Orchestrator

Provides unified access to all Chinese APT campaign simulators:
- APT41 (Winnti) - Gaming industry and supply chain attacks
- APT1 (Comment Crew) - Government espionage and long-term campaigns
- APT10 (Stone Panda) - MSP and cloud infrastructure targeting
- APT12 (Numbered Panda) - Diplomatic and strategic intelligence
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any

from .apt41_campaign import APT41CampaignSimulator, APT41CampaignConfig
from .apt1_campaign import APT1CampaignSimulator, APT1CampaignConfig
from .apt10_campaign import APT10CampaignSimulator, APT10CampaignConfig
from .apt12_campaign import APT12CampaignSimulator, APT12CampaignConfig


@dataclass
class ChineseAPTCampaignConfig:
    """Configuration for running multiple Chinese APT campaigns."""
    
    target_domain: str = "secure.dod.mil"
    target_ip: str = "203.0.113.10"
    beacon_duration_hours: int = 48
    seed: Optional[int] = None
    
    # Campaign type selection
    run_apt41: bool = True
    run_apt1: bool = True
    run_apt10: bool = True
    run_apt12: bool = True
    
    # APT-specific configurations
    apt41_config: Optional[APT41CampaignConfig] = None
    apt1_config: Optional[APT1CampaignConfig] = None
    apt10_config: Optional[APT10CampaignConfig] = None
    apt12_config: Optional[APT12CampaignConfig] = None


class ChineseAPTCampaignOrchestrator:
    """Orchestrates multiple Chinese APT campaign simulations."""
    
    def __init__(self, seed: Optional[int] = None):
        self._seed = seed
        self._apt41_simulator = APT41CampaignSimulator(seed=seed)
        self._apt1_simulator = APT1CampaignSimulator(seed=seed)
        self._apt10_simulator = APT10CampaignSimulator(seed=seed)
        self._apt12_simulator = APT12CampaignSimulator(seed=seed)
    
    def run_comparative_analysis(self, config: Optional[ChineseAPTCampaignConfig] = None) -> Dict[str, Any]:
        """Run all configured Chinese APT campaigns and provide comparative analysis."""
        
        config = config or ChineseAPTCampaignConfig()
        
        campaigns = {}
        
        # Run APT41 campaign if enabled
        if config.run_apt41:
            apt41_config = config.apt41_config or APT41CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            campaigns["apt41"] = self._apt41_simulator.simulate_gaming_industry_campaign(apt41_config)
        
        # Run APT1 campaign if enabled
        if config.run_apt1:
            apt1_config = config.apt1_config or APT1CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            campaigns["apt1"] = self._apt1_simulator.simulate_government_espionage_campaign(apt1_config)
        
        # Run APT10 campaign if enabled
        if config.run_apt10:
            apt10_config = config.apt10_config or APT10CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            campaigns["apt10"] = self._apt10_simulator.simulate_msp_compromise_campaign(apt10_config)
        
        # Run APT12 campaign if enabled
        if config.run_apt12:
            apt12_config = config.apt12_config or APT12CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            campaigns["apt12"] = self._apt12_simulator.simulate_diplomatic_espionage_campaign(apt12_config)
        
        # Generate comparative analysis
        comparative_analysis = self._generate_comparative_analysis(campaigns)
        
        return {
            "campaign_config": config.__dict__,
            "individual_campaigns": campaigns,
            "comparative_analysis": comparative_analysis,
            "chinese_apt_overview": self._get_chinese_apt_overview()
        }
    
    def _generate_comparative_analysis(self, campaigns: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comparative analysis between different Chinese APT campaigns."""
        
        analysis = {
            "targeting_focus": {},
            "tactical_approaches": {},
            "malware_characteristics": {},
            "operational_patterns": {}
        }
        
        for apt_group, campaign in campaigns.items():
            # Targeting focus analysis
            if "apt41_specific" in campaign:
                analysis["targeting_focus"][apt_group] = "Gaming industry and supply chain"
            elif "apt1_specific" in campaign:
                analysis["targeting_focus"][apt_group] = "Government and defense espionage"
            elif "apt10_specific" in campaign:
                analysis["targeting_focus"][apt_group] = "Managed Service Providers and cloud"
            elif "apt12_specific" in campaign:
                analysis["targeting_focus"][apt_group] = "Diplomatic and strategic intelligence"
            
            # Tactical approaches
            initial_access = campaign.get("initial_access", {})
            if isinstance(initial_access, dict):
                analysis["tactical_approaches"][apt_group] = {
                    "social_engineering": initial_access.get("social_engineering_themes", []),
                    "payload_types": initial_access.get("payload_types", []),
                    "attack_vectors": initial_access.get("attack_vectors", [])
                }
            
            # Malware characteristics
            apt_specific = campaign.get(f"{apt_group}_specific", {})
            if isinstance(apt_specific, dict):
                analysis["malware_characteristics"][apt_group] = {
                    "families": apt_specific.get("malware_families", []),
                    "persistence_layers": len(apt_specific.get("persistence", {}).get("persistence_layers", [])) if "persistence" in apt_specific else 0
                }
            
            # Operational patterns
            command_control = campaign.get("command_control", {})
            if isinstance(command_control, dict):
                analysis["operational_patterns"][apt_group] = {
                    "c2_sophistication": "High" if "c2_infrastructure" in command_control else "Medium",
                    "beacon_patterns": command_control.get("beacon_patterns", {})
                }
        
        return analysis
    
    def _get_chinese_apt_overview(self) -> Dict[str, Any]:
        """Provide overview of Chinese APT groups and their characteristics."""
        
        return {
            "chinese_apt_landscape": {
                "apt41_winnti": {
                    "primary_focus": "Economic espionage, gaming industry, supply chain attacks",
                    "notable_campaigns": ["Operation Night Dragon", "ShadowPad campaign"],
                    "signature_techniques": ["Polyglot payloads", "Supply chain compromise", "Multi-format malware"],
                    "malware_families": ["PlugX", "PoisonIvy", "Gh0stRAT"]
                },
                "apt1_comment_crew": {
                    "primary_focus": "Long-term government and defense espionage",
                    "notable_campaigns": ["Operation Aurora", "Byzantine Hades"],
                    "signature_techniques": ["Strategic web compromises", "Custom malware development", "Long-term persistence"],
                    "malware_families": ["Gh0stRAT", "PoisonIvy", "HydraQ", "BUBBLEWRAP"]
                },
                "apt10_stone_panda": {
                    "primary_focus": "Managed Service Provider targeting, cloud infrastructure",
                    "notable_campaigns": ["Operation Cloud Hopper", "MSP supply chain attacks"],
                    "signature_techniques": ["MSP credential theft", "Cloud management console abuse", "Large-scale data exfiltration"],
                    "malware_families": ["RedLeaves", "ChChes", "QUASARRAT", "PoisonIvy"]
                },
                "apt12_numbered_panda": {
                    "primary_focus": "Diplomatic and strategic intelligence collection",
                    "notable_campaigns": ["Ixeshe campaigns", "Strategic intelligence operations"],
                    "signature_techniques": ["Watering hole attacks", "Multi-layered persistence", "Advanced defense evasion"],
                    "malware_families": ["Ixeshe", "A2D2", "SHOTPUT", "BANGAT"]
                }
            },
            "common_characteristics": {
                "operational_tempo": "Typically low-and-slow for long-term access",
                "target_selection": "Strategic economic and political intelligence",
                "technical_sophistication": "High, with custom tool development",
                "attribution_resistance": "Strong focus on operational security"
            },
            "defensive_considerations": {
                "detection_challenges": [
                    "Use of legitimate administrative tools",
                    "Mimicry of normal business operations",
                    "Low network traffic volumes",
                    "Geographic diversity of infrastructure"
                ],
                "mitigation_strategies": [
                    "Enhanced monitoring of administrative access",
                    "Supply chain security assessments",
                    "Cloud security posture management",
                    "Behavioral analytics for anomalous activity"
                ]
            }
        }
    
    def simulate_specific_campaign_type(self, campaign_type: str, config: Optional[ChineseAPTCampaignConfig] = None) -> Dict[str, Any]:
        """Simulate a specific type of Chinese APT campaign."""
        
        config = config or ChineseAPTCampaignConfig()
        
        campaign_type = campaign_type.lower()
        
        if campaign_type == "apt41_gaming":
            apt41_config = config.apt41_config or APT41CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt41_simulator.simulate_gaming_industry_campaign(apt41_config)
        
        elif campaign_type == "apt41_supply_chain":
            apt41_config = config.apt41_config or APT41CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt41_simulator.simulate_supply_chain_attack()
        
        elif campaign_type == "apt1_government":
            apt1_config = config.apt1_config or APT1CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt1_simulator.simulate_government_espionage_campaign(apt1_config)
        
        elif campaign_type == "apt1_long_term":
            apt1_config = config.apt1_config or APT1CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt1_simulator.simulate_long_term_campaign(duration_days=365, config=apt1_config)
        
        elif campaign_type == "apt10_msp":
            apt10_config = config.apt10_config or APT10CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt10_simulator.simulate_msp_compromise_campaign(apt10_config)
        
        elif campaign_type == "apt10_cloud":
            apt10_config = config.apt10_config or APT10CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt10_simulator.simulate_cloud_infrastructure_attack()
        
        elif campaign_type == "apt12_diplomatic":
            apt12_config = config.apt12_config or APT12CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt12_simulator.simulate_diplomatic_espionage_campaign(apt12_config)
        
        elif campaign_type == "apt12_strategic":
            apt12_config = config.apt12_config or APT12CampaignConfig(
                target_domain=config.target_domain,
                target_ip=config.target_ip,
                beacon_duration_hours=config.beacon_duration_hours,
                seed=config.seed
            )
            return self._apt12_simulator.simulate_strategic_intelligence_operation(duration_months=24, config=apt12_config)
        
        else:
            raise ValueError(f"Unknown campaign type: {campaign_type}")
    
    def get_available_campaign_types(self) -> Dict[str, List[str]]:
        """Return available Chinese APT campaign types."""
        
        return {
            "apt41_winnti": [
                "apt41_gaming",
                "apt41_supply_chain"
            ],
            "apt1_comment_crew": [
                "apt1_government", 
                "apt1_long_term"
            ],
            "apt10_stone_panda": [
                "apt10_msp",
                "apt10_cloud"
            ],
            "apt12_numbered_panda": [
                "apt12_diplomatic",
                "apt12_strategic"
            ]
        }