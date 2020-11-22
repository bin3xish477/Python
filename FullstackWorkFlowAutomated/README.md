# Automate Fullstack Academy Office Hours


### Windows Setup 

```powershell
  
Invoke-WebRequest -Uri "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip" -Outfile "~/Documents/chromedriver.zip"

Expand-Archive -LiteralPath "~/Documents/chromedriver.zip" -DestinationPath "~/Documents"


```

### Linux Setup

```bash

wget "https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_win32.zip" -O ~/Documents/chromedriver.zip

unzip ~/Documents/chromedriver.zip

git clone 

```
