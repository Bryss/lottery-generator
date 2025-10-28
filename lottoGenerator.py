#!/usr/bin/env python3
# Lotto Number Generator
# Python 3.8+ recommended,
# Python 3.6 or lower is not supported due to f-strings.
# 
# Original script by Jan Brekke 
# Rewritten by Bryss
#
# Not affiliated with Norsk Tipping.
# No winnings guaranteed.
# Gamble responsibly
# https://hjelpelinjen.no/

from os import system, name
from sys import stdout, stdin
from random import sample
from shutil import get_terminal_size
from termios import tcgetattr, tcsetattr, TCSADRAIN
from tty import setraw

# ANSI colors for pretty output
CYAN  = "\033[96m"
WHITE = "\033[97m"
DIM   = "\033[2m"
RESET = "\033[0m"

# OS agnostic way to clear the terminal
def clear():
    system("cls" if name == "nt" else "clear")

# Get width of terminal 
def width():
    return get_terminal_size().columns

# Center output and allign to left for nice looking ouput
def center_block(lines):
    col = width()
    block_width = max(len(line) for line in lines)
    pad = (col - block_width) // 2
    for line in lines:
        print(" " * pad + line)

# Replace "press ENTER to continue" with any key
def any_key(msg="Press any key to continue"):
    stdout.write(DIM + msg + RESET)
    stdout.flush()
    if name == "nt":
        import msvcrt
        msvcrt.getch()
    else:
        fd = stdin.fileno()
        old = tcgetattr(fd)
        try:
            setraw(fd)
            stdin.read(1)
        finally:
            tcsetattr(fd, TCSADRAIN, old)
    print()

# Same generator used for all lotteries, shortens the script
def generate(p_start, p_end, p_count, s_start, s_end, s_count):
    prim = sorted(sample(range(p_start, p_end + 1), p_count))
    sec = sorted(sample(range(s_start, s_end + 1), s_count)) if s_count else []
    return prim, sec

def get_line_count():
    try:
        n = int(input("How many number lines do you want (1–10)? "))
        if n <= 0:
            print("You must choose at least 1 line."); any_key(); return None
        if n > 10:
            print("Maximum allowed is 10 lines."); any_key(); return None
        return n
    except ValueError:
        print("Please enter a valid number."); any_key(); return None

# Prettier printout for the generated numbers
def show_numbers(title, rows, prim_label="Primary", sec_label="Secondary"):
    col = width()
    print("\n" + f"{CYAN}{title}{RESET}".center(col) + "\n")
    print(" " * ((col // 2) - 20) + f"{prim_label:<25}| {sec_label}")
    print(" " * ((col // 2) - 20) + "-" * 38)
    for prim, sec in rows:
        ptxt = " ".join(f"{x:2}" for x in prim)
        stxt = " ".join(f"{x:2}" for x in sec)
        print(" " * ((col // 2) - 20) + f"{ptxt:<25}| {stxt}")
    print()


def eurojackpot():
    clear(); center_block([CYAN+"Eurojackpot Number Generator"+RESET,""])
    n = get_line_count();  clear()
    if not n: return
    lines = [generate(1,50,5,1,12,2) for _ in range(n)]
    show_numbers("Eurojackpot", lines, "Primary", "Star"); any_key()

def vikinglotto():
    clear(); center_block([CYAN+"Vikinglotto Number Generator"+RESET,""])
    n = get_line_count();  clear()
    if not n: return
    lines = [generate(1,48,6,1,5,1) for _ in range(n)]
    show_numbers("Vikinglotto", lines, "Primary", "Viking"); any_key()

def lotto():
    clear(); center_block([CYAN+"Lotto Number Generator"+RESET,""])
    n = get_line_count();  clear()
    if not n: return
    rows = [(generate(1,34,7,0,0,0)[0], []) for _ in range(n)]
    print("\n" + (CYAN+"Lotto"+RESET).center(width()) + "\n")
    for p,_ in rows:
        print(" " * ((width()//2)-10) + " ".join(f"{x:2}" for x in p))
    print(); any_key()

def keno():
    clear(); center_block([CYAN+"Keno Number Generator"+RESET,""])
    n = get_line_count();  clear()
    if not n: return
    rows = [(generate(1,70,10,0,0,0)[0], []) for _ in range(n)]
    print("\n" + (CYAN+"Keno"+RESET).center(width()) + "\n")
    for p,_ in rows:
        print(" " * ((width()//2)-12) + " ".join(f"{x:2}" for x in p))
    print(); any_key()

def startup():
    clear()
    info = [
        CYAN+"Lotto Number Generator"+RESET,"",
        "Generates random numbers for Lotto, Vikinglotto, Eurojackpot, and Keno.","",
        "Not related to Norsk Tipping. No winnings guaranteed.","",
        "Gamble responsibly.","",
        DIM+"Help: https://hjelpelinjen.no/"+RESET,"",
        "Original by Jan Brekke   |  https://www.digitalbrekke.com",
        "Improved by Bryss        |  https://bryss.pro","",
    ]
    center_block(info); any_key()

def menu():
    actions = {"1": lotto, "2": vikinglotto, "3": eurojackpot, "4": keno}
    while True:
        clear()
        block = [
            CYAN+"Main Menu"+RESET,"",
            "Choose which lottery system to generate numbers for:","",
            "1) Lotto","2) Vikinglotto","3) Eurojackpot","4) Keno","",
            "9) Exit","",
            DIM+"No affiliation with Norsk Tipping. Gamble responsibly."+RESET,"",
        ]
        center_block(block)
        c = input("Choice: ").strip()
        if c == "9": clear(); center_block(["Goodbye!",""]); break
        fn = actions.get(c)
        if fn: fn()
        else: print("Invalid input."); any_key()

if __name__ == "__main__":
    startup(); menu()
