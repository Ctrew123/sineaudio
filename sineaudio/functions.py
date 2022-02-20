import pyaudio
import numpy as np

def running_audio():
  """ 
  A function that plays a sound without storing it as a file
  """
  p = pyaudio.PyAudio()

  volume = 0.5   
  fs = 44100       
  duration = 1.0   
  f = 440.0        


  samples =    (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)


  stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)


  stream.write(volume*samples)

  stream.stop_stream()
  stream.close()

  p.terminate()

import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np



class Sound_Wave_Altering:

    def canvas_replacement(self):
        canvas1.get_tk_widget().destroy()
        canvas2 = FigureCanvasTkAgg(fig, master = root)
        canvas2.draw()
        canvas2.get_tk_widget().place(x="50",y="0")
        canvas2.get_tk_widget().place(x="450",y="0")

        
    def __init__(self,master):
        self.root = root
        master.title("Test")
        master.geometry("1000x450")
        
        """
        A function that introduces the GUI paramterss to adjust the graph and plots the graphs for sin waves depending on paramaters
        """

        
        frequency_slider = tk.Scale(master, from_=20, to = 20000, orient = "vertical", length = 300, label = "Frequency")
        amplitude_slider = tk.Scale(master, from_=1, to = 100, orient = "vertical", length = 300, label = "Amplitude")
        wavelength_slider = tk.Scale(master, from_=1700, to = 2, orient = "vertical", length = 300, label = "Wavelength")

        frequency_slider.place(x="0", y="0")
        amplitude_slider.place(x="150", y="0")
        wavelength_slider.place(x="300", y="0")

        frequency_value = frequency_slider.get()
        amplitude_value = amplitude_slider.get()
        wavelength_value = wavelength_slider.get()

        Pressure = amplitude_value * np.sin(2*np.pi*frequency_value*wavelength_value)


        frequency_slider_textbox = tk.Entry(root, bd=5, width=6)
        amplitude_slider_textbox = tk.Entry(root, bd=5, width=6)
        wavelength_slider_textbox = tk.Entry(root, bd=5, width=6)
        frequency_slider_button = tk.Button(root, text = "Set frequency", command = lambda : frequency_slider.set(frequency_slider_textbox.get()))
        amplitude_slider_button = tk.Button(root, text = "Set amplitude", command = lambda :  amplitude_slider.set(amplitude_slider_textbox.get()))
        wavelength_slider_button = tk.Button(root, text = "Set wavelength", command = lambda : wavelength_slider.set(wavelength_slider_textbox.get()))


        frequency_slider_textbox.place(x="25", y = "325")
        amplitude_slider_textbox.place(x="165", y = "325")
        wavelength_slider_textbox.place(x="315", y = "325")
        frequency_slider_button.place(x="0", y = "350")
        amplitude_slider_button.place(x="150", y = "350")
        wavelength_slider_button.place(x="300", y = "350")


        x = [frequency_slider.get() * np.sin(i) for i in range(0, 100)]
        Pressure = [amplitude_value * np.sin(2*np.pi*frequency_value*wavelength_value * x) for x in range(0,100)]

        fig  = Figure(figsize = (5, 5), dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.plot(Pressure)
        canvas1 = FigureCanvasTkAgg(fig, master = root)
        canvas1.draw()
        toolbar = NavigationToolbar2Tk(canvas1, root)
        toolbar.update()
        canvas1.get_tk_widget().place(x="450", y="0")
        
        plot_button = tk.Button(root, command = lambda : canvas_replacement(), height = 2, width = 10, text = "Plot")
        plot_button.place(x="450", y="400")

        play_button = tk.Button(root, text = "Play")
        play_button.place(x="500", y="400")





        
root = tk.Tk()
gui = Sound_Wave_Altering(root)
root.mainloop()
