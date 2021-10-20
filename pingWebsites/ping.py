import subprocess

def ping(servers):
	cmd = "ping"
	outputlist = []
	for server in servers:
		temp = subprocess.Popen([cmd, '-c 1', server], stdout = subprocess.PIPE)
		output = str(temp.communicate())
		outputlist.append(output)
	return outputlist

if __name__ == '__main__':
	servers = list(open('servers.txt'))
	for i in range(len(servers)):
		servers[i] = servers[i].strip('\n')
	outputlist = ping(servers)
#	print(outputlist)

	

