# KattiBot

Used to send daily random cat pictures from [thiscatdoesnotexist.com](https://thiscatdoesnotexist.com/).

### Commands
- /katti  - Random cat pic
- /start  - Start message
- /github - Link to this repository

---


### Run instructions
With dockers:

`$ docker build -t kattibot .` 

`$ docker run -d kattibot`

Without dockers:
1. Have python 3.7 or higher installed
1. Install everything listed in requirements.txt
2. Run `$ python3 kattibot.py`
