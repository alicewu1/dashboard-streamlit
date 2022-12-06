open port 80

- Under **Networking**, Add inbound security rule
    - Under Service: Select **HTTP** > ADD


# To Connect to Azure VM
-       ssh alice@[External IP Address of VM]
- Enter Password


# Setup
-       sudo apt-get update
-       python3
-       pip3 install flask
-       sudo apt install python3-flask
-       sudo apt install python3-pip
-       pip3 install streamlit
- When Installing Streamlit, it doesn not modity bash file to include path of where streamlit is
-       streamlit
- Go to .bashrc file:
-       nano ~/.bashrc
- Add streamlit path below to the very last line, save, exit
-       export PATH="$HOME/.local/bin:$PATH"
- Ctrl + O
- Ctrl + Z
- Restart Terminal:
-       source ~/.bashrc
-       streamlit
- Jinja2 needs to be above version 3.0
-       pip3 install jinja2 --upgrade

# Open the correct ports
- Displays: [IP Address:8501] >> Error: port 8501 is not open (the default port for streamlit)
- Open port 8501 by Opening Networking Tab,
- Add inbound security rule to open 2 ports: 
    - Destination port ranges: 8501
    - Destination port ranges: 8502


# Clone your Repo
-       git clone [repo url]
-       ls -l 
-       cd to folder
-       ls -l
-       sudo steamlit app.py
-       nano app.py 
