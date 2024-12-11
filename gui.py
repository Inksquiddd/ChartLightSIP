from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys
import time
import threading
import socket

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\\Users\\degga\\Desktop\\ChartlightDev-main\\New CLD GUI\Build Attempt 3\\11-15-Vers_CHARTLIGHT\\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to display text in a designated output box
def display_text(entry, output):
    content = entry.get("1.0", "end-1c")  # Get text from the entry box
    output.delete("1.0", "end")  # Clear previous content in the output box
    output.insert("1.0", content)  # Insert new content into the output box

backend_window = Tk()
backend_window.title("back end baybee")
frontend_window = Tk()##makes the second window
frontend_window.overrideredirect(True)#removes titlebar
frontend_window.title("front end baybee")
frontend_window.geometry("812x920")
frontend_window.configure(bg="#3C3C3C")
backend_window.geometry("512x620")
backend_window.configure(bg="#3C3C3C")

BE_canvas = Canvas(
    backend_window,
    bg="#3C3C3C",
    height=620,
    width=512,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
FE_canvas = Canvas(
    frontend_window,
    bg="#3C3C3C",
    height=620,
    width=512,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
BE_canvas.place(x=0, y=0)
FE_canvas.place(x=0, y=0)

# Title Text
BE_canvas.create_text(
    5.0,
    8.0,
    anchor="nw",
    text="ChartLight Administrative Menu - Home",
    fill="#FFFFFF",
    font=("AbhayaLibre Regular", 24 * -1)
)


# Focus Box
BE_canvas.create_text(
    20.0,
    76.0,
    anchor="nw",
    text="Focus Box",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 15 * -1)
)
####################################################################
# Output text area for the TIMER Box

class Timer:
    def __init__(self,seconds,looping,tog):
        self.seconds = seconds  # Initial countdown duration
        self.running = False  # Indicates if the timer is running
        self.timer_thread = None  # Holds the thread instance
        self.looping= looping #runs the timer continuously
        self.tog= tog #allows for the timer to run alongside the button toggle and force frequently

    def countdown(self):
        self.running = True
        while self.seconds > 0 and self.running:
            print(f"Time left: {self.seconds} seconds", end="\r")
            FE_canvas.after(0, lambda secs=self.seconds: FE_canvas.itemconfigure(timertext, text=f"Timer: {secs}"))
            time.sleep(1)
            self.seconds -= 1
        
        if self.looping:
            self.restart_timer()
        elif self.running:  # Only display "Time's up!" if not stopped
            print("Time's up!                ")
            self.running = False
        self.tog()

    def start_timer(self):
        if self.running:  # If already running, don't start again
            print("\nTimer is already running.")
            return
        
        self.seconds = 5  # Reset the timer
        self.timer_thread = threading.Thread(target=self.countdown, daemon=True)
        self.timer_thread.start()

    def restart_timer(self):
        if self.running:
            self.running = False  # Stop the current timer
            self.timer_thread.join()  # Wait for the thread to finish

        self.start_timer()
timer= Timer(5,False, lambda: None )


###############       ###################          #################
def closerooni():
    try:
        frontend_window.destroy()
    except:
        pass
        
    backend_window.destroy()
    sys.exit()
    
backend_window.protocol("WM_DELETE_WINDOW",closerooni)

#this pushes backend to the front
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frontend_window.focus_force(),
    relief="flat"
)
button_1.place(x=22.125, y=93.5, width=105.6, height=14.7,
    in_=frontend_window)

#This section will do connectivity once the desktop has demonstrated the ability

class LoopWorm:
    def __init__(self):
        self.server_ip= "192.168.0.102" 
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_ip, 12345))
        print(f"Connected to the server at {self.server_ip}")
    def start_net(self):
       
        self.timer_thread = threading.Thread(target=self.wiggly , daemon=True)
        self.timer_thread.start()
    def wiggly(self):
        try:
            while True:
                # Receive and print the server's response
                response = self.client_socket.recv(1024).decode('utf-8')
                if response == "Pbutton":
                    FE_canvas.after(0, lambda :frontend_window.focus_force())
                    print("Pbutton_Pressed")
        except KeyboardInterrupt:
            print("Client stopped.")
        finally:
            self.client_socket.close()
#instance
loopWorm= LoopWorm()
loopWorm.start_net()

#timer2 toggle on off with timer restart
def Retimer2():
    if timer2.running:
        timer2.running=False
    else:
        timer2.restart_timer()



##Timer 2 (not the five second one)
timer2= Timer(10,True,lambda:FE_canvas.after(0, lambda:frontend_window.focus_force() ))

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Retimer2(),
    relief="flat"
)
button_4.place(x=22.125, y=125.5, width=105.6, height=14.7,
    in_=frontend_window)


#########################################
#########################################

#Host button for server



# Output text area for the Active Users Box
# TIMER Box
BE_canvas.create_text(
    165.0,
    75.0,
    anchor="nw",
    text="Timer Box",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 15 * -1)
)




# this allows the application to be terminated
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
  
    relief="flat"
)
button_2.place(x=165.0, y=95.0, width=91.95, height=15.0)


#Fill in wireframed buttons potential

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frontend_window.focus_force(),
    relief="flat"
)
button_5.place(x=165.0, y=125.5, width=90.0, height=14.7,
    in_=frontend_window)
#secondfiller
button_image_6 = PhotoImage(file=relative_to_assets("button_5.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frontend_window.focus_force(),
    relief="flat"
)
button_6.place(x=165.0, y=145.5, width=90.0, height=14.7,
    in_=frontend_window)
#third
button_image_7 = PhotoImage(file=relative_to_assets("button_5.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frontend_window.focus_force(),
    relief="flat"
)
button_7.place(x=165.0, y=165.5, width=90.0, height=14.7,
    in_=frontend_window)
#fourth
button_image_8 = PhotoImage(file=relative_to_assets("button_5.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frontend_window.focus_force(),
    relief="flat"
)
button_8.place(x=165.0, y=185.5, width=90.0, height=14.7,
    in_=frontend_window)
#fifth
button_image_9 = PhotoImage(file=relative_to_assets("button_5.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frontend_window.focus_force(),
    relief="flat"
)
button_9.place(x=165.0, y=205.5, width=90.0, height=14.7,
    in_=frontend_window)
#sixth
button_image_10 = PhotoImage(file=relative_to_assets("button_5.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: frontend_window.focus_force(),
    relief="flat"
)
button_10.place(x=165.0, y=225.5, width=90.0, height=14.7,
    in_=frontend_window)



#leftmost rectangle 
BE_canvas.create_rectangle(
    15.0,
    94.0,
    130.0,
    400.0,
    fill="#D9D9D9",
    outline="")
#Middle rectangle
BE_canvas.create_rectangle(
    155.0,
    94.0,
    270.0,
    400.0,
    fill="#D9D9D9",
    outline="")

#lower Rectangle
#Middle rectangle
BE_canvas.create_rectangle(
    10.0,
    425.0,
    500.0,
    600.0,
    fill="#D9D9D9",
    outline="")

button_image_3 = PhotoImage(file=relative_to_assets("button_2.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: timer.restart_timer(),
    relief="flat"
)
button_3.place(x=165.0, y=95.0, width=91.95, height=15.0)


#just in case you need to close out the front end solamente
# button_11 = Button(
#     frontend_window,
#     text="GETOFFMYBLOCK",
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: frontend_window.destroy(), #Dont know why this was here ---> 976
#     relief="flat"
# )
# button_11.place(x=300.9, y=50.0, width=90, height=16.0)

#image placement attempt
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = BE_canvas.create_image(
    455.0,
    118.0,
    image=image_image_1
)

# Focus Box
BE_canvas.create_text(
    20.0,
    408.0,
    anchor="nw",
    text="Future Updates Box",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 15 * -1)
)
#Explanation of focus box buttons line 1
BE_canvas.create_text(
    20.0,
    158.0,
    anchor="nw",
    text="In order to force",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
# Focus Box line 2
BE_canvas.create_text(
    20.0,
    178.0,
    anchor="nw",
    text="user end upward ",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
# Focus Box line 3
BE_canvas.create_text(
    20.0,
    198.0,
    anchor="nw",
    text="press the first",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
# Focus Box line 4
BE_canvas.create_text(
    20.0,
    218.0,
    anchor="nw",
    text="button",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
# Focus Box line 5 (sepperator)
BE_canvas.create_text(
    19.0,
    225.0,
    anchor="nw",
    text="______________",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
#Second button explanation
# Focus Box line 6 
BE_canvas.create_text(
    19.0,
    250.0,
    anchor="nw",
    text="In order to run",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
# Focus Box line 7
BE_canvas.create_text(
    19.0,
    270.0,
    anchor="nw",
    text="on a loop",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
# Focus Box line 7
BE_canvas.create_text(
    19.0,
    290.0,
    anchor="nw",
    text="double click the",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
# Focus Box line 8
BE_canvas.create_text(
    19.0,
    310.0,
    anchor="nw",
    text="second button",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)

#text for things coming head
BE_canvas.create_text(
    20.0,
    438.0,
    anchor="nw",
    text="Anything YOU ask for!",
    fill="#000000",
    font=("ABeeZee Regular", 20 * -1)
)
#text for things coming body
BE_canvas.create_text(
    20.0,
    468.0,
    anchor="nw",
    text="Plans include: Increasing capacity for even more users",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
#text for second and third coming addons
BE_canvas.create_text(
    20.0,
    488.0,
    anchor="nw",
    text="                        Improving the rewards system & scoreboard",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)
#text for second and third coming addons
BE_canvas.create_text(
    20.0,
    508.0,
    anchor="nw",
    text="                        Adding audio and Visual cues to user statuses",
    fill="#000000",
    font=("ABeeZee Regular", 15 * -1)
)




#image placement attempt
image_image_2 = PhotoImage(
    file=relative_to_assets("USER SCREEN LIST.png"),
    master=FE_canvas
    )
image_2 = FE_canvas.create_image(
    250.0,
    300.0,
    image=image_image_2
)



#TIMER LAD

FE_canvas.create_text(
    5.0,
    8.0,
    anchor="nw",
    text="ChartLight USER DISPLAY - Home",
    fill="#FFFFFF",
    font=("AbhayaLibre Regular", 24 * -1)
)
#timer title
timertext= FE_canvas.create_text(
    20.0,
    525.0,
    anchor="nw",
    
    text=f"Timer: {timer.seconds }",
    fill="#FFFFFF",
    font=("AbhayaLibre Regular", 24 * -1)
)


#Scoreboard title
FE_canvas.create_text(
    25.0,
    550.0,
    anchor="nw",
    
    text="WHO'S OUR HARDEST WORKER?: JENSON THE MAN\nPoints!: 4035",
    fill="#FFFFFF",
    font=("AbhayaLibre Regular", 12 * -1)
)







backend_window.resizable(False, False)
# backend_window.mainloop()
frontend_window.mainloop()