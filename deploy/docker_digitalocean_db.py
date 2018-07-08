import os
from docker_digitalocean_common import *

def copy_db_src_to_remote_host(ssh_con_str, deploy_dir):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/../*"
	print "Copying web-db src (" + local_dir + ") to remote host."
	os.system("scp -r " + local_dir + " " + ssh_con_str + ":" + deploy_dir)
	print "Copying web-db src to remote host finished."

def build_db_image_in_remote_host(ssh, tag, build_dir):
	print "Building alexa-air-dev/web-db image in remote host."
	result = ssh("docker build -t " + tag + " " + build_dir)
	print "Building " + tag + " image in remote host result: "
	print result

def run_db_container(ssh, image_tag, name):
	print "Starting alexa-air-dev-web-db container in remote host."
	result = ssh("docker run --name " + name + " -d " + image_tag)
	print "Starting " + image_tag + " container in remote host result: "
	print result

