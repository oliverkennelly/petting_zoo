# import the python datetime module to help us create a timestamp
from datetime import date
from petting import Llama, Cow, Pig, Sheep, Rabbit
from pond import Frog, Salamander, Snail, Snake, Turtle
from tank import Clam, Crab, Fish, Jellyfish, Shrimp

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )

print(miss_fuzz.feed())