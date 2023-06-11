import argparse
import configparser
import poe

def generate_template(vulnerability, api_key):
    # Create a Poe client instance
    client = poe.Client(api_key)

    # Construct the prompt for generating the bug report template
    prompt = f"""You are a security researcher participating in a bug bounty program on hackerone.com. You have identified a potential security vulnerability related to "{vulnerability}" that needs to be reported. Please provide the following details:

Bug Bounty Report: 

Vulnerability Type: {vulnerability}

## Summary
[Provide a concise summary of the vulnerability]

## Description
[Describe the vulnerability in detail, including the affected functionality or code]

## Vulnerable HTTP Request
[Provide vulnerable raw HTTP Request]

## Steps to Reproduce
[Provide clear and detailed steps to reproduce the vulnerability]

## PoC
[Proof of concept of the vulnerability]

## Impact
[Explain the potential impact an attacker could have if they exploit this vulnerability]

## CVSS Score
Predict the CVSS score for the following vulnerability,also give a CVSS vector string.

Attack Vector: [Describe how an attacker could exploit this vulnerability]
Attack Complexity: [Specify the complexity of the attack]
Privileges Required: [Indicate the privileges required to exploit the vulnerability]
User Interaction: [Specify if user interaction is required for exploitation]
Scope: [Specify the scope of the vulnerability (changed impact beyond the vulnerable component)]
Confidentiality Impact: [Describe the potential impact on confidentiality]
Integrity Impact: [Describe the potential impact on integrity]
Availability Impact: [Describe the potential impact on availability]

Based on the provided information, please predict the CVSS score for this vulnerability.


## Recommendation
[Offer recommendations on how to fix or mitigate the vulnerability]

Best regards,
[Your username]
"""

    response = ""
    # Send the prompt to the Poe client and receive the response
    for chunk in client.send_message("chinchilla", prompt):
        print(chunk["text_new"], end="", flush=True)
    client.send_chat_break("chinchilla")
    client.purge_conversation("chinchilla")


def main():
    # Load the API key from the config.ini file
    config = configparser.ConfigParser()
    config.read("config.ini")
    api_key = config["DEFAULT"]["API_KEY"]

    # Create an argument parser for the script
    parser = argparse.ArgumentParser(description="Bug Report Generator")
    parser.add_argument("-gt", metavar="VULNERABILITY", help="Generate a bug report template based on the vulnerability", required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    if args.gt:
        # Retrieve the vulnerability from the command-line arguments
        vulnerability = args.gt

        # Generate the bug report template based on the vulnerability and API key
        generate_template(vulnerability, api_key)

if __name__ == "__main__":
    main()
  
