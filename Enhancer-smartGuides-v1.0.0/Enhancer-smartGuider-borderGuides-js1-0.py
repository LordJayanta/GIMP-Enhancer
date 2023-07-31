#!/usr/bin/env python

from gimpfu import *

def add_guides(image, drawable, border_width=0, guide_style="Solid", guide_color=(50, 168, 158)):
    # Get image dimensions
    img_width = image.width
    img_height = image.height
    
    # Calculate guide positions
    top_guide_pos = border_width
    bottom_guide_pos = img_height - border_width
    left_guide_pos = border_width
    right_guide_pos = img_width - border_width
    
    # Add top guide
    pdb.gimp_image_add_hguide(image, top_guide_pos)
    
    # Add bottom guide
    pdb.gimp_image_add_hguide(image, bottom_guide_pos)
    
    # Add left guide
    pdb.gimp_image_add_vguide(image, left_guide_pos)
    
    # Add right guide
    pdb.gimp_image_add_vguide(image, right_guide_pos)
    
    # Set guide style and color
    for guide in image.vectors:
        guide.stroked = True
        guide.stroke_style = guide_style
        guide.stroke_color = guide_color
    
    # Refresh display
    pdb.gimp_displays_flush()

register(
    "python-fu-add-guides",
    "Add guides to the image border",
    "Adds guides to the image border with the specified width",
    "LordJayanta",
    "LordJayanta",
    "2023",
    "<Image>/Enhancer/Smart Guider/Border Guides...",
    "*",  # Use "*" to indicate all image types are supported
    [
        (PF_SPINNER, "border_width", "Border Width", 0, (0, 1000, 1)),
        (PF_OPTION, "guide_style", "Guide Style", 0, ["Solid", "Dash", "Dot", "Dash Dot", "Dash Dot Dot"]),
        (PF_COLOR, "guide_color", "Guide Color", (50, 168, 158))
    ],
    [],
    add_guides
)

main()
