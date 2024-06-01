import psutil
import time
import tkinter as tk
from tkinter import StringVar

class NetworkMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Network Speed Monitor")
        self.geometry("300x100")
        
        self.upload_speed_var = StringVar()
        self.download_speed_var = StringVar()
        
        self.create_widgets()
        self.update_speeds()
    
    def create_widgets(self):
        tk.Label(self, text="Download Speed:").pack()
        tk.Label(self, textvariable=self.download_speed_var).pack()
        
        tk.Label(self, text="Upload Speed:").pack()
        tk.Label(self, textvariable=self.upload_speed_var).pack()
    
    def update_speeds(self):
        net_io = psutil.net_io_counters()
        time.sleep(1)
        net_io_updated = psutil.net_io_counters()
        
        download_speed = (net_io_updated.bytes_recv - net_io.bytes_recv) / 1024
        upload_speed = (net_io_updated.bytes_sent - net_io.bytes_sent) / 1024
        
        self.download_speed_var.set(f"{download_speed:.2f} KB/s")
        self.upload_speed_var.set(f"{upload_speed:.2f} KB/s")
        
        self.after(1000, self.update_speeds)

if __name__ == "__main__":
    app = NetworkMonitor()
    app.mainloop()
