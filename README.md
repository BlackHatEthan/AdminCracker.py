# AdminCracker.py

Elevate privileges. Unlock hidden admin rights.

## Overview

AdminCracker.py is a powerful tool designed to bypass administrative restrictions on Windows machines. By leveraging the built-in user management system, this script can create a new admin account with just a few lines of code, giving you full access to the system.

This script isn't about breaking into systems—it’s about testing and hacking your own limits. Use it wisely, and remember: the line between white and grey is thin.

## Features

Privilege Escalation: Automatically creates a new user with administrator privileges on the target machine.
No Admin Access? No Problem: If you don’t have admin privileges to run the script, it’ll automatically elevate itself to administrator using Windows’ runAs command.
Minimal Setup: No complicated installations. Just run the script, and you’re in.
Powerful Flexibility: This script can be modified to meet specific needs, whether for local security testing or system recovery.

## How it Works

The script first checks if the current user has admin privileges.
If not, it re-launches the script with elevated privileges (using runAs).
Once admin rights are gained, it creates a new admin user on the system by calling the net user command.
The new admin is added to the administrators group, giving full access to the system.
