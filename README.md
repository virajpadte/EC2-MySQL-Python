# EC2-MySQL-Python
My plan is to build a simple workflow to try and get a python code to work with a remote MySQL database hosted on AWS EC2 instance.

Pre-requisitives:
Make sure you have an EC2 instance up and running. 
You have allowed inbound traffic on port 3306

Step 1: Install MySQL on the EC2 instance:
This LAMP tutorial comes handy you can just go ahead and install mysql:
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html

Step 2: Clone the repository:
git clone https://github.com/virajpadte/EC2-MySQL-Python.git

Step 3: Install dependencies:
pip install -r requirements.txt

Step 4: Make changes in the connection string in both db_test_fetch.py and db_test_insert.py
"<type db server IP>","<type username>","<type password>","<type database name>"


