import tkinter as tk

class App:
    wide_window = "400x350+200+100"
    def __init__(self, master):
        self.tkn = master
        self.tkn.title("BMI Calculator App")
        self.tkn.geometry(self.wide_window)
        self.form_input(self.tkn)

    def form_input(self, master):
        form_container = tk.Frame(self.tkn)
        form_container.pack(pady = 50)

        self.name_entry = self.name_input(form_container)
        self.weight_entry = self.weight_input(form_container)
        self.height_entry = self.height_input(form_container)
        self.submit_input(form_container)
        self.clear_input(form_container)
        self.result_name = tk.Label(master, text = "", pady=-50, padx=10)
        self.result_bmi = tk.Label(master, text = "")
        self.result_category = tk.Label(master, text = "")
        self.result_name.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.result_bmi.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        self.result_category.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        
    def name_input(self, master):
        name_label = tk.Label(master, text = "Name: ")
        name_label.grid(row = 0, column = 0, sticky = "w")
        name_entry = tk.Entry(master)
        name_entry.grid(row = 0, column = 1)
        return name_entry

    def weight_input(self, master):
        weight_label = tk.Label(master, text = "Weight (kg): ")
        weight_label.grid(row = 2, column = 0, sticky = "w")
        weight_entry = tk.Entry(master)
        weight_entry.grid(row = 2, column = 1, pady = 10)
        return weight_entry

    def height_input(self, master):
        height_label = tk.Label(master, text = "Height (cm): ")
        height_label.grid(row = 3, column = 0, sticky = "w")
        height_entry = tk.Entry(master)
        height_entry.grid(row = 3, column = 1)
        return height_entry

    def submit_input(self, master):
        submit = tk.Button(master, text = "Submit", command = self.send_form)
        submit.grid(row = 4, columnspan=1, pady=10)
    
    def clear_input(self, master):
        clear = tk.Button(master, text = "Clear form", command = self.clear_form)
        clear.grid(row = 4, columnspan = 2, pady = 10)
    
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.result_name.config(text = "")
        self.result_bmi.config(text = "")
        self.result_category.config(text = "")

    def send_form(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100
            bmi = self.formula(weight, height)
            res_bmi = f"BMI: {bmi[0]:.2f}"
            self.result_name.config(text = "Name: " + self.name_entry.get())
            self.result_bmi.config(text = "BMI: " + res_bmi)
            self.result_category.config(text = "Category: " + bmi[1])
        except ValueError:
            self.result_name.config(text = "Input Error, check your input!")

    def formula(self, weight, height):
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            return [bmi, "Slim"]
        elif bmi < 25:
            return [bmi, "Ideal"]
        else:
            return [bmi, "Fat"]
        
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
