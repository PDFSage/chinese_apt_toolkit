"""Campaign orchestration utilities for the APT Toolkit.

This module connects the standalone primitives (initial access, persistence,
privilege escalation, defense evasion, lateral movement, command and control,
and exfiltration) into a coherent end-to-end campaign simulator. The output is
conceptual and intended for defensive research, purple teaming exercises, and
training scenarios only.
"""

from __future__ import annotations

import hashlib
import ipaddress
import random
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .command_control import C2Communicator
from .defense_evasion import DefenseEvader
from .defense_evasion_enhanced import (
    AdvancedEDREvasion,
    AdvancedLOTLTechniques,
    AdvancedProcessInjection,
)
from .exfiltration import DataExfiltrator
from .initial_access_enhanced import (
    AdvancedSocialEngineering,
    PolyglotPayloadEngine,
    SupplyChainCompromise,
)
from .lateral_movement import LateralMover
from .persistence_enhanced import (
    AdvancedPersistenceFramework,
    CounterForensics,
    FilelessPersistence,
)
from .privilege_escalation import PrivilegeEscalator
from .privilege_escalation_enhanced import (
    ADCSExploitationSuite,
    AdvancedKerberosAttacks,
)
from .exploit_intel import enrich_with_exploit_intel


@dataclass
class CampaignConfig:
    """Configuration options for a simulated APT campaign."""

    target_domain: str = "secure.dod.mil"
    target_ip: str = "203.0.113.10"
    beacon_duration_hours: int = 48
    include_supply_chain: bool = True
    include_counter_forensics: bool = True
    seed: Optional[int] = None


class APTCampaignSimulator:
    """Orchestrate the toolkit's primitives into a full campaign narrative."""

    def __init__(self, seed: Optional[int] = None):
        self._base_seed = seed
        self._social_engineering = AdvancedSocialEngineering()
        self._polyglot_engine = PolyglotPayloadEngine()
        self._supply_chain = SupplyChainCompromise()
        self._persistence_framework = AdvancedPersistenceFramework()
        self._fileless = FilelessPersistence()
        self._counter_forensics = CounterForensics()
        self._privilege_escalator = PrivilegeEscalator()
        self._adcs_suite = ADCSExploitationSuite()
        self._kerberos_suite = AdvancedKerberosAttacks()
        self._defense_evader = DefenseEvader()
        self._advanced_edr = AdvancedEDREvasion()
        self._advanced_process_injection = AdvancedProcessInjection()
        self._advanced_lotl = AdvancedLOTLTechniques()
        self._c2 = C2Communicator()
        self._exfiltrator = DataExfiltrator()

    def simulate(self, config: Optional[CampaignConfig] = None) -> Dict[str, Any]:
        """Run the end-to-end simulation and return a structured report."""

        config = config or CampaignConfig()
        seed = config.seed if config.seed is not None else self._base_seed
        if seed is not None:
            random.seed(seed)

        initial_access = self._simulate_initial_access(config)
        persistence = self._simulate_persistence(config)
        privilege_escalation = self._simulate_privilege_escalation(config)
        defense_evasion = self._simulate_defense_evasion()
        lateral_movement = self._simulate_lateral_movement(
            privilege_escalation, config
        )
        command_control = self._simulate_command_control(config)
        exfiltration = self._simulate_exfiltration()

        timeline = self._build_timeline(
            initial_access,
            persistence,
            privilege_escalation,
            defense_evasion,
            lateral_movement,
            command_control,
            exfiltration,
        )

        return {
            "config": config.__dict__,
            "initial_access": initial_access,
            "persistence": persistence,
            "privilege_escalation": privilege_escalation,
            "defense_evasion": defense_evasion,
            "lateral_movement": lateral_movement,
            "command_control": command_control,
            "exfiltration": exfiltration,
            "campaign_timeline": timeline,
            "key_takeaways": self._summarize_takeaways(
                initial_access,
                persistence,
                privilege_escalation,
                lateral_movement,
                exfiltration,
            ),
        }

    # ------------------------------------------------------------------
    # Phase simulators

    def _simulate_initial_access(self, config: CampaignConfig) -> Dict[str, Any]:
        target_email = f"security.team@{config.target_domain}"
        dossier = self._social_engineering.build_target_dossier(target_email)
        lure = self._social_engineering.create_context_aware_lure(dossier)
        payload = self._polyglot_engine.create_advanced_polyglot({"office_software": True})

        supply_chain_state: Optional[Dict[str, Any]] = None
        if config.include_supply_chain:
            supply_chain_state = self._supply_chain.malicious_update_check(
                config.target_ip,
                config.target_domain,
            )
            supply_chain_state["implant_outcome"] = self._supply_chain.execute_implant(
                supply_chain_state
            )

        result = {
            "target_email": target_email,
            "target_dossier": dossier,
            "lure": lure,
            "polyglot_payload": payload,
            "supply_chain": supply_chain_state,
        }
        lure_subject = lure.get("subject") if isinstance(lure, dict) else None
        payload_vector = payload.get("primary_vector") if isinstance(payload, dict) else None
        search_terms = [config.target_domain, lure_subject, payload_vector]
        search_terms = [term for term in search_terms if term]
        return enrich_with_exploit_intel(
            "initial-access",
            result,
            search_terms=search_terms,
            platform="windows",
            include_payloads=True,
        )

    def _simulate_persistence(self, config: CampaignConfig) -> Dict[str, Any]:
        multi_layer = self._persistence_framework.install_multi_layer_persistence(
            {"edr_present": True}
        )
        fileless = self._fileless.establish_fileless_persistence()
        counter_forensics = (
            self._counter_forensics.implement_counter_forensics()
            if config.include_counter_forensics
            else None
        )

        result = {
            "multi_layer": multi_layer,
            "fileless": fileless,
            "counter_forensics": counter_forensics,
        }
        return enrich_with_exploit_intel(
            "persistence",
            result,
            search_terms=["fileless persistence", "counter forensics"],
            platform="windows",
            include_payloads=True,
        )

    def _simulate_privilege_escalation(self, config: CampaignConfig) -> Dict[str, Any]:
        ad_enum = self._privilege_escalator.enumerate_ad_privileges()
        vuln_scan = self._privilege_escalator.check_vulnerabilities(
            f"dc1.{config.target_domain}"
        )
        adcs_scan = self._adcs_suite.perform_adcs_escalation_scan(config.target_domain)
        kerberos_suite = self._kerberos_suite.perform_kerberos_attack_suite(
            config.target_domain
        )

        result = {
            "active_directory": {
                "enumeration": ad_enum,
                "vulnerabilities": vuln_scan,
            },
            "adcs": adcs_scan,
            "kerberos": kerberos_suite,
        }
        return enrich_with_exploit_intel(
            "privilege-escalation",
            result,
            search_terms=[config.target_domain, "adcs", "kerberos"],
            platform="windows",
            include_payloads=True,
        )

    def _simulate_defense_evasion(self) -> Dict[str, Any]:
        lotl = self._defense_evader.generate_lotl_commands()
        lotl_detection = self._defense_evader.analyze_lotl_detection()
        edr_evasion = self._advanced_edr.execute_stealthy_payload(
            "reflective_loader",
            "advanced",
        )
        process_injection = self._advanced_process_injection.perform_stealthy_injection()
        advanced_lotl = self._advanced_lotl.generate_advanced_lotl_commands("beacon")

        result = {
            "lotl": lotl,
            "lotl_detection": lotl_detection,
            "advanced_edr_evasion": edr_evasion,
            "process_injection": process_injection,
            "advanced_lotl": advanced_lotl,
        }
        return enrich_with_exploit_intel(
            "defense-evasion",
            result,
            search_terms=["lotl", "edr evasion", "process injection"],
            platform="windows",
            include_payloads=True,
        )

    def _simulate_lateral_movement(
        self, privilege_escalation: Dict[str, Any], config: CampaignConfig
    ) -> Dict[str, Any]:
        kerberos_results = privilege_escalation["kerberos"]["kerberos_attack_results"]
        stolen_hashes = self._derive_stolen_hashes(kerberos_results)

        lateral = LateralMover(stolen_hashes)
        network_map = lateral.discover_network_segments()
        target_hosts = self._derive_target_hosts(config.target_ip, len(stolen_hashes))

        lateral_attempts = [
            lateral.pass_the_hash_lateral(host, creds["username"], creds["hash"])
            for host, creds in zip(target_hosts, stolen_hashes)
        ]
        implant_deployments = [
            lateral.deploy_implant(host, "beacon") for host in target_hosts
        ]

        result = {
            "stolen_hashes": stolen_hashes,
            "network_map": network_map,
            "pass_the_hash_attempts": lateral_attempts,
            "implant_deployments": implant_deployments,
        }
        return enrich_with_exploit_intel(
            "lateral-movement",
            result,
            search_terms=["pass-the-hash", config.target_domain],
            platform="windows",
            include_payloads=True,
        )

    def _simulate_command_control(self, config: CampaignConfig) -> Dict[str, Any]:
        beacon = self._c2.send_beacon({"stage": "maintenance"})
        lifecycle = self._c2.simulate_c2_lifecycle(config.beacon_duration_hours)
        channels = self._c2.analyze_c2_channels()

        result = {
            "sample_beacon": beacon,
            "lifecycle": lifecycle,
            "channel_analysis": channels,
        }
        return enrich_with_exploit_intel(
            "command-control",
            result,
            search_terms=["c2", "beacon"],
            platform=None,
            include_payloads=True,
        )

    def _simulate_exfiltration(self) -> Dict[str, Any]:
        discovery = self._exfiltrator.find_sensitive_data()
        strategy = self._exfiltrator.generate_exfiltration_strategy(discovery)
        sample_exfiltration = None
        if discovery["files_discovered"]:
            sample_exfiltration = self._exfiltrator.slow_exfiltrate(
                discovery["files_discovered"][0]
            )

        result = {
            "discovery": discovery,
            "strategy": strategy,
            "method_analysis": self._exfiltrator.analyze_exfiltration_methods(),
            "sample_exfiltration": sample_exfiltration,
        }
        return enrich_with_exploit_intel(
            "exfiltration",
            result,
            search_terms=["data exfiltration", "dns", "https"],
            platform="windows",
            include_payloads=True,
        )

    # ------------------------------------------------------------------
    # Helpers

    def _derive_stolen_hashes(self, kerberos_results: Dict[str, Any]) -> List[Dict[str, str]]:
        kerberoast = kerberos_results.get("kerberoasting", {})
        vulnerable_accounts = kerberoast.get("vulnerable_accounts", [])

        hashes: List[Dict[str, str]] = []
        for account in vulnerable_accounts:
            digest = hashlib.md5(account.encode("utf-8")).hexdigest()
            hashes.append({"username": account, "hash": digest})

        if not hashes:
            # Ensure lateral movement still runs even if no vulnerable accounts were found.
            digest = hashlib.md5(b"default_admin").hexdigest()
            hashes.append({"username": "default_admin", "hash": digest})

        return hashes

    def _derive_target_hosts(self, base_ip: str, count: int) -> List[str]:
        ip = ipaddress.IPv4Address(base_ip)
        return [str(ip + index + 1) for index in range(max(count, 1))]

    def _build_timeline(
        self,
        initial_access: Dict[str, Any],
        persistence: Dict[str, Any],
        privilege_escalation: Dict[str, Any],
        defense_evasion: Dict[str, Any],
        lateral_movement: Dict[str, Any],
        command_control: Dict[str, Any],
        exfiltration: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        dataset = []

        dataset.append(
            {
                "phase": "Initial Access",
                "techniques": [
                    "Context-aware spear phishing",
                    "Polyglot payload delivery",
                    "Supply chain pre-positioning"
                    if initial_access["supply_chain"]
                    else "Direct lure engagement",
                ],
                "detection_focus": "Email security, user awareness, supplier validation",
            }
        )

        dataset.append(
            {
                "phase": "Persistence",
                "techniques": [
                    persistence["multi_layer"]["persistence_layers"]["primary"]["technique"],
                    "Fileless PowerShell reflection",
                    "Counter-forensics"
                    if persistence["counter_forensics"]
                    else "Stealth maintenance",
                ],
                "detection_focus": "Autoruns auditing, WMI monitoring, memory analysis",
            }
        )

        dataset.append(
            {
                "phase": "Privilege Escalation",
                "techniques": [
                    "ADCS exploitation (ESC paths)",
                    "Kerberoasting",
                    "Vulnerability-driven escalation",
                ],
                "detection_focus": "Kerberos telemetry, certificate authority hardening",
            }
        )

        dataset.append(
            {
                "phase": "Defense Evasion",
                "techniques": [
                    "Direct syscall payload execution",
                    defense_evasion["process_injection"]["injection_technique"],
                    "Advanced LOTL command chaining",
                ],
                "detection_focus": "EDR hook integrity, LOTL command monitoring",
            }
        )

        dataset.append(
            {
                "phase": "Lateral Movement",
                "techniques": [
                    "Pass-the-Hash",
                    "Targeted implant deployment",
                ],
                "detection_focus": "Authentication anomaly detection, east-west traffic",
            }
        )

        dataset.append(
            {
                "phase": "Command & Control",
                "techniques": [
                    command_control["sample_beacon"]["technique"],
                    "Domain fronted beacon rotation",
                ],
                "detection_focus": "Beacon timing analysis, TLS inspection",
            }
        )

        dataset.append(
            {
                "phase": "Exfiltration",
                "techniques": [
                    exfiltration["strategy"]["primary_method"],
                    "Slow-and-low chunked transfers",
                ],
                "detection_focus": "DLP enforcement, outbound anomaly monitoring",
            }
        )

        return dataset

    def _summarize_takeaways(
        self,
        initial_access: Dict[str, Any],
        persistence: Dict[str, Any],
        privilege_escalation: Dict[str, Any],
        lateral_movement: Dict[str, Any],
        exfiltration: Dict[str, Any],
    ) -> List[str]:
        takeaways = [
            "Multi-layered tradecraft: social engineering, payload crafting, and supply-chain positioning work in concert.",
            "Persistence layering combines on-disk, fileless, and counter-forensic measures for resiliency.",
            "Privilege escalation highlights ADCS and Kerberos weaknesses that feed directly into credential theft.",
            "Stolen credentials are operationalized immediately for lateral movement and implant deployment.",
            "Exfiltration planning adapts to discovered data volumes and classification levels.",
        ]

        high_value_accounts = privilege_escalation["kerberos"]["kerberos_attack_results"].get(
            "kerberoasting", {}
        ).get("vulnerable_accounts", [])
        if high_value_accounts:
            takeaways.append(
                f"High-value service accounts at risk: {', '.join(high_value_accounts)}"
            )

        discovered_files = exfiltration["discovery"]["files_discovered"]
        if discovered_files:
            takeaways.append(
                f"Sensitive data staged for exfiltration: {', '.join(discovered_files[:2])}"
            )

        if initial_access["supply_chain"]:
            takeaways.append(
                "Supply-chain foothold provides backup ingress path outside core phishing campaign."
            )

        if persistence["counter_forensics"]:
            takeaways.append(
                "Counter-forensic measures significantly raise the bar for incident responders."
            )

        if lateral_movement["pass_the_hash_attempts"]:
            success_rate = sum(
                1 for attempt in lateral_movement["pass_the_hash_attempts"] if attempt["success"]
            )
            takeaways.append(
                f"Pass-the-Hash attempts succeeded on {success_rate} of {len(lateral_movement['pass_the_hash_attempts'])} targeted hosts."
            )

        return takeaways


def simulate_campaign(config: Optional[CampaignConfig] = None) -> Dict[str, Any]:
    """Convenience wrapper that instantiates the simulator with defaults."""

    simulator = APTCampaignSimulator()
    return simulator.simulate(config)


__all__ = ["CampaignConfig", "APTCampaignSimulator", "simulate_campaign"]
