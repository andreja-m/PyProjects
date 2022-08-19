import paramiko

# We create a function called ssh_command, which makes a connection
# to an SSH server and runs a single command
def ssh_command(ip, port, user, passwd, cmd):
	client = paramiko.SSHClient()

	# we set the policy to accept the SSH key 
	# for the SSH server we’re connecting to	
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip,port=port, username=user, password=passwd)

	# Assuming the connection is made, we run the command
	_, stdout, stderr = client.exec_command(cmd)
	output = stdout.rteadlines() + stderr.readlines()
	if output:
		print('---Output---')
		for line in output:
			print(line.strip())

if __name__ == '__main__':
	import getpass
	# user = getpass.getuser()
	user = input('Username: ')
	password = getpass.getpass()

	ip = input('Enter server IP: ') # or 192.168.0.1
	port = input('enter port or <CR>: ') # or 2222
	cmd = input('Enter command or <CR>: ') # or 'id'
	ssh_command(ip, port, user, password, cmd)