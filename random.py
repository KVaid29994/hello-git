import tkinter as tk


# --- Model ---
class DrawingModel:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """ Adds a shape to the model (e.g., rectangle, oval). """
        self.shapes.append(shape)

    def get_shapes(self):
        """ Retrieves all shapes. """
        return self.shapes


# --- Controller ---
class DrawingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_rectangle(self, x1, y1, x2, y2, color="blue"):
        """ Adds a rectangle to the model and updates the view. """
        shape = {"type": "rectangle", "x1": x1, "y1": y1, "x2": x2, "y2": y2, "color": color}
        self.model.add_shape(shape)
        self.view.update_view(self.model.get_shapes())

    def add_oval(self, x1, y1, x2, y2, color="yellow"):
        """ Adds an oval to the model and updates the view. """
        shape = {"type": "oval", "x1": x1, "y1": y1, "x2": x2, "y2": y2, "color": color}
        self.model.add_shape(shape)
        self.view.update_view(self.model.get_shapes())


# --- Presenter (View) ---
class DrawingView:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

    def update_view(self, shapes):
        """ Updates the canvas with the latest shapes from the model. """
        self.canvas.delete("all")  # Clear the canvas
        for shape in shapes:
            if shape["type"] == "rectangle":
                self.canvas.create_rectangle(shape["x1"], shape["y1"], shape["x2"], shape["y2"], outline="black", fill=shape["color"], width=2)
            elif shape["type"] == "oval":
                self.canvas.create_oval(shape["x1"], shape["y1"], shape["x2"], shape["y2"], outline="black", fill=shape["color"], width=2)


# --- Main Application ---
def main():
    root = tk.Tk()
    root.title("MCP Drawing Application")

    # Create the Model, View, and Controller
    model = DrawingModel()
    view = DrawingView(root)
    controller = DrawingController(model, view)

    # Add shapes via the controller
    controller.add_rectangle(50, 50, 150, 150, color="blue")
    controller.add_oval(200, 50, 300, 150, color="yellow")
    controller.add_rectangle(100, 200, 250, 350, color="red")
    controller.add_oval(50, 250, 150, 350, color="green")

    root.mainloop()


if __name__ == "__main__":
    main()
