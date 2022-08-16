![alt text](https://github.com/1qgl/GUI-AI-Crowd-Counter/blob/main/demo%20images/3.PNG?raw=true)

# GUI AI Crowd Size Estimator
A python GUI tool I made for fun that can instantly estimate how many people are in an image of a crowd. This tool uses one of the models and sets of weights developed by Pongpisit Thanasutives, Ken-ichi Fukui, Masayuki Numao, and Boonserm Kijsirikul in their paper "Encoder-Decoder Based Convolutional Neural Networks with Multi-Scale-Aware Modules for Crowd Counting". In my informal testing I've found that their model is pretty impressively accurate (and actual rigorous testing can be found in their paper).

Here is a link to their github repo: https://github.com/Pongpisit-Thanasutives/Variations-of-SFANet-for-Crowd-Counting

And a link to their paper on arxiv: https://arxiv.org/abs/2003.05586

## Install and Launch
You should clone this repo and probably should create a python virtual environment for the dependencies.

Then install the dependencies like so:
```bash
$ pip install -r requirements.txt
```

Finally, launch the GUI tool by running the python script from inside the directory:
```bash
$ python "GUI AI Crowd Counter.py"
```

## Use
This is how the tool will look upon launching:

![alt text](https://github.com/1qgl/GUI-AI-Crowd-Counter/blob/main/demo%20images/1.PNG?raw=true)

Simply click the "Choose File" button to pick an image of a crowd on your device, an image preview will load:

![alt text](https://github.com/1qgl/GUI-AI-Crowd-Counter/blob/main/demo%20images/2.PNG?raw=true)

Then click the "Estimate Crowd Size Button" and the ML model will return an estimate:

![alt text](https://github.com/1qgl/GUI-AI-Crowd-Counter/blob/main/demo%20images/3.PNG?raw=true)

The first time an estimate is made will take longer than normal and will require an internet connection. This is because pytorch has to install the pretrained VGG model which the SFANet model uses. After this, the tool can be used offline and will make estimates quickly.
