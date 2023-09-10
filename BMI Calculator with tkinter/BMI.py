import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100  # Convert height to meters
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    bmi_category = ""

    if bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    result_label.config(text=f'BMI: {bmi:.2f}\nCategory: {bmi_category}')

# Create a Tkinter window
window = tk.Tk()
window.title("BMI Calculator")

# Create labels and entry fields
height_label = tk.Label(window, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack()

window.mainloop()
