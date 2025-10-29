# Red Team Campaign: Operation GildedDragon

## 1. Executive Summary

Operation GildedDragon is a Red Team campaign simulating a Chinese APT group targeting the United States financial sector. The primary objectives are to gain access to sensitive financial data, disrupt operations, and test the resilience of financial institutions against a sophisticated state-sponsored threat actor.

## 2. Campaign Objectives

*   **Primary**:
    *   Exfiltrate sensitive customer data, including PII and financial records.
    *   Gain access to internal trading and transaction systems.
    *   Simulate the disruption of critical financial services.
*   **Secondary**:
    *   Establish long-term persistence in the network.
    *   Map the internal network architecture and identify key assets.
    *   Test the organization's incident response capabilities.

## 3. Target Profile

*   **Primary Targets**:
    *   JPMorgan Chase
    *   Bank of America
    *   Citigroup
    *   Wells Fargo
    *   Goldman Sachs
*   **Secondary Targets**:
    *   Regional banks and credit unions.
    *   Financial technology (FinTech) companies.
    *   Stock exchanges (NYSE, NASDAQ).

## 4. Attack Lifecycle

*   **Initial Access**:
    *   Spear-phishing campaigns targeting employees with access to sensitive systems.
    *   Watering hole attacks on financial news websites.
    *   Exploitation of vulnerabilities in public-facing applications.
*   **Execution & Persistence**:
    *   Custom malware loaders to execute payloads in memory.
    *   WMI and Scheduled Tasks for persistence.
    *   COM hijacking for stealthy persistence.
*   **Defense Evasion**:
    *   Process injection to hide malicious code in legitimate processes.
    *   Rootkits to hide files and processes.
    *   Code signing certificates to bypass security controls.
*   **Command & Control**:
    *   DNS and ICMP tunneling for covert communication.
    *   Domain fronting to hide C2 traffic.
*   **Credential Access**:
    *   LSASS memory dumping to extract credentials.
    *   Keylogging to capture user credentials.
*   **Exfiltration**:
    *   Steganography to hide data in images.
    *   DNS exfiltration for small payloads.
    *   Encrypted archives uploaded to cloud storage providers.
