import tkinter as tk
from tkinter import ttk

import numpy as np
from PIL import Image, ImageDraw, ImageGrab


class HandWritingRecognitionApp:
    def __init__(self,window):
        self.window=window
        self.window.title("HandWriting Recogniztion")

        self.canvas= tk.Canvas(self.window, width=280, height=280,bg="white")
        self.canvas.pack(padx=10,pady=10)
        self.canvas.bind("<B1-Motion>",self.draw)

        ttk.Button(self.window, text="Clear", command=self.clear).pack(side=tk.LEFT)
        ttk.Button(self.window, text="Recognize", command=self.recognize).pack(side=tk.RIGHT)

        self.modle=None

    def draw(self,event):
        x1, y1=(event.x-8), (event.y-8)
        x2, y2=(event.x+8), (event.y+8)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black")

    def clear(self):
        self.canvas.delete("all")

    def recognize(self):
        img= Image.new("RGB",(280,280),"white")
        draw=ImageDraw.Draw(img)
        draw.rectangle([0, 0, 280,280], fill="white")
        img.paste(ImageGrab.grab(bbox=(
            self.window.winfo_x() + self.canvas.winfo_x(),
            self.window.winfo_y() + self.canvas.winfo_y(),
            self.window.winfo_x() + self.canvas.winfo_x() + 280,
            self.window.winfo_y() + self.canvas.winfo_y() + 280
        )).convert("L"))

        if self.model is None:
            self.model  = load_model()
        result = self.model.predict(img)
        digit = np.argmax(result)

        tk.messagebox.showinfo(tite="Recognition Result", message=f"Predicted digit:{digit}")

if __name__=="__main__":
    app=HandWritingRecognitionApp(tk.Yk())
    app.window.mainloop()