#Dependancies
import paramiko
import time

'''Getting Target Information'''
host = input("Enter Host Name:")
port = input("Enter Port:")
print("Target Acquired! Setting Up Paramiko environment........")
time.sleep(1)

'''Setting Paramiko'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Paramiko All Set Up Successfully... Attempting to Login...")
time.sleep(1)

try:
    '''Getting Login Credentials'''
    username = input("Enter Remote User:")
    password = input("Enter Access Key/Password:")

    '''Attempting an SSH'''
    ssh.connect(host, port, username, password)

    '''Establishing and maintaining active SSH session'''
    execute_condition = 'True'
    while execute_condition == 'True':
        command = input('Enter Command to Execute:  ')
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)
        if command.upper() == 'SSH EXIT':
            execute_condition = 'False'

    '''Exit Statement'''
    print("SSH OUT: Successfully completed SSH Session.")

    '''Unexpected Errors Go Here'''
except Exception as e:
    print(f'Unable to SSH IN. Exception occured:{e}')
