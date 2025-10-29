# Red Team Campaign: OperationSiliconDragon

## 1. Executive Summary

OperationSiliconDragon is a Red Team campaign simulating a Chinese APT group targeting the United States technology and defense sectors. The primary objectives are to steal intellectual property, compromise sensitive government and military data, and gain a strategic advantage in the global technology landscape.

## 2. Campaign Objectives

*   **Primary**:
    *   Exfiltrate source code, trade secrets, and proprietary algorithms.
    *   Gain access to sensitive defense and military data.
    *   Compromise the supply chain of major technology and defense companies.
*   **Secondary**:
    *   Establish a long-term presence in the networks of key targets.
    *   Map the network architecture of research and development environments.
    *   Test the security posture of organizations against a determined nation-state adversary.

## 3. Target Profile

*   **Primary Targets**:
    *   **Technology**: Google, Microsoft, Apple, Amazon (AWS), Intel, NVIDIA.
    *   **Defense**: Lockheed Martin, Northrop Grumman, Raytheon, General Dynamics.
*   **Secondary Targets**:
    *   Semiconductor companies.
    *   Cloud service providers.
    *   Government contractors.

## 4. Attack Lifecycle

*   **Initial Access**:
    *   Supply chain attacks through compromised software updates.
    *   Spear-phishing campaigns targeting engineers and developers.
    *   Zero-day exploits targeting unpatched vulnerabilities.
*   **Execution & Persistence**:
    *   Custom rootkits and bootkits for deep persistence.
    *   Firmware modification of network devices.
*   **Defense Evasion**:
    *   Bypassing virtualization-based security (VBS).
    *   Use of polymorphic and metamorphic malware.
*   **Command & Control**:
    *   Custom C2 protocols to evade detection.
    *   Use of satellite communication for C2 in air-gapped networks.
*   **Credential Access**:
    *   Golden Ticket attacks to gain domain-wide administrative access.
    *   Pass-the-Hash for lateral movement.
*   **Exfiltration**:
    *   Exfiltration of data through covert channels.
    *   Use of data diodes to exfiltrate data from secure networks.
