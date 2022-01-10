# Mercenaries-Farm-Bot for Hearthstone
```diff
Bot is on a development stage but it already works to do some "Tasks" and run low level bounties
```
## Purpose
The purpose of this bot is to automatically pass the levels to level up your heros, win somes coins and do some campfire tasks 

It started as a fork of (and a collaboration to) a previous project but after being the only dev and going with a different point of view, I decided to make a new project.

(the purpose of the previous project was to autogroup heroes to level them up to 30)

There is a branch main to use and a branch for dev with new features but not well tested.


## News & contact 
More informations in [Wiki](https://github.com/Efemache/Mercenaries-Farm-Bot/wiki)

For contact, open an [issue](https://github.com/Efemache/Mercenaries-Farm-Bot/issues)

For news, follow us on Twitter : [@MercenariesFarm](https://twitter.com/MercenariesFarm)

To discuss with the community, go to discord [Mercenaries Farm server](https://discord.gg/ePghxaUBEK)

## Dev progress
|               |  1920x1080 (windowed mode) |
| :------------ | :-------------:| 
|1. transition to Travel point selection | ✓|
|2. transition to Level/Bounty selection | ✓|
|3. transition between encounters | ✓ |
|4. choosing a treasure after passing a level | ✓|
|5. putting heroes on the board | ✓|
|6. searching for suitable opponents | ✓|
|7. choosing abilities :  | ✓|
|    * for [supported Mercenaries](https://github.com/Efemache/Mercenaries-Farm-Bot/wiki/Mercenaries) | ✓|
|    * or the first one by default | ✓|
|8. attacking opponents | ✓|
|9. collecting rewards for reaching the last level|  ✓|
|10. repeat from 1 point | ✓|
 
## Supported game language & resolution
|               |     English    |
| :------------ | :-------------:| 
|   1920x1080   |        ✅      |

## PvE system work preview
Watch the video : [![Watch the video](https://user-images.githubusercontent.com/68296704/137970053-fe49c896-d237-49f1-8658-46d1477340d7.png)](https://www.youtube.com/watch?v=znt1P3KkrNg&t)

## When the bot is running
* don't move the Hearthstone window
* don't put another window in front of Hearthstone
* don't touch your mouse (except if you want to bypass the bot)
* don't resize the Hearthstone window

## Installation
### Windows
* Install [Python 3.9](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64-webinstall.exe) (see the video below) 
* Download and install AutoHotKey (AHK) : https://www.autohotkey.com/
* Download the project
* Open Settings.ini and set your settings
* Start Hearthstone
* Create a group of mercenaries named "Botwork" (and go back to main menu)
* Run HSbotRunner.bat


### Linux
* Install gir1.2-wnck-3.0 (sudo apt install gir1.2-wnck-3.0)
* Download the project
* Open Settings.ini and set your settings
* Start Hearthstone
* Create a group of mercenaries named "Botwork" (and go back to main menu)
* Run HSbotRunner.sh

### Demo
[![Watch the video](https://user-images.githubusercontent.com/68296704/138687982-0f6d971d-783d-4f35-a3a5-4f5d5a3e59af.png)](https://www.youtube.com/watch?v=nOZXCkrQ5fk)


