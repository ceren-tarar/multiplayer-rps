import tkinter as tk
import tkinter.messagebox as messagebox

## RPS Gameplay 
def rps(o1,o2):
    dif = abs(o1-o2)
    if dif==1:
        if o1>o2:
            result="win"
        else:
            result = "lose"
    elif dif==2:
        if o1<o2:
            result="win"
        else:
            result ="lose"
    else:
        result = "tie"

    return result

def rps_game(num_inputs,values):
    arr = [0]*num_inputs

    for i in range(num_inputs):
        arr[i] = [i,values[i],0]

    for i in range(len(arr)):
        for c in range(1,len(arr)):

            try:
                res = rps(int(arr[i][1]),int(arr[i+c][1]))
    
                if res == "win":
                    arr[i][2]+=1

                elif res == "lose":
                    arr[i+c][2]+=1
            except:
                print()

    scorelist = [0]*num_inputs
    for i in range(len(arr)):
        scorelist[i] = arr[i][2]

    indices = [index for index, item in enumerate(scorelist) if item == max(scorelist)]

    #get results
    if len(indices) == 1:
        result = 'Winner is Player ' + str(indices[0]+1)
    else:
        for i in range(len(indices)):
            indices[i]=indices[i]+1
            
        result = 'Tie between players: ' + str(indices)

    return result


def get_inputs():
    try:
        # Get the number of inputs from the Entry widget
        num_inputs = int(entry.get())

        # Create a new Toplevel window to get the inputs
        input_window = tk.Toplevel(root)
        input_window.title("Enter Inputs")

        # Create a function to add an input value to the list
        inputs = []
        def add_input(option):
            inputs.append(option)
            if len(inputs) == num_inputs:
                # Calculate the sum of the inputs
                result = rps_game(num_inputs,inputs)

                # Display the result in a message box
                infotext =""
                for i in range(num_inputs):
                    if inputs[i] == 0:
                        s = "Rock"
                    elif inputs[i] == 1:
                        s = "Paper"
                    else:
                        s = "Scissors"
                    infotext=infotext+ f"Player {i+1} chose {s}\n"
                
                info_label.config(text=infotext)
                result_label.config(text="{}".format(result))

        # Create a Label widget for the result
        info_label = tk.Label(root)
        info_label.pack()

        result_label = tk.Label(root)
        result_label.pack()

        # Create a Button widget for each input value and each option
        for i in range(num_inputs):
            input_label = tk.Label(input_window, text="Player {}".format(i+1))
            input_label.grid(row=i, column=0)

            option1_button = tk.Button(input_window, text="Rock", command=lambda: add_input(0))
            option1_button.grid(row=i, column=1)

            option2_button = tk.Button(input_window, text="Paper", command=lambda: add_input(1))
            option2_button.grid(row=i, column=2)

            option3_button = tk.Button(input_window, text="Scissors", command=lambda: add_input(2))
            option3_button.grid(row=i, column=3)

    except ValueError:
        # Handle the case where the input value is not an integer
        messagebox.showerror("Error", "Invalid input value")

# Create the GUI window
root = tk.Tk()
root.title("Input Example")

root.geometry("500x300")

# Create the Entry widget
entry = tk.Entry(root)
entry.pack()

# Create the Button widget
button = tk.Button(root, text="Get Inputs", command=get_inputs)
button.pack()

# Start the main event loop
root.mainloop()