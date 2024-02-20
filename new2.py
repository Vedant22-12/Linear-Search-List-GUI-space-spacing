import tkinter as tk
import time

def linear_search():
    search_value = int(entry.get())
    found_elements = []

    for index, num in enumerate(numbers):
        canvas.itemconfig(rectangles[index], fill="blue")  # Highlight current element being checked
        canvas.update()
        time.sleep(0.3)

        if num == search_value:
            canvas.itemconfig(rectangles[index], fill="green")  # Change color to green if found
            found_elements.append(f"{num} (Index {index})")
            found_label.config(text=f"Found: {', '.join(found_elements)}", fg="green")
            break

        canvas.itemconfig(rectangles[index], fill="red")  # Change color to red if not found
        canvas.update()
        time.sleep(0.3)

    else:
        result_label.config(text="Value not found", fg="red")
        return

    result_label.config(text="Value found", fg="green")

def process_input():
    numbers_str = input_entry.get()
    numbers.clear()

    for num in numbers_str.split():
        numbers.append(int(num))

    redraw_canvas()

def insert_number():
    new_num = int(insert_entry.get())
    index = int(insert_index_entry.get())  # Get the index from the entry

    if 0 <= index <= len(numbers):
        numbers.insert(index, new_num)
        redraw_canvas()
        result_label.config(text=f"Inserted {new_num} at Index {index}", fg="blue")

def delete_number():
    index = int(delete_index_entry.get())  # Get the index from the entry

    if 0 <= index < len(numbers):
        deleted_num = numbers.pop(index)
        redraw_canvas()
        result_label.config(text=f"Deleted {deleted_num} at Index {index}", fg="red")

def update_number():
    new_num = int(update_entry.get())
    index = int(update_index_entry.get())  # Get the index from the entry

    if 0 <= index < len(numbers):
        old_num = numbers[index]
        numbers[index] = new_num
        redraw_canvas()
        result_label.config(text=f"Updated {old_num} to {new_num} at Index {index}", fg="green")

def redraw_canvas():
    canvas.delete("all")  # Clear the canvas
    rectangles.clear()    # Clear the list of rectangles

    for index, num in enumerate(numbers):
        rect = canvas.create_rectangle(10 + index * 40, 100, 50 + index * 40, 150, fill="white")
        text = canvas.create_text(30 + index * 40, 125, text=str(num))
        rectangles.append(rect)

root = tk.Tk()
root.title("Linear Search Algorithm")
root.configure(bg="#E1BEE7")  # Light Purple Color

# Heading with background color
heading_label = tk.Label(root, text="Linear Search Algorithm", font=("Helvetica", 35, "bold","italic"), bg="#E1BEE7", padx=10, pady=10)
heading_label.pack(fill="x")

canvas = tk.Canvas(root, width=600, height=300, bg="light blue")
canvas.pack()

rectangles = []  # To store rectangle elements
arrows = []      # To store arrow elements

input_label = tk.Label(root, text="Enter numbers (space-separated):", bg="#E1BEE7")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

process_button = tk.Button(root, text="Process Input", command=process_input)
process_button.pack()

insert_frame = tk.Frame(root, bg="#E1BEE7")
insert_frame.pack()

insert_label = tk.Label(insert_frame, text="Insert a number:", bg="#E1BEE7")
insert_label.pack(side="left")

insert_entry = tk.Entry(insert_frame)
insert_entry.pack(side="left")

insert_index_label = tk.Label(insert_frame, text="at Index:", bg="#E1BEE7")
insert_index_label.pack(side="left")

insert_index_entry = tk.Entry(insert_frame)
insert_index_entry.pack(side="left")

insert_button = tk.Button(insert_frame, text="Insert", command=insert_number)
insert_button.pack(side="left")

delete_frame = tk.Frame(root, bg="#E1BEE7")
delete_frame.pack()

delete_label = tk.Label(delete_frame, text="Delete at Index:", bg="#E1BEE7")
delete_label.pack(side="left")

delete_index_entry = tk.Entry(delete_frame)
delete_index_entry.pack(side="left")

delete_button = tk.Button(delete_frame, text="Delete", command=delete_number)
delete_button.pack(side="left")

update_frame = tk.Frame(root, bg="#E1BEE7")
update_frame.pack()

update_label = tk.Label(update_frame, text="Update at Index:", bg="#E1BEE7")
update_label.pack(side="left")

update_index_entry = tk.Entry(update_frame)
update_index_entry.pack(side="left")

update_entry = tk.Entry(update_frame)
update_entry.pack(side="left")

update_button = tk.Button(update_frame, text="Update", command=update_number)
update_button.pack(side="left")

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Search", command=linear_search)
search_button.pack()

found_label = tk.Label(root, text="Found:", font=("Helvetica", 25), bg="#E1BEE7")
found_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 25), bg="#E1BEE7")
result_label.pack(side="bottom")

numbers = []

root.mainloop()
