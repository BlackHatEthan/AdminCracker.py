import ctypes
import os
import sys
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate():
    # Re-run the script with admin privileges
    script = sys.argv[0]
    params = ' '.join(sys.argv[1:])
    subprocess.call(['powershell', '-Command', f'Start-Process python "{script}" -ArgumentList "{params}" -Verb runAs'])

def create_admin_user(username, password):
    try:
        # Create new user
        subprocess.call(['net', 'user', username, password, '/add'])
        # Add to administrators group
        subprocess.call(['net', 'localgroup', 'administrators', username, '/add'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if not is_admin():
        elevate()
        sys.exit()

    # Replace with desired username and password
    create_admin_user('newadmin', 'P@ssw0rd123')
