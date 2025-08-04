from psychopy import visual, core, event, sound
import random

# Window setup
win = visual.Window(fullscr=True, color='black')
text = visual.TextStim(win, text='', height=0.07, wrapWidth=1.5, color='white')
beep = sound.Sound('A', secs=0.5)  # Default beep sound

# Utility Functions
def show_message(msg, wait=True):
    text.text = msg
    text.draw()
    win.flip()
    if wait:
        event.waitKeys()

def show_digit(d, seconds):
    text.text = str(d)
    text.draw()
    win.flip()
    core.wait(seconds)

def visualize_digit(d):
    text.text = f"{d}\n\nNow, close your eyes and visualize the digit {d} in your mind for 10 seconds.\nA beep will indicate the end."
    text.draw()
    win.flip()
    core.wait(10)
    beep.play()
    core.wait(0.6)

# =======================
# 1. Welcome
# =======================
show_message("Welcome to the EEG Dataset Collection Experiment\n\nPlease click any key to begin.")
show_message("Don’t worry about anything. Just stay calm and relaxed.\n\nClick any key to continue.")

# =======================
# 2. Introduction
# =======================
show_message("Welcome to the study!\n\nIn this session, you will first stay still for a brief baseline measurement,\nthen learn about the task.\n\nClick any key to continue.")

# =======================
# 3. Meditation
# =======================
show_message("Start Meditation\n\nSit still, close your eyes if you’d like, and take deep breaths.\nAn audio clip will play for one minute.\n\nClick any key to begin.")
core.wait(60)  # Replace with actual audio if available
show_message("Meditation complete.\n\nClick any key to proceed.")

# =======================
# 4. Task 1 (Ordered 0-9)
# =======================
show_message("Task 1\n\nOn the next screen, you will alternate between imagining the digits 0 to 9.\nEach digit lasts 20 seconds (10s observe + 10s visualize).\n\nClick any key to start.")

for digit in range(10):
    show_message(f"Now, look at and observe the digit {digit} on the screen for 10 seconds.", wait=False)
    show_digit(digit, 10)
    visualize_digit(digit)
    show_message("Click any key to continue to next digit.")

# =======================
# 5. Second Meditation (Optional)
# =======================
show_message("Start Meditation Again\n\nTake a short break. Deep breaths.\nClick any key to begin.")
core.wait(60)
show_message("Click any key to proceed to Task 2.")

# =======================
# 6. Task 2 (Shuffled 0–9)
# =======================
show_message("Task 2\n\nNow, digits will appear in random order.\nEach will be observed and visualized.\n\nClick any key to start.")

digits = list(range(10))
random.shuffle(digits)

for digit in digits:
    show_message(f"Now, look at and observe the digit {digit} on the screen for 10 seconds.", wait=False)
    show_digit(digit, 10)
    visualize_digit(digit)
    show_message("Click any key to continue to next digit.")

# =======================
# 7. End of Experiment
# =======================
show_message("Thank you for participating in the study.\n\nYou have successfully completed all the tasks.\nYour responses have been recorded.\n\nPress any key to exit.")
win.close()
core.quit()

