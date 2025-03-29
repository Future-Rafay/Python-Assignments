import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraseCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        self.create_grid()
        
        # Bind mouse movement for erasing
        self.canvas.bind("<Motion>", self.erase_objects)
        
        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

    def create_grid(self):
        """Create a grid of blue cells."""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

    def erase_objects(self, event):
        """Erase objects when the eraser moves."""
        # Move eraser with the mouse
        self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        
        # Find overlapping objects
        overlapping_objects = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        
        # Erase (turn white) any blue cells that the eraser touches
        for obj in overlapping_objects:
            if obj != self.eraser:
                self.canvas.itemconfig(obj, fill="white")

def main():
    root = tk.Tk()
    root.title("Erase Canvas")
    app = EraseCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
