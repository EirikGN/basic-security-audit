Basic Linux Security Audit

This is a small Python script that runs a few basic security checks on a Linux system.
It checks common areas like the firewall, SSH settings, file permissions, and available updates.
The script can be useful for simple system reviews.

What the script checks:
Check	       
Firewall	Checks if the UFW firewall is active (skipped when running in WSL).
SSH root login	Checks whether root login is allowed in /etc/ssh/sshd_config.
Critical files	Shows permissions for /etc/passwd and /etc/shadow.
UID 0 users	Lists users that have administrative (root) privileges.
Updates	Lists how many software packages can be updated.

How to use:

Clone or download this repository from GitHub.

Open a terminal and go into the project folder.

Make the script executable by running:
chmod +x audit.py

Run the script:
./audit.py

If you are running it in Windows through WSL, some results (like the firewall check) may not reflect the actual Windows system.
The script will detect WSL and print a note when this happens.

Example output

=== Basic Linux Security Audit ===
[Info] Running inside WSL — some checks may not reflect a real Linux system
[Firewall] WSL detected — cannot reliably check firewall
[SSH] PermitRootLogin not set
[File] /etc/passwd permissions: 644
[File] /etc/shadow permissions: 640
[UID0] Users with UID 0: root
[Updates] 110 packages can be updated
=== Audit Complete ===

Why I made this

I created this project to practice Python scripting and improve my understanding of basic Linux security.
It’s a small and clear example of how system checks can be automated using Python.

Author:
Eirik Gjertsen Norbye
GitHub: https://github.com/eirikGN
