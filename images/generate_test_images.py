from PIL import Image, ImageDraw, ImageFont

def generate_test_image(name, size, square_size, colors, text):
    "(width,height) ; square_size ; (color1,color2) ; text -> void, saves photo in folder"
    img = Image.new("RGB",size,"white")
    draw = ImageDraw.Draw(img)
    width = size[0]
    height = size[1]

    for row in range(height//square_size):
        for col in range(width//square_size):
            if (row + col) % 2 == 0:
                color = colors[0]
            else:
                color = colors[1]
            
            x0 = col * square_size
            y0 = row * square_size
            x1 = x0 + square_size
            y1 = y0 + square_size      

            draw.rectangle([x0, y0, x1, y1], fill=color)



    
    font = ImageFont.truetype("FreeSans.ttf",height//10)
    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    position = ((width-w)//2,(height-h)//2)
    draw.text(position, text, font=font, fill="#000000")
    img.save(name)
    return

block_size = (2000,1200)
size =(1200,1200)
square_size = 200

generate_test_image("block-image.png",block_size, square_size, ["#495363","#223d63"], "BLOCK IMAGE")
generate_test_image("image-1.png",size, square_size, ["#85AFFC","#85D37C"], "IMAGE 1")
generate_test_image("image-2.png",size, square_size, ["#95FFC7","#BF8FD4"], "IMAGE 2")    
generate_test_image("image-3.png",size, square_size, ["#F17B7B","#99C7EE"], "IMAGE 3")
generate_test_image("image-4.png",size, square_size, ["#BFEADF","#9985C5"], "IMAGE 4")