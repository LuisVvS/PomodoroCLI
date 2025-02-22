import time
from rich.progress import Progress

def Timer():
    sessions = int(input("Ho many sessions you are going to take?"))
    focus = int(input("What is your focus time?"))
    breaks = int(input("What is your break time?"))

    #The countdown function to run the time
    countdown(focus)
    breaker(breaks)


def countdown(f):
    respond = "nao"
    while respond == "nao":
        respond = input("You want to start the focusing timer?")

    if(respond == "sim"):
        with Progress() as progress:
            seconds = f * 60
            task = progress.add_task("Focusing....", total=seconds)
            for i in range(seconds):
                time.sleep(0.9)
                seconds-=1
                progress.update(task, advance=1)
            print("⏰ Time's up!") 


def breaker(breaker):
    respond = "nao"
    while respond == "nao":
        respond = input("Start Break?")


    if respond == "sim":
        seconds = breaker * 60
        if(respond == "sim"):
            with Progress() as progress:
                task = progress.add_task("Resting....", total=seconds)
                for i in range(seconds):
                    time.sleep(0.9)
                    seconds-=1
                    progress.update(task, advance=1) 
                print("The break if over") 


    

def sessions_loop(s):
    ...
