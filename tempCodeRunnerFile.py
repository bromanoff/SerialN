for file in os.listdir("./test"):
    if file.endswith(".jpg"):
        img = Image.open(file)
        img.show()