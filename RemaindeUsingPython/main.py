# instagram: @code_with_sam127
import datetime
import tkinter as tk

print(f"Current time is: {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
def create_window(user_input_sentence):
    window = tk.Tk()
    window.title("Remainder pop up!")
    window.geometry("700x300+370+250")
    sentence = user_input_sentence
    label = tk.Label(window, text=sentence, font=("Arial", 20, "bold"))
    label.pack(fill=tk.BOTH, expand=True)
    window.mainloop()
print("Enter details to set remainder (hour and time)")
rem_hour = int(input("Enter your remainder (hour): "))
rem_minute = int(input("Enter your remainder (minute): "))
rem_text = str(input("Enter a text to remaind you: "))
print("Soon we will remind you for your work!")
while True:
    current_time = datetime.datetime.now()
    if current_time.hour == rem_hour and current_time.minute == rem_minute:
        create_window(rem_text)
        break