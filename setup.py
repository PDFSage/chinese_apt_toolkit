"""
Setup configuration for APT Toolkit
"""

from setuptools import setup, find_packages

setup(
    name="apt-toolkit",
    version="3.0.0",
    description="Advanced Persistent Threat offensive toolkit for authorized penetration testing",
    author="Security Research Team",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'apt-analyzer=apt_toolkit.cli:main',
            'apt-offensive=apt_toolkit.cli_enhanced:main_enhanced',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: Education",
    ],
)