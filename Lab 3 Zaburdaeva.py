import tkinter as tk
import random
import string
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("май литл пони.mp3")
pygame.mixer.music.play(-1)

def generate_key():
    key_parts = []
    for _ in range(3):
        block = []
        letters = random.choices(string.ascii_uppercase, k=3)
        digits = random.choices(string.digits, k=2)
        block.extend(letters + digits)
        random.shuffle(block)
        key_parts.append(''.join(block))
    generated_key = '-'.join(key_parts)
    key_entry.config(text=generated_key)
    
    animate_key_frame()

def animate_key_frame():
    current_color = key_frame.cget("bg")
    new_color = "lightgreen" if current_color == "pink" else "pink"
    key_frame.config(bg=new_color)
    
    root.after(555, animate_key_frame)

#анимация начинает работать после нажатия кнопки "Сгенерировать ключ"

root = tk.Tk()
root.title("Key Generator")

bg_image = tk.PhotoImage(file="картинка.png")

bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

image_width = bg_image.width()
image_height = bg_image.height()
root.geometry(f"{image_width}x{image_height}")

key_frame = tk.Frame(root, bg="pink", padx=8, pady=0.3)
key_frame.place(relx=0.5, rely=0.83, anchor="center")

key_entry = tk.Label(key_frame, font=("Helvetica", 17), justify='center', width=20, bg="white", fg="indigo", relief="solid", padx=5, pady=5)
key_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="pink", padx=5, pady=0.2)
button_frame.place(relx=0.5, rely=0.95, anchor="center")

generate_button = tk.Button(button_frame, text="Сгенерировать ключ", command=generate_key, font=("Helvetica", 12), bg="skyblue", relief="flat", padx=10, pady=5)
generate_button.pack(pady=5)

root.mainloop()
