########################################### Import Packages ###########################################
# Tkinter for create GUI game
import tkinter as tk    
########################################### Import Packages ###########################################


######################################## Screen Initialization ########################################
# Create a new window
window = tk.Tk()
 
# Set the area of the window
window.geometry("600x400")
 
# Set the background color
window.configure(background = 'lightblue')   

# Set the resizable = False
window.resizable(width = False, height = False)
 
# Set Title
window.title('BMI 計算機')
######################################## Screen Initialization ########################################


########################################## Define Functions ##########################################
# update the result text
def update_text(text):
    # Global variables
    
    result.configure(text = text)

# Calculate BMI
def calculate_bmi():
    # Global variables
    global height_output, weight_output

    # get the value of Entry
    height_get = float(height_output.get())
    weight_get = float(weight_output.get())
    
    # Check the unit: meter or centermeter
    if height_get <= 3:
        bmi = weight_get / height_get**2
    else:
        bmi = weight_get / (height_get*0.01)**2

    # Check the bmi between 18.5~24
    if bmi < 18.5:
        result = "您的 BMI 為： %d, 有點吃太少囉～" % (bmi)

    elif bmi <=24:
        result = "您的 BMI 為： %d, 非常健康喔～" % (bmi)

    else:
        result = "您的 BMI 為： %d, 有點吃太多囉～" % (bmi)

    # update the result text
    update_text(result)
########################################## Define Functions ##########################################
play_button = tk.Button(window, text = "計算結果", font = ("Arial", 14, "bold"), fg = "Black", command = calculate_bmi)


###################################### Draw Label, Button, Entry ######################################
# Label Text 
title = tk.Label(window, text = "BMI 計算機", font = ("Arial", 24), fg = "black", bg = "lightblue")
name = tk.Label(window,   text = "姓名 :", font = ("Arial", 18), fg = "black", bg = "lightblue")
height = tk.Label(window, text = "身高 :", font = ("Arial", 18), fg = "black", bg = "lightblue")
weight = tk.Label(window, text = "體重 :", font = ("Arial", 18), fg = "black", bg = "lightblue")
result = tk.Label(window, text = "BMI :", font = ("Arial", 18), fg = "black", bg = "lightblue")
 
# Play Button
 
# Exit Button
exit_button = tk.Button(window, text = "結束系統", font = ("Arial", 14, 'bold'), fg = "black", command = exit)

# Entry for name
name_input = tk.StringVar()
name_output = tk.Entry(window, width=30, font=("Arial", 16), textvariable = name_input)

# Entry for height
height_input = tk.StringVar()
height_output = tk.Entry(window, width=30, font=("Arial", 16), textvariable = height_input)

# Entry for weight
weight_input = tk.StringVar()
weight_output = tk.Entry(window, width=30, font=("Arial", 16), textvariable = weight_input)

# Place the labels
title.place(x = 240, y = 20)
name.place(x = 150, y = 100)
height.place(x = 150, y = 145)
weight.place(x = 150, y = 190)
result.place(x = 150, y = 235)
 
# Place the buttons
exit_button.place(x = 360, y = 320)
play_button.place(x = 190, y = 320)

# Place the entry field
name_output.place(x = 220, y = 100)
height_output.place(x = 220, y = 145)
weight_output.place(x = 220, y = 190)
###################################### Draw Label, Button, Entry ######################################


# Run
window.mainloop()