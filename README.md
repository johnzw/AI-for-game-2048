# RL-AI for game 2048
It uses reinforcement learning to play game 2048

### Disclaimer
First all, this project is still in progress. And due to the limit of states, which I am getting trouble on, it can only play 2*2 game following the rule of game 2048. So I may have lied in the title, saying it's the AI for game 2048. Well, it is true in some way, that it is a simplified game 2048 after all - -.

### customize your own AI game engine
well, fancy as the title may sound, the process is easy as hell.
* use LearningProc.py to generate a new array.data file, that is:

`python LearningProc.py`

that's it, that's the only step. 
Right now it has its own data.array file, a [pickle](https://docs.python.org/2/library/pickle.html)-dumped file that descibes the action-values of all the possible states in this game, which I may have run under the condition of:
(I can't remember for sure)
* alpha:0.7
* Learning times:500000
* greedy level:0.97
* Reward Mode:False, the mode in which only winning state gives positive reward, which is the game score, with other state-reward set to be 0

You are encouraged to use other settings. you may have to run `python LearningProc.py --help` to see further details about all the possible parameters.
**warning**: you may need a little patience becuase running this file might take a while, especilly when you set the Learning Times to large, say, a million.

###About 2048.py and anothergame.py
you can simply run both files without any further arguments: `python 2048.py` or `python anothergame.py`. And in fact they don't use any more arguments. 
you may not need any other user manual when entering into game, since as far as I see it the game per se is quite self-explanatory. but here is what you may have questions about:
* in 2048.py, once upon the game, AI engine takes control and make a move automatically *every second*. Basically you lose control of the game and there is nothing you can do but wait until one round of game ends. And then you can restart or quit the game.
* in anothergame.py, users play the game themselves and see the hint provided by AI engine as they stuck on the game.

the AI engine are based on array.data file in both files. Both games are powered by python package [curses](https://docs.python.org/3.3/howto/curses.html#user-input). And most of the code of the game part are referenced in [here](https://www.shiyanlou.com/courses/368)(it's online course website, you may have to sign up to check out more)


####All in all, it is still in progress

###Reference
https://www.shiyanlou.com/courses/368