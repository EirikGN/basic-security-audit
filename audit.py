#!/usr/bin/env python3
import os
import subprocess

def is_wsl():
    """Detect if running inside Windows Subsystem for Linux."""
    return "microsoft" in os.uname().release.lower()

def check_firewall():
    """Check UFW firewall status."""
    if is_wsl():
        print("[Firewall] WSL detected — cannot reliably check firewall")
        return
    try:
        result = subprocess.run(['ufw', 'status'], capture_output=True, text=True)
        print("[Firewall] " + result.stdout.splitlines()[0])
    except FileNotFoundError:
        print("[Firewall] ufw not installed")

def check_ssh_root_login():
    """Check if root login is allowed in SSH configuration."""
    ssh_file = '/etc/ssh/sshd_config'
    try:
        with open(ssh_file) as f:
            for line in f:
                if line.strip().lower().startswith("permitrootlogin"):
                    print("[SSH] " + line.strip())
                    return
        print("[SSH] PermitRootLogin not set")
    except FileNotFoundError:
        print("[SSH] Config file not found")

def check_critical_files():
    """Check permissions of key system files."""
    files = ['/etc/passwd', '/etc/shadow']
    for f in files:
        try:
            perms = oct(os.stat(f).st_mode)[-3:]
            print(f"[File] {f} permissions: {perms}")
        except FileNotFoundError:
            print(f"[File] {f} not found")

def check_uid0_users():
    """List users with administrative (UID 0) privileges."""
    try:
        with open('/etc/passwd') as f:
            users = [line.split(':')[0] for line in f if line.split(':')[2] == '0']
            print(f"[UID0] Users with UID 0: {', '.join(users)}")
    except FileNotFoundError:
        print("[UID0] /etc/passwd not found")

def check_updates():
    """Check for available package updates."""
    try:
        result = subprocess.run(
            ['apt', 'list', '--upgradable'],
            stdout=subprocess.PIPE,
            text=True
        )
        count = len(result.stdout.splitlines()) - 1
        print(f"[Updates] {count} packages can be updated")
    except FileNotFoundError:
        print("[Updates] apt not available")

if __name__ == "__main__":
    print("=== Basic Linux Security Audit ===")
    if is_wsl():
        print("[Info] Running inside WSL — some checks may not reflect a real Linux system")
    check_firewall()
    check_ssh_root_login()
    check_critical_files()
    check_uid0_users()
    check_updates()
    print("=== Audit Complete ===")

