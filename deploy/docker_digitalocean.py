import subprocess
import re
import os
import time
import sh
import time
from docker_digitalocean_db import *
from docker_digitalocean_config import config

env_config = config['dev']

ssh_con_str = env_config['ssh_con_str']

print "NOTICE: this script has to be run as a user with access to SSH keys."
print "Deployment to remote server (" + ssh_con_str + ") started."

ssh = sh.ssh.bake('-oStrictHostKeyChecking=no', ssh_con_str)

print "Successfully connected to remote server."

kill_and_remove_all_containers(ssh, env_config['container_name'])

copy_db_src_to_remote_host(ssh_con_str, env_config['deploy_dir'])
build_db_image_in_remote_host(ssh, env_config['image_tag'], env_config['deploy_dir'])
run_db_container(ssh, env_config['image_tag'], env_config['container_name'])



