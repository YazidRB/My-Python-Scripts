import paramiko
import time
import random

# Set the target IP address and port
target_ip = "127.0.0.1"
target_port = 22  # SSH port

# Set the imaginary IP address
imaginary_ip = "203.0.113.1"

# Set the number of login attempts
num_attempts = 100

# Function to attempt SSH login
def ssh_login(username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target_ip, port=target_port, username=username, password=password, timeout=5)
        print(f"Successful login as {username} with password {password} from {imaginary_ip}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print(f"Failed login attempt as {username} with password {password} from {imaginary_ip}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Loop through login attempts
for i in range(num_attempts):
    # Generate a random username and password for each attempt (for demonstration purposes)
    username = "wazuh" 
    password = "password" + str(random.randint(1, 100))

    # Simulate a login attempt
    print(f"Attempting to login as {username} with password {password} from {imaginary_ip}")

    # Attempt SSH login
    ssh_login(username, password)

    # Simulate a delay between attempts
    time.sleep(1)  # Add a delay to avoid overwhelming the target system

print("Login attempts completed.")
