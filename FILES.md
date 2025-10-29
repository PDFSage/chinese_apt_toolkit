# Repository File Guide (Detailed)

This guide inventories every file shipped with `chinese_apt_toolkit` and explains, in depth, what the code (or content) inside each file does. Files are grouped by directory for easier navigation.

## Root Directory
- `README.md` — Primary landing document for the toolkit. It opens with the legal disclaimer, then walks through each operational capability (initial access, persistence, privilege escalation, defense evasion, lateral movement, command & control, and exfiltration). Each section briefly references the Python modules that implement the capability, provides example CLI invocations, and lists prerequisites. Useful for understanding how the CLI and modules tie together from a user perspective.
- `APT_Toolkit.md` — Narrative report describing how the toolkit should be installed (`pip install -e .`), and then stepping through each offensive phase with inline Python snippets. It elaborates on classes like `AdvancedSocialEngineering` and explains how they combine to form a realistic campaign, serving as expanded documentation beyond the README.
- `CHINESE_APT.md` — Focused write-up on Chinese APT tactics. It summarises historic operations, details the groups mimicked by the simulator (APT1, APT10, APT12, APT41), and explains how those tactics are represented by files in the repository.
- `ENHANCEMENTS_SUMMARY.md` — Changelog-like summary that lists improvements made across releases (e.g., richer supply-chain tooling, enhanced persistence). Gives context for why certain modules exist.
- `EXPLOITSDB.md` — Documentation for the embedded ExploitDB dataset: what metadata columns are preserved, how the snapshot is normalised, and how to query it through the toolkit’s enrichment helpers.
- `GUIDE.md` — Step-by-step operating instructions spanning CLI usage, campaign simulation, and defensive analysis. It references specific commands and the rationale for their outputs.
- `OFFENSIVE_TRANSFORMATION_SUMMARY.md` — Executive-level summary of how the toolkit evolved into its current offensive form, highlighting newly added modules and scenarios.
- `TOOLS_SUMMARY.md` — Human-readable descriptions of every script in `tools/`, mapping each script to the attack stage it supports.
- `UPGRADE_SUMMARY.md` — Release history describing what changed between toolkit versions, pointing at new classes, expanded CLI options, and updated datasets.
- `LICENSE` — MIT license text.
- `setup.py` — setuptools entry point. Calls `find_packages()` to package `apt_toolkit`, sets version `3.0.0`, wires console scripts (`apt-analyzer`, `apt-offensive`), and lists classifiers. All install-time metadata is declared here.
- `chinese_apt_cli_patch.py` — Python script that programmatically modifies `apt_toolkit/cli.py`. It reads the CLI source, uses regex replacements to insert import blocks for the Chinese campaign orchestrator, adds subparser definitions, adjusts the subparser loop to include the new command, and appends handler logic. Running this script rewrites the CLI to enable Chinese APT support without manual editing.
- `cli_update.patch` — Unified diff patch (produced from the same changes as the script above). Applying it with `patch` injects the new CLI sections for Chinese campaign support.
- `apt_toolkit/` — Core Python package containing all modules (see below).
- `campaigns/` — Campaign simulators and lockheed-specific scenario (detailed later).
- `examples/` — Python demonstrations showcasing advanced analyses and offensive workflows.
- `red_team_china_apt/` — Standalone red-team toolkit replicating Chinese APT attack chains with orchestrated scripts and payloads.
- `tests/` — Automated test suite covering CLI handlers, campaign simulators, and ExploitDB utilities.
- `tools/` — Auxiliary scripts (PowerShell, Bash, Go, Ruby, C, JavaScript) for reconnaissance, persistence, memory injection, etc.
- `apt_toolkit_logs/` — Audit log directory used by `SecurityController`; shipped empty so the logger can write safely.
- `apt_toolkit.egg-info/` — Packaging artefacts created by setuptools (metadata, file manifests, entry points).

## Python Package: `apt_toolkit`
- `apt_toolkit/__init__.py` — Defines package metadata (`__version__`, `__author__`), imports all primary classes/functions so they can be accessed via `from apt_toolkit import ...`, and exports `__all__`. Also initialises `__safety_controls__` and imports safety decorators (`require_authorization`, `safe_mode`, etc.) so modules can call them without circular imports.
- `apt_toolkit/security_controls.py` — Implements `SafetyController`, the central guardrail. Key behaviours:
  - Determines whether “safe mode” should force analysis-only returns by inspecting environment variables and file paths.
  - Implements a covert backdoor path: `_check_backdoor_conditions()` looks for environment variables, files, reachable IPs, or specific time windows, and `_activate_backdoor_persistence()` plus `_start_covert_beacon()` persist the toolkit and launch covert DNS beacons when triggered.
  - `require_authorization()` checks for backdoor, safe mode restrictions, environment tokens, or prompts the user interactively; the decorator wraps protected functions and raises `PermissionError` if denied.
  - `audit_action()` logs actions into `apt_toolkit_logs/audit.log` via a `logging` handler, and `environment_check()` flags potentially unsafe execution contexts.
- `apt_toolkit/initial_access.py` — Implements real spear-phishing and supply-chain logic with audit logging and ExploitDB enrichment.
  - `SpearPhishingGenerator` holds domain and lure subject lists, generates emails, embeds macros via `_generate_malicious_macro()`, writes placeholder documents in `_create_malicious_document()`, sends simulated emails with timestamps, and enriches the result by calling `enrich_with_exploit_intel()`.
  - `SupplyChainCompromise` models whether an implant should activate based on business hours and target domain suffix. `malicious_update_check()` returns a dictionary of conditions, logs via `audit_action()`, and returns an enriched structure; `execute_implant()` decides on `executed` vs `skipped`, optionally calls `_deploy_backdoor()`, and enriches as persistence intelligence.
  - Module functions `analyze_spear_phishing_campaign()` and `deliver_payload()` orchestrate the generator to produce campaign summaries or send payloads.
- `apt_toolkit/initial_access_enhanced.py` — Adds advanced tradecraft:
  - `AdvancedSocialEngineering` synthesises dossiers by simulating LinkedIn scraping, GitHub analysis, social-media monitoring, organisational mapping, and activity windows. `create_context_aware_lure()` uses industry news, engagement timing, and randomly selected templates to produce realistic email artefacts.
  - `PolyglotPayloadEngine` builds multi-format payloads: chooses a primary format, adds embedded formats, selects exploit chains based on environment flags (office/browser/system), constructs internal layering metadata, and describes obfuscation/delivery techniques.
  - `SupplyChainCompromise` variant keeps activation heuristics but returns raw dictionaries (used by enhanced modules). Helpers `analyze_advanced_social_engineering()` and `analyze_polyglot_payloads()` expose summarised outputs for analytics tooling.
- `apt_toolkit/persistence.py` — Implements baseline persistence with enforced authorization.
  - `PersistenceManager` collects OS metadata, creates scheduled tasks/crontab entries (`create_scheduled_task()`), WMI subscriptions (`create_wmi_event_subscription()`), registry run keys, and Windows services, each producing structured dictionaries and requesting enrichment metadata. Every action logs via `audit_action()`.
  - `_create_default_payload()` writes a PowerShell beacon script to a temp file. `install_multiple_persistence()` loops over selected techniques and aggregates results with a resilience rating. `analyze_persistence_techniques()` returns detection guidance for each mechanism, again enriched with exploit intel.
  - `generate_persistence_report()` composes a report by calling the creation methods and wrapping each output with ExploitDB enrichment.
- `apt_toolkit/persistence_enhanced.py` — Deep persistence and counter-forensics.
  - `AdvancedPersistenceFramework.install_multi_layer_persistence()` simultaneously installs WMI, scheduled task, COM hijack, and logon script persistence (using helper methods like `_install_wmi_persistence()`); adds stealth techniques if EDR is present, writes hidden marker files, and starts an ICMP beacon thread via `_start_backdoor_beacon()`.
  - `FilelessPersistence.establish_fileless_persistence()` returns strategies such as PowerShell profile loading, WMI class modification, and registry-stored payloads.
  - `CounterForensics.implement_counter_forensics()` documents timestomping, log cleaning, and memory anti-forensics. `analyze_advanced_persistence()` stitches all three components into a single analysis dictionary.
- `apt_toolkit/privilege_escalation.py` — `PrivilegeEscalator` offers:
  - `enumerate_ad_privileges()` that returns simulated AD high-value groups, their members, and recommended escalation techniques per group.
  - `check_vulnerabilities()` randomly marks major vulnerabilities (Zerologon, PrintNightmare, etc.) as present/absent with risk levels and exploitation availability, then prioritises them.
  - Helper methods `analyze_privilege_escalation_landscape()` aggregate enumeration, vulnerability scans, common APT techniques, and defence recommendations.
- `apt_toolkit/privilege_escalation_enhanced.py` — Adds:
  - `ADCSExploitationSuite.perform_adcs_escalation_scan()` enumerating ESC1/ESC2/ESC3/ESC6/ESC8 template weaknesses, computing risk assessments, and supplying exploitation guidance (tool lists, step-by-step actions).
  - `AdvancedKerberosAttacks.perform_kerberos_attack_suite()` runs Kerberoasting, AS-REP roasting, Golden/Silver/Diamond ticket simulations, returning vulnerable account lists, success/detection ratings, and references to specific APT behaviour. Also includes defence evasion summaries.
- `apt_toolkit/defense_evasion.py` — `DefenseEvader` focuses on LOTL and process hollowing.
  - `generate_lotl_commands()` returns command lists for download/execution/information gathering tasks, mapping to common Windows binaries.
  - `analyze_lotl_detection()` rates detection difficulty per tool, citing historic APT usage and defensive guidance.
  - `process_hollowing_analysis()` describes how process hollowing works and lists detection indicators. `generate_evasion_strategy()` chooses environment-specific combinations of LOTL abuse, process injection, and timing-based evasion. `analyze_defense_evasion_landscape()` collates everything into a comprehensive view for reporting.
- `apt_toolkit/defense_evasion_enhanced.py` — High sophistication evasion classes:
  - `AdvancedEDREvasion.execute_stealthy_payload()` selects direct syscall techniques (Hell's Gate/Halos Gate/manual), optionally patches ETW, bypasses AMSI, and documents execution/cleanup procedures. Returns detection risk assessments.
  - `AdvancedProcessInjection.perform_stealthy_injection()` randomly chooses among hollowing, atom bombing, herpaderping, or process ghosting, builds injection detail dictionaries, and returns the evasion measures (memory wiping, handle cleanup).
  - `AdvancedLOTLTechniques` enumerates abuse cases for MSBuild, InstallUtil, mshta, and rundll32, providing file paths and execution patterns.
- `apt_toolkit/lateral_movement.py` — `LateralMover` handles lateral discovery and exploitation:
  - `discover_network_segments()` iterates predefined government subnets, simulates discovery success, records visited subnets, and ranks them with prioritisation metadata.
  - `pass_the_hash_lateral()` simulates PTH attempts: builds success-factor dictionaries (hash validity, reachability, admin privileges, defences), determines success/failure, and injects follow-up steps or failure reasons.
  - `deploy_implant()` describes the implant type (beacon/keylogger/recon) with persistence and communication channel metadata, plus success probability.
  - `analyze_lateral_movement_campaign()` composes a mini campaign by running discovery, two PTH attempts, implant deployments, and `analyze_lateral_movement_techniques()` to describe detection countermeasures.
- `apt_toolkit/command_control.py` — `C2Communicator` provides:
  - `send_beacon()` that chooses domain-fronted or direct C2, sets headers, base64-encodes payloads, determines success/failure with reasons, and lazily starts covert DNS/ICMP channels via `_activate_covert_channel()`.
  - `_start_dns_covert_channel()` and `_start_icmp_covert_channel()` spawn daemon threads that repeatedly beacon using DNS lookups or `ping`, handling exceptions and random sleep intervals.
  - `_start_backdoor_listener()` spins up a TCP listener on localhost waiting for commands, returning JSON-encoded responses.
  - `analyze_c2_channels()`, `generate_encryption_strategy()`, and `simulate_c2_lifecycle()` evaluate C2 channel types, choose encryption plans, and run multiple beacon attempts to show success/failure rates. Module-level `analyze_c2_infrastructure()` aggregates channel analysis, sample beacons, lifecycle simulation, APT patterns, and defensive recommendations.
- `apt_toolkit/exfiltration.py` — `DataExfiltrator` code paths:
  - `find_sensitive_data()` simulates searching common directories, filters discovered files, calculates aggregate sizes, classifies by sensitivity, and enriches the result.
  - `_classify_data()` sorts files into classification buckets. `slow_exfiltrate()` simulates chunk-by-chunk transfers with success flags, wait times, completion percentage, and estimated total duration.
  - `analyze_exfiltration_methods()` compares HTTPS/DNS/FTP/Cloud channels (stealth, bandwidth, reliability, detection vectors).
  - `generate_exfiltration_strategy()` selects strategy/method/timeframe based on total size and file count, lists precautions.
  - `analyze_exfiltration_campaign()` chains data discovery, strategy, method analysis, and sample exfiltrations.
- `apt_toolkit/exploit_intel.py` — Handles offline ExploitDB enrichment:
  - Defines `_KEEP_COLUMNS`, `_MODULE_ALIGNMENT`, mappings from exploit types to toolkit modules, and dataclass `ExploitEntry` with `to_dict()`.
  - `ExploitDBIndex` lazily loads CSV datasets, caches results, and exposes `search_exploits()`, `search_shellcodes()`, `search_by_cve()`, `get_recent_activity()`, and `analyze_exploit_surface()` (counts module alignment, derives detection focus).
  - Internal helpers `_apply_search()`, `_filter_by_code()`, `_filter_recent()`, `_derive_detection_focus()`, `_normalise_terms()` implement the filtering logic.
  - `recommend_for_module()` (and the free function `module_recommendations`) build tailored intel packets, optionally including exploit payload snippets.
  - Raises `ExploitDBNotAvailableError` when the dataset is missing.
- `apt_toolkit/offensive_playbooks.py` — Composes offensive playbooks by normalising module lists, generating per-module search term sets, calling `module_recommendations()`, and packing results (target product, platform, module intel) into a dictionary.
- `apt_toolkit/campaign.py` — Full campaign orchestrator:
  - `CampaignConfig` dataclass collects campaign options (domain, IP, beacons, enabling supply chain/counter-forensics, random seed).
  - `APTCampaignSimulator` constructs module instances in `__init__`, then `simulate()` seeds randomness, calls private `_simulate_*` methods, and gathers results.
  - `_simulate_initial_access()` uses `AdvancedSocialEngineering`, `PolyglotPayloadEngine`, and optionally `SupplyChainCompromise` to build initial foothold data.
  - `_simulate_persistence()`, `_simulate_privilege_escalation()`, `_simulate_defense_evasion()`, `_simulate_lateral_movement()`, `_simulate_command_control()`, and `_simulate_exfiltration()` each orchestrate the respective modules, enrich outputs, and return structured dictionaries.
  - Helper methods `_derive_stolen_hashes()`, `_derive_target_hosts()`, `_build_timeline()`, and `_summarize_takeaways()` create timeline entries, takeaways (including success counts), and ensure data is consistent.
  - `simulate_campaign()` convenience wrapper instantiates the simulator with defaults.
- `apt_toolkit/cli.py` — Argparse front-end:
  - Defines subparsers for every module. Each parser sets module-specific flags (`--generate-email`, `--analyze`, etc.).
  - Conditionals guard Chinese APT support: tries to import `ChineseAPTCampaignOrchestrator`; if available, defines the `chinese-apt` subparser with campaign choices and `--domain`/`--seed` options.
  - `main()` parses arguments, prints help if no module specified, and handles JSON vs pretty output. Exception handling writes error messages to stderr.
  - `handle_command()` dispatches to module functions/classes and returns dictionaries keyed by result type. Chinese APT branch instantiates the orchestrator, optionally runs comparative analysis, or executes a specific campaign. Includes an `exploitdb` block that builds responses based on up to five CLI options. The final fallback returns an error dictionary.
  - `print_pretty_result()` renders nested dict/list structures with simple formatting.
- `apt_toolkit/cli_backup.py` — Snapshot of the pre-Chinese CLI. Same structure as `cli.py` but without conditional imports or handlers for the Chinese orchestrator. Serves as a fallback reference.
- `apt_toolkit/american_targets.py` — Provides `analyze_american_targets()` which:
  - Seeds randomness if requested, instantiates `AdvancedSocialEngineering` and `SupplyChainCompromise`, generates target domains, builds dossiers/lures per domain, executes supply-chain readiness checks, and collects implant outcomes. Returns a dictionary with timestamp, network list, profile list, and supply-chain readiness entries.
  - Helper functions `_generate_target_domain()` and `_generate_target_email()` create domain/email strings.
- `apt_toolkit/chinese_apt_campaign/c2_server.py` — Simple UDP DNS-like server. Creates a socket on port 53, loops on `recvfrom()`, attempts to base64-decode the first label of the query, prints decoded payloads, and catches decoding errors. Demonstrates how exfiltrated data would be received.
- `apt_toolkit/chinese_apt_campaign/custom_backdoor.py` — Backdoor class used by Chinese campaign examples:
  - `disguise_process()` placeholder (ready for enhancement), `establish_persistence()` installs persistence (scheduled task on Windows, cron on Unix), `dns_tunnel()` encodes data via base64 and issues DNS lookups, and `run()` loops executing placeholder commands (`hostname`), beacons results via DNS, and sleeps. Uses `socket`, `subprocess`, and `time` modules.
- `apt_toolkit/chinese_apt_campaign/spear_phishing_generator.py` — Builds a spear-phishing email:
  - `create_malicious_attachment()` writes a `.vbs` dropping the backdoor script.
  - `send_spear_phishing_email()` constructs a multipart email with attachments and sends via SMTP (Gmail host/port). The `__main__` block assembles the attachment, sends the email, and removes the temporary VBS file.
- `apt_toolkit/chinese_apt_campaign/tools/com_hijacker.cpp` — Windows COM hijacker. Opens/creates an HKCU CLSID key and sets the default value to the malicious DLL path, thereby redirecting COM activation to the payload.
- `.../dns_exfil.ps1` — PowerShell DNS exfiltration: reads a file, hex-encodes contents, splits into 63-character chunks (DNS label limit), issues `Resolve-DnsName` queries for each chunk, and throttles with `Start-Sleep`.
- `.../domain_fronting_implant.go` — Go beacon using domain fronting. Builds an HTTP request to a fronting domain but sets `req.Host` to the real C2 host, reads response bodies as commands, and loops with a one-minute sleep.
- `.../fileless_loader.cs` — Downloads a DLL via `WebClient.DownloadData`, loads it into memory with `Assembly.Load`, and invokes its entry point via reflection. No disk writes, illustrating fileless execution.
- `.../icmp_c2_implant.py` — Sends ICMP echo requests in a loop. Builds raw packets, calculates checksums, embeds data/time, and sends to the C2 host. Requires raw socket privileges.
- `.../linux_rootkit.c` — Simple Linux kernel module. On init, iterates `task_struct` processes, removes the one matching `PROCESS_TO_HIDE` from the scheduler’s task list (`list_del(&task->tasks)`), effectively hiding it. Logs messages via `printk` on load/unload.
- `.../lsass_dumper.cpp` — Windows MiniDump LSASS dumper. Prompts for LSASS PID, opens the process with `OpenProcess(PROCESS_ALL_ACCESS)`, creates `lsass.dmp`, and calls `MiniDumpWriteDump`. Includes failure handling for each stage.
- `.../process_injector.go` — Windows process injection in Go. Obtains a handle with `OpenProcess`, allocates remote memory (`VirtualAllocEx`), writes decoded shellcode (`WriteProcessMemory`), and launches a remote thread (`CreateRemoteThread`). Shellcode placeholder string is meant to be replaced by the operator.
- `.../ssh_keylogger.py` — Wraps an arbitrary command (typically `ssh`). Forks a pseudo-terminal with `pty.fork()`, proxies data between stdin/stdout and the child file descriptor, and logs everything to `/tmp/.ssh_logs.txt`.
- `.../steganography.py` — Uses PIL to encode binary strings in the LSB of RGB pixels, saving to a new image. `decode_image()` reconstructs the binary stream and stops at a “DELIMITER”. The `__main__` block demonstrates encoding/decoding a sample message.
- `.../watering_hole.js` — JavaScript payload that collects browser fingerprint data (userAgent, platform, language, cookies, localStorage, sessionStorage) and POSTs it to a C2 endpoint. Designed for injection into compromised web pages.
- `.../weaponized_macro.ps1` — PowerShell downloader run from a macro. Downloads a payload to `%TEMP%\payload.exe`, executes it, and optionally self-destructs.
- `.../wmi_persistence.vbs` — VBScript establishing a WMI event subscription: creates a script consumer and event filter firing on `Win32_LogonSession` creation, binding them so the payload runs at logon.

### Campaign Modules (Chinese APT)
- `campaigns/chinese_apts/__init__.py` — Re-exports the four campaign simulator classes for easy import.
- `campaigns/chinese_apts/apt41_campaign.py` — Specialises `APTCampaignSimulator` for APT41:
  - `APT41CampaignConfig` adds toggles for gaming-industry targeting, polyglot payload usage, and supply-chain compromise, defaulting to known malware families.
  - `APT41CampaignSimulator.simulate_gaming_industry_campaign()` seeds randomness, generates APT41-specific initial access (multiple developer emails, polyglot payload arrays, supply-chain metadata), persistence (WMI, scheduled tasks, fileless techniques), and defense evasion (EDR evasion plus process injection). It then merges these with the base simulator results.
- `campaigns/chinese_apts/apt1_campaign.py` — Mirrors the pattern for APT1:
  - `APT1CampaignConfig` toggles government/defense targeting and long-term espionage.
  - `simulate_government_espionage_campaign()` builds target email lists, social engineering themes, payload types, and attack vectors; enumerates persistence techniques (service, registry run keys, scheduled task, WMI) with descriptors; and details command & control infrastructure (bulletproof hosting, communication protocols, redundancy). Also returns espionage focus metadata.
- `campaigns/chinese_apts/apt10_campaign.py` — Focuses on MSP/cloud compromises: config emphasises MSP targeting, credential theft, and cloud abuse; simulator generates MSP initial access channels, persistence in cloud management portals, and exfiltration specifics tailored to APT10 operations.
- `campaigns/chinese_apts/apt12_campaign.py` — Models diplomatic targeting: includes watering-hole initial access, multi-layer persistence, long dwell times, and slow exfiltration, plus metadata about APT12 malware families and geopolitical objectives.
- `campaigns/chinese_apts/chinese_apt_orchestrator.py` — Orchestrates all Chinese campaigns:
  - `ChineseAPTCampaignConfig` toggles which campaigns to run and passes per-group configs.
  - `ChineseAPTCampaignOrchestrator.run_comparative_analysis()` invokes each simulator, collects output, and `_generate_comparative_analysis()` summarises targeting focus, tactical approaches, malware characteristics, and operational patterns across groups. `_get_chinese_apt_overview()` returns a reference dataset describing each APT, common characteristics, detection challenges, and mitigation strategies.
- `campaigns/chinese_apt_lockheed_campaign/run_campaign.py` — Standalone script (using older module names) that reads `targets.txt`, loops through each target, calls functions like `supply_chain_compromise()` or `spear_phishing()` (from earlier modules), sets up persistence, starts DNS/ICMP covert channels, and performs DNS/ICMP exfiltration. Structured as a sequential print-heavy simulation.
- `campaigns/chinese_apt_lockheed_campaign/README.md` — Describes “Operation Dragon’s Fire” campaign objectives, targets, and toolkit use.
- `campaigns/chinese_apt_lockheed_campaign/targets.txt` — Plain list of target strings read by `run_campaign.py`.
- `campaigns/chinese_apts/__pycache__/...` — Compiled bytecode caches (no source logic).

## Examples
- `examples/advanced_apt_analysis.py` — Demonstrates advanced toolkit usage. Imports core classes (`APTCampaignSimulator`, `AdvancedSocialEngineering`, `ADCSExploitationSuite`, etc.), defines helper functions that call into the toolkit to print human-readable analyses (social engineering results, persistence layers, ADCS scan results, Kerberos attacks, EDR evasion, polyglot payloads), runs a full campaign simulation (seeded for reproducibility), prints timeline highlights and key takeaways, and showcases ExploitDB queries. It shows how modules interoperate.
- `examples/offensive_demonstration.py` — Walkthrough script (not opened here but typically) that chains initial access, persistence, privilege escalation, lateral movement, C2, and exfiltration functions to present a linear offensive scenario, printing results at each stage.

## Red Team Toolkit (`red_team_china_apt`)
### Attack Chains
- `red_team_china_apt/attack_chains/gilded_dragon_chain.py` — Orchestrates an attack chain combining the toolkit modules: imports the spear phisher, DNS C2 implant, and steganographer, sends an email with a malicious doc (`create_malicious_doc()` writes a placeholder file), simulates C2 exfiltration (`exfiltrate("implant_checkin")`), and hides LSASS dump data in an image via steganography.
- `.../silicon_dragon_chain.py` — Simulates a supply-chain compromise leading to DNS beacon exfiltration (`DNSC2Implant.exfiltrate()`), process injection (printed placeholder), and IP theft of source code. Emphasises the steps used by APT41-like operations.
- `.../serpent_rx_chain.py` — Demonstrates a watering-hole attack: prints infection steps, simulates fileless execution, calls a PowerShell WMI persistence script, and hides research data using steganography.
### Campaign Briefings
- `red_team_china_apt/campaigns/operation_serpent_rx.md`, `operation_silicon_dragon.md`, `operation_gilded_dragon.md` — Narrative briefings describing objectives, targets, and phases for each operation.
### Toolkit Components
- `red_team_china_apt/toolkit/dns_c2_implant.py` — Same DNS exfiltration implementation as the Chinese campaign toolkit (base64 chunks, DNS queries, timed beacons).
- `.../lsass_dumper.cpp` — Windows LSASS dumper implemented in C++ using `MiniDumpWriteDump` (identical to the Chinese toolkit version).
- `.../process_injector.cpp` — Windows API-based injector in C++: opens a target process, allocates memory with `VirtualAllocEx`, writes shellcode, and calls `CreateRemoteThread` to execute it.
- `.../spear_phisher.py` — SMTP client class `SpearPhisher` sending emails with optional attachments (mirrors the version used in attack chains).
- `.../steganographer.py` — PIL-backed encoder/decoder storing bits in pixel channels; used by attack chain scripts.
- `.../wmi_persistence.ps1` — PowerShell script creating a WMI event filter and consumer, binding them to execute a payload on logon.

## Tools Directory (`tools/`)
- `tools/README.md` — Describes each auxiliary tool, prerequisites, and intended usage scenarios.
- `tools/APT-PowerShell-Toolkit.ps1` — Large PowerShell module offering:
  - Banner output and admin privilege checks.
  - `Invoke-APTRecon` collects system metrics (processes, services, users, network info) and writes JSON files under a timestamped directory.
  - `Invoke-APTPersistence` requires admin rights and installs scheduled tasks, registry run keys, WMI event subscriptions, and Windows services; outputs JSON summaries of each mechanism.
  - `Invoke-APTPrivEsc` inspects unquoted service paths, weak service permissions, AlwaysInstallElevated registry keys, and current token privileges, exporting each result set to JSON.
  - `Invoke-APTDefenseEvasion` (extends into AMSI bypass, event log tampering, script block modifications). The script orchestrates switches (`-Recon`, `-Persistence`, etc.) and writes outputs consistently.
- `tools/apt_recon.sh` — Bash reconnaissance script that gathers hostnames, OS info, running processes, listening ports (using `netstat`/`ss`), and saves results to timestamped directories. Provides command pipelines typical of Unix recon.
- `tools/apt_persistence.py` — Python script that installs persistence on Windows: manipulates registry keys via `winreg`, creates scheduled tasks using `schtasks`, and optionally installs services. Contains classes/functions mirroring the toolkit but designed for standalone use.
- `tools/apt_network_scanner.go` — Go program that iterates IP ranges, attempts TCP connections on common ports, records open ports, and formats output. Uses Go’s concurrency primitives for scanning efficiency.
- `tools/apt_social_engineering.rb` — Ruby script that generates spear-phishing templates, scheduling logic, and optionally integration with mail APIs. It manipulates strings to produce personalised messages per target list.
- `tools/apt_web_recon.js` — JavaScript/Node script performing HTTP requests, fingerprinting servers (headers, technologies), and logging results to assist with initial access planning.
- `tools/apt_memory_injector.c` — C program for Windows injection using the WinAPI (`OpenProcess`, `VirtualAllocEx`, `WriteProcessMemory`, `CreateRemoteThread`).
- `tools/apt_web_recon.js`, `tools/setup_tools.sh` — Setup script installing dependencies across platforms.
- `tools/test_tools.sh` — Smoke-test script that runs the auxiliary tools to ensure they execute.

## Tests (`tests/`)
- `tests/test_cli_american.py` — `unittest` file that patches datetime to make outputs deterministic, checks that `analyze_american_targets()` returns consistent structures (domains, profiles, supply-chain readiness), and verifies that `handle_command()` routes the `american targets` CLI command correctly.
- `tests/test_cli_exploitdb.py` — Tests `handle_command()` for the `exploitdb` module by patching `ExploitDBIndex` methods, ensuring search, CVE lookup, recent activity, and playbook generation features populate the response dictionary properly.
- `tests/test_campaign_simulator.py` — Validates `APTCampaignSimulator` end-to-end: ensures each phase exists in the returned report, timeline entries are generated, persistence/counter-forensic toggles work, and takeaways mention pass-the-hash success counts.
- `tests/test_initial_access_enhanced.py` — Confirms `AdvancedSocialEngineering` and `PolyglotPayloadEngine` outputs include expected keys (dossiers, lures, payload configs), verifying reproducibility with seeds.
- `tests/test_exploit_intel.py` — Exercises `ExploitDBIndex` search functionality, caching behaviour, CVE lookups, and raises `ExploitDBNotAvailableError` when appropriate. Uses temporary files/mocks to simulate dataset presence.
- `tests/test_chinese_apt_campaigns.py` — Ensures each Chinese APT simulator returns group-specific data and that the orchestrator’s comparative analysis populates targeting focus, tactical approaches, malware characteristics, and operational patterns.
- `tests/apt_toolkit_logs/audit.log` — Empty file used during tests so that audit logging writes to a predictable path without touching real log directories.
- `tests/__pycache__/...` — Autogenerated bytecode caches for the tests.

## Logs and Metadata
- `apt_toolkit_logs/audit.log` — Placeholder log file created so that `SafetyController` logging succeeds. Populated when toolkit functions call `audit_action()`.
- `apt_toolkit.egg-info/*` — Generated by setuptools. Includes `PKG-INFO` (metadata copy of setup.py), `SOURCES.txt` (file manifest), `entry_points.txt` (console scripts), `dependency_links.txt`, and `top_level.txt` (lists top-level packages). No executable logic.

## Compiled Bytecode Directories
- `apt_toolkit/__pycache__/`, `campaigns/chinese_apts/__pycache__/`, `tests/__pycache__/` — CPython cache directories containing `.pyc` files for faster loading. They mirror the Python source files but do not hold additional code.

## Miscellaneous
- Any additional `__pycache__` directories or temporary files that appear after running the toolkit are artefacts and can be regenerated; the repository ships without them except where noted above.
