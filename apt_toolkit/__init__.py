"""
APT Toolkit - Advanced Persistent Threat Offensive Toolkit

A comprehensive framework for red team operations, penetration testing, and advanced adversary simulation.
This toolkit provides real-world offensive security capabilities for authorized security testing.

⚠️ LEGAL AND ETHICAL NOTICE:
This toolkit is intended for authorized penetration testing, security research, and educational purposes only.
Unauthorized use is illegal and unethical. Always obtain proper permissions before use.
"""

__version__ = "3.1.0"
__author__ = "Security Research Team"

# Core modules
from .american_targets import analyze_american_targets
from .initial_access import SpearPhishingGenerator, SupplyChainCompromise
from .persistence import PersistenceManager
from .privilege_escalation import PrivilegeEscalator
from .defense_evasion import DefenseEvader
from .lateral_movement import LateralMover
from .command_control import C2Communicator
from .exfiltration import DataExfiltrator

# Enhanced modules with sophisticated tradecraft
from .campaign import APTCampaignSimulator, CampaignConfig, simulate_campaign
from .initial_access_enhanced import AdvancedSocialEngineering, PolyglotPayloadEngine, analyze_advanced_social_engineering, analyze_polyglot_payloads
from .persistence_enhanced import AdvancedPersistenceFramework, FilelessPersistence, CounterForensics, analyze_advanced_persistence
from .privilege_escalation_enhanced import ADCSExploitationSuite, AdvancedKerberosAttacks, analyze_advanced_privilege_escalation
from .defense_evasion_enhanced import AdvancedEDREvasion, AdvancedProcessInjection, AdvancedLOTLTechniques, analyze_advanced_edr_evasion, analyze_advanced_process_injection
from .exploit_intel import (
    ExploitDBIndex,
    ExploitDBNotAvailableError,
    ExploitEntry,
    enrich_with_exploit_intel,
    module_recommendations,
)
from .offensive_playbooks import generate_offensive_playbook

# Chinese APT Campaign modules
from .chinese_apt_campaign import (
    AdvancedTargetingEngine,
    CampaignOrchestrator,
    SystemExploitationEngine
)

__all__ = [
    # Core modules
    "SpearPhishingGenerator",
    "SupplyChainCompromise", 
    "PersistenceManager",
    "PrivilegeEscalator",
    "DefenseEvader",
    "LateralMover",
    "C2Communicator",
    "DataExfiltrator",
    
    # Enhanced modules
    "AdvancedSocialEngineering",
    "PolyglotPayloadEngine",
    "AdvancedPersistenceFramework", 
    "FilelessPersistence",
    "CounterForensics",
    "ADCSExploitationSuite",
    "AdvancedKerberosAttacks",
    "AdvancedEDREvasion",
    "AdvancedProcessInjection",
    "AdvancedLOTLTechniques",
    
    # Analysis functions
    "analyze_advanced_social_engineering",
    "analyze_polyglot_payloads",
    "analyze_advanced_persistence",
    "analyze_advanced_privilege_escalation",
    "analyze_advanced_edr_evasion",
    "analyze_advanced_process_injection",
    "analyze_american_targets",

    # Campaign orchestration
    "CampaignConfig",
    "APTCampaignSimulator",
    "simulate_campaign",

    # ExploitDB intelligence
    "ExploitDBIndex",
    "ExploitEntry",
    "ExploitDBNotAvailableError",
    "enrich_with_exploit_intel",
    "module_recommendations",
    "generate_offensive_playbook",

    # Chinese APT Campaign modules
    "AdvancedTargetingEngine",
    "CampaignOrchestrator", 
    "SystemExploitationEngine"
]

# Security controls and safety measures
__safety_controls__ = {
    "require_authorization": True,
    "safe_mode_default": False,
    "audit_logging": True,
    "environment_checks": True
}

# Import safety controls
from .security_controls import (
    SafetyController,
    require_authorization,
    safe_mode,
    audit_action,
    environment_check
)