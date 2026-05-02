import tkinter as tk
import random
import time

# =============================================================================
# SARINA — Spin logic
# =============================================================================
# produce unpredictable results like a real slot machine.

symbols = ["🍒","⭐","💎"]

def spin_reels() -> list:

    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    return [reel1, reel2, reel3]


def check_result(results):

    if results[0] == results[1] == results[2]:
        return "JACKPOT! 🎉"

    elif results[0] == results[1] or results[1] == results[2] or results[0] == results[2]:
        return "Almost there buddy"

    else:
        return "Try Again 😢"


# =============================================================================
# LUCK — UI setup
# =============================================================================

root = tk.Tk()
root.title("PYCHARMERS888")
root.configure(bg="#8b0000")
root.attributes("-topmost", True)

# Title banner
label = tk.Label(
    root,
    text="🃁🂡🂱🃑PYC888🃁🂡🂱🃑",
    font=("Retro Signed", 100, "bold"),
    bg="#8b0000"
)
label.pack(pady=80)

# Balance display
balance_amount = 1000
balance = tk.Label(
    root,
    text=f"Balance: {balance_amount}",
    font=("Retro Signed", 20, "bold"),
    bg="#8b0000",
    fg="white"
)
balance.pack(pady=5)

# Reel display
reel_label = tk.Label(
    root,
    text="[ ? ]  [ ? ]  [ ? ]",
    font=("Arial", 36, "bold"),
    bg="#8b0000",
    fg="white"
)
reel_label.pack(pady=10)

# Outcome message
outcome_label = tk.Label(
    root,
    text="",
    font=("Retro Signed", 24, "bold"),
    bg="#8b0000",
    fg="#FFB81C"
)
outcome_label.pack(pady=5)

# Title color animation
colors = ["yellow", "yellow", "white", "white", "#FFB81C", "#FFB81C"]
index = 0

def cycle_color():
    global index
    label.config(fg=colors[index % len(colors)])
    index += 1
    label.after(300, cycle_color)

cycle_color()
# =============================================================================
# Reyna - Betting System
# =============================================================================
default_bet_amount = 100
bet_label = tk.Label(root,text="Set your bet:",font=("Retro Signed", 20, "bold"),bg="#8b0000",fg="white")
bet_label.pack(pady=5)
bet_entry = tk.Entry(root,font=("Retro Signed", 20, "bold"),justify="center")
bet_entry.pack(pady=5)
bet_entry.insert(0,str(default_bet_amount))
# =============================================================================
# WIN — Button logic
# =============================================================================

def spin_button():

    global balance_amount
    try:
        bet=int(bet_entry.get())
        if bet <=0:
            outcome_label.config(text="bet must be greater than 0",fg="red")
            return
    except ValueError:
        outcome_label.config(text="invalid bet",fg="red")
        return
    if balance_amount < bet:
        outcome_label.config(text="Not enough balance", fg="red")
        return

    # spinning animation
    for i in range(10):
        temp = [
            random.choice(symbols),
            random.choice(symbols),
            random.choice(symbols)
        ]

        reel_label.config(text=f"[ {temp[0]} ]  [ {temp[1]} ]  [ {temp[2]} ]")
        root.update()
        time.sleep(0.1)

    # deduct bet
    balance_amount -= bet
    balance.config(text=f"Balance: {balance_amount}")

    # real spin
    results = spin_reels()
    outcome = check_result(results)

    # add winnings if jackpot
    if outcome.startswith("JACKPOT"):
        balance_amount += bet * 10

    # show final results
    reel_label.config(text=f"[ {results[0]} ]  [ {results[1]} ]  [ {results[2]} ]")
    outcome_label.config(text=outcome)
    balance.config(text=f"Balance: {balance_amount}")


# Spin button
button = tk.Button(
    root,
    text="Spin",
    command=spin_button,
    font=("Party LET", 50, "bold")
)
button.pack(pady=10)

# =============================================================================
# Run the app
# =============================================================================

root.mainloop()#
