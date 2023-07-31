#!/usr/bin/env python

from gimpfu import *

def create_center_guide(image, drawable, guide_type, position_percentage):
    pdb.gimp_image_undo_group_start(image)

    if drawable:
        x, y = pdb.gimp_drawable_offsets(drawable)
        width = pdb.gimp_drawable_width(drawable)
        height = pdb.gimp_drawable_height(drawable)
    else:
        x = 0
        y = 0
        width = image.width
        height = image.height

    if guide_type == 1:  # Vertical Guide
        guide_position = x + int((width * position_percentage) / 100)
        pdb.gimp_image_add_vguide(image, guide_position)
    else:  # Horizontal Guide
        guide_position = y + int((height * position_percentage) / 100)
        pdb.gimp_image_add_hguide(image, guide_position)

    pdb.gimp_image_undo_group_end(image)

register(
    "python_fu_create_center_guide",
    "Create center guide",
    "Create a vertical or horizontal guide at the specified position (in percentage) on the active layer or canvas.",
    "LordJayanta",
    "LordJayanta",
    "2023",
    "<Image>/Enhancer/Smart Guider/Center Guide...",
    "*",
    [
        (PF_RADIO, "guide_type", "Guide Type:", 1, (("Vertical Guide", 1), ("Horizontal Guide", 2))),
        (PF_FLOAT, "position_percentage", "Position Percentage:", 50.0)
    ],
    [],
    create_center_guide)

main()
