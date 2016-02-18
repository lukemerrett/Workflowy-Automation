from setuptools import setup, find_packages

setup(
    name="workflowy.automation",
    packages=find_packages(),
    author="Luke Merrett",
    description="Scripts for automating Workflowy tasks using Selenium",
    license="MIT",
    url="https://github.com/lukemerrett/Workflowy-Automation",
    install_requires=['selenium']
)
