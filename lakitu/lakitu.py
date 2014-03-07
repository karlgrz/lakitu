from pprint import pprint
from boto import ec2
import sys

class Lakitu(object):

	def __init__(self, access_key, secret_access_key, windows_key, keys_path):
		self.access_key = access_key
		self.secret_access_key = secret_access_key
		self.windows_key = windows_key
		self.keys_path = keys_path

	def display_instances(self):
		ec2conn = ec2.connection.EC2Connection(self.access_key, self.secret_access_key)
		reservations = ec2conn.get_all_instances()
		instances = [i for r in reservations for i in r.instances]
		for i in instances:
			if (i.state == 'running'):
				grouplist = ""
				for group in i.groups:
					grouplist = grouplist + "|" + group.name

				if (i.platform == u"windows"):
					print "WINDOWS {0} /usr/bin/gnome-terminal -x /usr/bin/rdesktop -g 1440x900 -u Administrator -p \"{1}\" -x l {2}  -K -r clipboard:PRIMARYCLIPBOARD".format(grouplist, self.windows_key, i.public_dns_name)
				else:
					print "        {0} /usr/bin/gnome-terminal -x /usr/bin/ssh -i \"{1}{2}.pem\" ubuntu@{3}".format(grouplist, self.keys_path, i.key_name, i.public_dns_name)

def main(argv):
	access_key = argv[1]
	secret_access_key = argv[2]
	windows_key = argv[3]
	keys_path = argv[4]
	lakitu = Lakitu(access_key, secret_access_key, windows_key, keys_path)
	print lakitu.display_instances()

if __name__ == "__main__":
	main(sys.argv)
