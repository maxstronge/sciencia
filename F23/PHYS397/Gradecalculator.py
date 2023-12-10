import tkinter as tk
from tkinter import messagebox

class GradeCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Grade Calculator")

        self.components = []
        self.default_rows = 5

        # Adding labels for clarity
        tk.Label(root, text="Course Component Title").grid(row=1, column=0)
        tk.Label(root, text="Grade (%)").grid(row=1, column=1)
        tk.Label(root, text="Weight (%)").grid(row=1, column=2)

        self.add_course_component_button = tk.Button(root, text="Add Course Component", command=self.add_course_component)
        self.add_course_component_button.grid(row=0, column=0, columnspan=2)

        self.calculate_button = tk.Button(root, text="Calculate Grade Possibilities", command=self.calculate_grades)
        self.calculate_button.grid(row=0, column=2, columnspan=2)

        # Initialize the reset button
        self.reset_button = tk.Button(root, text="Calculate grades for another course", command=self.reset_calculator)
        self.reset_button.grid(row=self.default_rows + 3, column=0, columnspan=4)
        self.reset_button.grid_remove()  # Hide the reset button initially

        # Initialize the final exam row
        self.add_final_exam_row()

        for _ in range(self.default_rows):
            self.add_course_component()



    def add_course_component(self):
        row = len(self.components) + 2
        title_entry = tk.Entry(self.root)
        grade_entry = tk.Entry(self.root)
        weight_entry = tk.Entry(self.root)
        remove_button = tk.Button(self.root, text="Remove", command=lambda: self.remove_course_component(row))

        title_entry.grid(row=row, column=0)
        grade_entry.grid(row=row, column=1)
        weight_entry.grid(row=row, column=2)
        remove_button.grid(row=row, column=3)

        self.components.append((title_entry, grade_entry, weight_entry, remove_button))

            
        # Update the grid row of the final exam components
        final_exam_row = len(self.components) + 2
        self.final_exam_weight_entry.grid(row=final_exam_row, column=2)
        tk.Label(self.root, text="Final Exam").grid(row=final_exam_row, column=0)
        tk.Label(self.root, text="N/A").grid(row=final_exam_row, column=1)

         # Update the grid row of the reset button if it's visible
        if self.reset_button.winfo_ismapped():
            self.reset_button.grid(row=final_exam_row + 1, column=0, columnspan=4)


    def remove_course_component(self, row):
        for widget in self.components[row-2]:
            widget.destroy()
        del self.components[row-2]

        for i in range(row-2, len(self.components)):
            for widget in self.components[i]:
                widget.grid_configure(row=i+2)

    def add_final_exam_row(self):
        self.final_exam_weight_entry = tk.Entry(self.root)
        self.final_exam_weight_entry.grid(row=self.default_rows + 2, column=2)
        tk.Label(self.root, text="Final Exam").grid(row=self.default_rows + 2, column=0)
        tk.Label(self.root, text="N/A").grid(row=self.default_rows + 2, column=1)

    def calculate_grades(self):
        total_weight = 0
        current_score = 0
        for title, grade, weight, _ in self.components:
            if grade.get() and weight.get():
                try:
                    g = float(grade.get())
                    w = float(weight.get())
                    total_weight += w
                    current_score += g * w
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers for grades and weights.")
                    return

        if total_weight > 100:
            messagebox.showerror("Error", "Total weight cannot exceed 100%.")
            return

        final_exam_weight = float(self.final_exam_weight_entry.get()) if self.final_exam_weight_entry.get() else 0
        if total_weight + final_exam_weight != 100:
            messagebox.showerror("Error", f"The total weight (including the final exam) must sum up to 100%. Current total: {total_weight + final_exam_weight}%")
            return

        results = []
        for final_exam_score in [0, 25, 50, 75, 100]:
            final_grade = current_score + final_exam_score * final_exam_weight
            results.append((final_exam_score, final_grade / 100))

        pass_score = max((60 * 100 - current_score) / final_exam_weight, 0) if final_exam_weight > 0 else "N/A"
        a_score = max((85 * 100 - current_score) / final_exam_weight, 0) if final_exam_weight > 0 else "N/A"

        result_text = "Grade Possibilities:\n"
        for score, grade in results:
            result_text += f"Final Exam {score}%: Total Grade {grade:.2f}%\n"
        result_text += f"Score needed to Pass (Prerequisite) (60%): {pass_score}\n"
        result_text += f"Score needed for an A (85%): {a_score}\n"

        messagebox.showinfo("Results", result_text)
        self.reset_button.grid()

    def reset_calculator(self):
        # Clear all entries and reset to initial state
        for title, grade, weight, remove_button in self.components:
            title.delete(0, tk.END)
            grade.delete(0, tk.END)
            weight.delete(0, tk.END)
            remove_button.destroy()

        self.final_exam_weight_entry.delete(0, tk.END)

        self.components = []
        for _ in range(self.default_rows):
            self.add_course_component()

        self.reset_button.grid_remove()

def main():
    root = tk.Tk()
    app = GradeCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
