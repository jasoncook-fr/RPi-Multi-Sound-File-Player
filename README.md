## Play multiple channels of sounds with touch sensor MPR121
Python3 is used to execute the included code _MPR121MultiSoundPlay.py_ <br/>
<br/>
Sound files are to be prepared as .wav 16-bit. Up to 12 channels are possible with the MPR121 capacitive sensor controller. The files must be placed in the _sounds_ folder before launching the python code.<br/>
Within the _sounds_ folder is a bonus code for normalizing volume of all wav files found within the folder. Launch this code simply with python. It will convert all sound files and place them in the folder titled _modified_ . <br/>
<br/>
Be sure to activate the I2C port for communication with the mpr121, option found in _interface options_ of raspi-config:

```bash
sudo raspi-config
```

Dependencies are as follows:

```bash
sudo apt-get update
sudo apt-get install python3-pygame python3-pip
sudo pip3 install adafruit-circuitpython-mpr121
```
**This project was produced at the school of fine arts and media of Caen/Cherbourg (France). The sound clips included are the work of Rajat Mondal**
