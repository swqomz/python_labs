
import tkinter as tk
import lab06 as lab

students = ["Anna", "Ivan", "Olha"]
count = 5

def create_report():
    report = ""

    for i in range(len(students)):
        name = students[i]
        grades = lab.generate_grades(count)
        average = lab.average_grade(grades)
        level = lab.get_level(average)

        report += f"{name}: {grades} -> {average:.2f} -> {level}\n"

    print(report)
    result_label.config(text=report)

root = tk.Tk()
root.title("оцінки")
root.geometry("500x300")

title_label = tk.Label(root,text="звіт",font=("Arial", 14))

title_label.pack(pady=10)
button = tk.Button(root,text="створити звіт",command=create_report)
button.pack(pady=10)

result_label = tk.Label(root,text="натисніть кнопку для звіту",font=("Arial", 11),justify="left")
result_label.pack(pady=10)

root.mainloop()
