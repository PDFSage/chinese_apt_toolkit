# Red Team Campaign: Operation SerpentRx

## 1. Executive Summary

Operation SerpentRx is a Red Team campaign simulating a Chinese APT group targeting the United States healthcare and pharmaceutical sectors. The primary objectives are to steal intellectual property (e.g., drug formulas, research data), access sensitive patient data, and disrupt healthcare operations.

## 2. Campaign Objectives

*   **Primary**:
    *   Exfiltrate proprietary research and development data.
    *   Steal sensitive patient health information (PHI).
    *   Disrupt clinical trials and research activities.
*   **Secondary**:
    *   Gain long-term access to healthcare networks.
    *   Map the network architecture of research and clinical systems.
    *   Test the incident response capabilities of healthcare organizations.

## 3. Target Profile

*   **Primary Targets**:
    *   Pfizer
    *   Johnson & Johnson
    *   Merck
    *   AbbVie
    *   Major hospital chains (e.g., HCA Healthcare, Mayo Clinic).
*   **Secondary Targets**:
    *   Biotechnology companies.
    *   Medical device manufacturers.
    *   Health insurance providers.

## 4. Attack Lifecycle

*   **Initial Access**:
    *   Spear-phishing campaigns targeting researchers and clinicians.
    *   Exploitation of vulnerabilities in electronic health record (EHR) systems.
    *   Watering hole attacks on medical journals and conference websites.
*   **Execution & Persistence**:
    *   Custom malware designed to operate in sterile environments.
    *   Use of legitimate administrative tools for persistence (e.g., PowerShell).
*   **Defense Evasion**:
    *   Application whitelisting bypasses.
    *   Time-stomping to alter malware timestamps.
*   **Command & Control**:
    *   HTTPS for C2 communication to blend in with normal traffic.
    *   Use of compromised medical devices for C2.
*   **Credential Access**:
    *   Credential harvesting from medical professionals.
    *   Kerberoasting to extract service account credentials.
*   **Exfiltration**:
    *   Exfiltration of data to academic or research-themed domains.
    *   Use of custom encryption to hide exfiltrated data.
