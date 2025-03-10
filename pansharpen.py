import orthority as oty

def pansharpen_image(
        input_low_resolution_path,
        input_high_resolution_path,
        output_image_path
        ):
    pan_sharp = oty.PanSharpen(input_high_resolution_path, input_low_resolution_path)
    pan_sharp.process(output_image_path)