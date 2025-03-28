import time
import signal
import sys

# Replace with your custom lyrics (lines of the song)
lyrics = [
    """
        Well, you can tell by the way I use my walk
        I'm a woman's man no time to talk
        Music loud and women warm, I've been kicked around
        Since I was born
    """,
    """
        And now it's all right, it's okay
        And you may look the other way
        We can try to understand"
        The New York Times' effect on man"
    """,
    """
        Whether you're a brother or whether you're a mother
        You're stayin' alive, stayin' alive
        Feel the city breakin' and everybody shakin'
        And we're stayin' alive, stayin' alive
    """,
    """
        Ah, ha, ha, ha, stayin' alive, stayin' alive
        Ah, ha, ha, ha, stayin' alive
    """
]

interrupt_count = 0
max_interrupts = len(lyrics)

def handle_sigint(signum, frame):
    global interrupt_count
    if interrupt_count < max_interrupts:
        print(f"\n{lyrics[interrupt_count]}")
        interrupt_count += 1
    else:
        sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

while True:
    time.sleep(1)  # just idling; staying alive
