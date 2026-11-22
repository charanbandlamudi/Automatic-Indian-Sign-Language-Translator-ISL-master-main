import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid


# Custom Class for GIF Handling
class ImageLabel(tk.Label):
    """A label that displays images, and plays them if they are gifs."""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 1

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


# Mesa Components for Simulation
class SignLanguageAgent(Agent):
    """An agent representing a person in the simulation."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.state = "idle"

    def step(self):
        if self.state == "idle":
            self.state = "communicating"
            print(f"Agent {self.unique_id}: Started communication.")
        elif self.state == "communicating":
            print(f"Agent {self.unique_id}: Communicating using sign language.")


class SignLanguageModel(Model):
    """The Mesa model managing agents and their interactions."""
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        for i in range(self.num_agents):
            agent = SignLanguageAgent(i, self)
            self.schedule.add(agent)
            x = self.random.randint(0, width - 1)
            y = self.random.randint(0, height - 1)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        print(f"\nSimulation Step {self.schedule.steps + 1}")
        self.schedule.step()


# Simulation and Voice-to-ISL Integration
def run_mesa_simulation():
    print("Starting Mesa Simulation...")
    model = SignLanguageModel(10, 10, 10)  # 10 agents on a 10x10 grid
    for i in range(5):  # Run for 5 steps
        model.step()
    print("\nSimulation complete. Starting Voice-to-ISL functionality...\n")


def func():
    """Voice-to-ISL conversion functionality."""
    print("Voice to ISL functionality here")


def func_with_mesa():
    """Run Mesa simulation followed by Voice-to-ISL."""
    run_mesa_simulation()
    func()


# Main Program
def main():
    while True:
        image = "signlang.png"  # Ensure this image file exists
        msg = "HEARING IMPAIRMENT ASSISTANT"
        choices = ["Run Voice + Simulation", "Quit"]
        reply = buttonbox(msg, image=image, choices=choices)

        if reply == "Run Voice + Simulation":
            func_with_mesa()
        elif reply == "Quit":
            print("Exiting program. Goodbye!")
            break


# Entry Point
if __name__ == "__main__":
    main()
