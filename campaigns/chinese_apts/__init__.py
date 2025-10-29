"""
Chinese APT Campaign Module

This module provides specialized campaign simulation capabilities for Chinese APT groups
including APT41 (Winnti), APT1 (Comment Crew), APT10 (Stone Panda), and APT12 (Numbered Panda).

Legal and Ethical Notice:
This module is for authorized security testing, defensive research, and educational purposes only.
"""

from .apt41_campaign import APT41CampaignSimulator
from .apt1_campaign import APT1CampaignSimulator
from .apt10_campaign import APT10CampaignSimulator
from .apt12_campaign import APT12CampaignSimulator

__all__ = [
    "APT41CampaignSimulator",
    "APT1CampaignSimulator", 
    "APT10CampaignSimulator",
    "APT12CampaignSimulator",
]