# Automate Fullstack Academy Office Hours


### Windows Setup 

```powershell
  
Invoke-WebRequest -Uri "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip" -Outfile "~/Documents/chromedriver.zip"

Expand-Archive -LiteralPath "~/Documents/chromedriver.zip" -DestinationPath "~/Documents"

cd ~/Documents/ 

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/binexisHATT/Python/master/FullstackWorkFlowAutomated/create_office_hours.py"

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/binexisHATT/Python/master/FullstackWorkFlowAutomated/values.json"

# pip should be part of path 
pip install selenium colored

```

### Linux Setup

```bash

wget "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip" -O ~/Documents/chromedriver.zip

unzip ~/Documents/chromedriver.zip

cd ~/Documents && wget "https://raw.githubusercontent.com/binexisHATT/Python/master/FullstackWorkFlowAutomated/create_office_hours.py"

wget "https://raw.githubusercontent.com/binexisHATT/Python/master/FullstackWorkFlowAutomated/values.json"

pip install selenium colored

```

### Run
```
python create_office_hours.py -h
```
