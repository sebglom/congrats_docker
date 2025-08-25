#!/usr/bin/env python3
import os, sys, time, shutil

# Fallback to the ascii art file next to this script if no environment
# variable is set. The previous default pointed to ``/app/ascii.txt`` which
# fails when running the script outside of its container image.  By resolving
# the path relative to ``run.py`` we ensure the script works in any location.
DEFAULT_ART = os.path.join(os.path.dirname(__file__), "ascii.txt")
ART_PATH = os.environ.get("ART", DEFAULT_ART)
MSG = os.environ.get("MSG", "Congratulations Dr. Lennart Schürmann!")
FRAME_DELAY = float(os.environ.get("FRAME_DELAY", "0.04"))
HOLD = float(os.environ.get("HOLD", "0.4"))
EXIT_DELAY = float(os.environ.get("EXIT_DELAY", "1.2"))

with open(ART_PATH, "r", encoding="utf-8") as f:
    art_lines = [line.rstrip("\n") for line in f]

# Terminalgröße (Fallback 80x24)
cols, rows = shutil.get_terminal_size(fallback=(80, 24))

art_h = len(art_lines)
art_w = max((len(l) for l in art_lines), default=0)

# Horizontale Zentrierung
pad_x = max(0, (cols - art_w) // 2)
pad_msg = max(0, (cols - len(MSG)) // 2)

def clear_home():
    sys.stdout.write("\033[2J\033[H")

def render(offset_y, do_clear=True):
    if do_clear:
        clear_home()
    sys.stdout.write("\n" * max(0, offset_y))
    pad = " " * pad_x
    for line in art_lines:
        sys.stdout.write(pad + line + "\n")
    sys.stdout.flush()

def print_message(bold=True):
    start = "\033[1m" if bold else ""
    end = "\033[0m" if bold else ""
    sys.stdout.write("\n" + " " * pad_msg + f"{start}{MSG}{end}\n")
    sys.stdout.flush()

is_tty = sys.stdout.isatty() and os.environ.get("NO_ANIM", "") == ""

if not is_tty:
    # Ohne TTY: statischer, testsicherer Output
    center_y = max(0, (rows - art_h) // 2)
    render(center_y, do_clear=False)
    print_message(bold=False)
    sys.exit(0)

# Mit TTY: Animation von unten nach oben
start_y = max(0, rows - art_h - 1)
target_y = max(0, rows // 4 - art_h // 2)

# Cursor aus-/einblenden
sys.stdout.write("\033[?25l")
try:
    for y in range(start_y, target_y - 1, -1):
        render(y)
        time.sleep(FRAME_DELAY)

    render(target_y)
    time.sleep(HOLD)
    print_message(bold=True)
    time.sleep(EXIT_DELAY)
finally:
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
