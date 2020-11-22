# Automate Fullstack Academy Office Hours

### Chrome Driver
https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip

### Windows Setup 

```powershell
  
Invoke-WebRequest -Uri "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip" -Outfile "~/Documents/chromedriver.zip"

Expand-Archive -LiteralPath "~/Documents/chromedriver.zip" -DestinationPath "~/Documents" -Force

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

### Modify values.json file for Office Hours Settings

```
{
	"description": "Office hours with Alexis",
	"location": "Slack me before office hours",
	"dates": [
		"11/30/2020",
		"12/2/2020",
		"12/2/2020"
	],
	"time": {
		"hour": 6,
		"minute": 00,
		"am_pm": "PM"
	},
	"num_of_slots": 5,
	"slot_duration": 20,
	"booking_method": "any available",
	"employees_only": false,
	"restrict_to_cohorts": [
		"2010-FCB-NY-CYB-PT"
	]
}

```

### Run
```
python create_office_hours.py -h
```
