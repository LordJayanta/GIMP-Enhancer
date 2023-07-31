#!/usr/bin/env python

from gimpfu import *

def create_rectangle(image, drawable, width, height, radius, fill_color, border_color, border_size):
    pdb.gimp_context_push()
    pdb.gimp_image_undo_group_start(image)
    
    # Create a new layer for the rectangle
    layer = pdb.gimp_layer_new(image, width, height, RGB_IMAGE, "Rectangle", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(image, layer, None, 0)
    
    # Set the foreground color to the fill color
    pdb.gimp_context_set_foreground(fill_color)
    
    # Fill the layer with the foreground color
    pdb.gimp_edit_fill(layer, FOREGROUND_FILL)
    
    # Add a border to the rectangle
    if border_size > 0:
        pdb.gimp_selection_all(image)
        pdb.gimp_context_set_foreground(border_color)
        pdb.gimp_context_set_line_width(border_size)
        pdb.gimp_edit_stroke(layer)
    
    # Set the border radius of the rectangle
    if radius > 0:
        pdb.gimp_selection_all(image)
        pdb.gimp_context_set_background(fill_color)
        pdb.gimp_edit_round_corners(layer, radius, radius, 0, 0, 0, 0)
    
    # Center the layer on the canvas
    layer_position = (image.width - layer.width) // 2, (image.height - layer.height) // 2
    pdb.gimp_layer_set_offsets(layer, *layer_position)
    
    pdb.gimp_image_undo_group_end(image)
    pdb.gimp_context_pop()
    
    # Return the path of the rectangle layer
    return layer

register(
    "python-fu-create-rectangle",
    "Create a rectangle layer with customizable parameters",
    "Create a rectangle layer with customizable parameters",
    "LordJayanta",
    "LordJayanta",
    "2023",
    "Create Rectangle...",
    "",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
        (PF_INT, "width", "Width of the rectangle", 100),
        (PF_INT, "height", "Height of the rectangle", 100),
        (PF_INT, "radius", "Border radius of the rectangle", 0),
        (PF_COLOR, "fill_color", "Fill color of the rectangle", (0, 0, 0)),
        (PF_COLOR, "border_color", "Border color of the rectangle", (255, 255, 255)),
        (PF_INT, "border_size", "Size of the rectangle border", 0)
    ],
    [ 
        (PF_LAYER, "layer", "Created rectangle layer", None),
    ],
    create_rectangle,
    menu="<Image>/Enhancer/Shape"
)

main()
