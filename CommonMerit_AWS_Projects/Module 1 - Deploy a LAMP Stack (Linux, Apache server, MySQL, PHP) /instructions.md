1. Overview:

	We're going to launch an EC2 instance that will include the following for a LAMP stack:

	- Apache web server
	- MariaDB relational database
	- PHP running on it.

	Linux, Apache, MariaDB, PHP

2. Business Case:

	Many customers who come to Common Merit have said that they would like to be able to place orders online.  I need to create a functioning website for Common Merit.

   
3. Deploy LAMP Stack
    
	- Create a backup of script1.sh and script2.sh
	- Analyze the contents of the script.
	- Run aws_script1.sh

			Issue #1

			The terminal output states An error occurred (InvalidAMIID.NotFound) when calling the RunInstances operation: The image id '[ami-...]' does not exist. Alternatively, you might see the message An error occurred (InvalidSubnetID.NotFound) when calling the RunInstances operation: The subnet ID 'subnet-....' does not exist. Both errors have the same root cause in the script configuration.
			Tips to help you resolve the issue #1:
				• Locate the line in the bash script that led to this error.
				• What AWS CLI command could be run to verify that the resource that could not be found does exist? You could also use the EC2 console to search for and confirm the existence of the resource that the script could not find.
				• Does the same AMI ID or subnet exist in every AWS Region? After you think you have found the issue and have adjusted the script accordingly, run it again (always reply with Y when you are prompted to delete any existing security groups or instances that were created the last time the script ran). Did the error get resolved?

			Issue #2

			The call to run-instances succeeds, and a public IP address is assigned to the new instance. However, when you try to use SSH to connect to the instance with the key pair file, you cannot connect (Permission denied error).
			Tips to help you resolve the issue #2:
				• It is an Amazon Linux 2 instance. The default user name is ec2-user.
				• Are the permissions on the key pair file set correctly (e.g., chmod 400)? What key pair file are you using? Is that the key pair file that the instance expects you to connect with?
				• Remember to use the AWS CLI Command Reference as an important source of information.
				• After you think you have found the issue and have adjusted the script accordingly, run it again.
					○ Are you able to connect to the instance by using SSH? Make the SSH attempt from your laptop, where you have the key pair already downloaded. Remember that it takes up to 5 minutes for the instance to fully boot.
					○ You should be able to connect by using SSH. Leave this SSH connection open.

			Issue #3

				The instance is created and you can establish an SSH connection to it successfully, but you cannot load the test webpage.
				Tips to help you resolve the issue #3:
					• The web server runs on TCP port 80.
					• If you use SSH to connect to the instance, can you verify that the web server service is running? The web server service name is httpd.
					29. While you are connected to the instance via SSH, run this command to install nmap, which is a port scanning tool:

				sudo yum install -y nmap		

				30. Next, run this command (where <public-ip> is the actual public IP address of your LAMP instance):

				nmap -Pn <public-ip>
				
				○ The results that are returned by this command show which ports are accessible. Do the results match what you expected?

    - Try connecting to the web page in a browser, http://<public-ip>
    - SSH to the instance and run the following to check your logs:
		sudo tail -f /var/log/cloud-init-output.log
	- Check for all the services in your LAMP stack.
	- Try placing an order

From <https://labs.vocareum.com/web/1543799/91853.0/ASNLIB/public/docs/lang/en/README.md> 
