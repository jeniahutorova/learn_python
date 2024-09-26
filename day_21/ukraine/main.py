import turtle
import pandas

image = r"C:\Users\jenia\Desktop\learn_python\day_21\ukraine\ukraine_img.gif"


turtle.addshape(image)
turtle.shape(image)

# Function to find coordinates of regions
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
 
# regions = {
#     "Vinnytsia": [-182, 21],
#     "Dnipro": [135, -10],
#     "Donetsk": [309, -47],
#     "Zhytomyr": [-193, 168],
#     "Zaporizhzhia": [203, -114],
#     "Ivano-Frankivsk": [-399, 21],
#     "Kyiv": [ -74, 148],
#     "Lviv": [-427, 88],
#     "Luhansk": [427, 2],
#     "Mykolaiv": [6, -91],
#     "Odesa": [-82, -111],
#     "Poltava": [83, 102],
#     "Rivne": [-285, 165],
#     "Sumy": [123, 204],
#     "Ternopil": [-332, 74],
#     "Kharkiv": [248, 77],
#     "Kherson": [72, 148],
#     "Khmelnytskyi": [-260, 75],
#     "Cherkasy": [-58, 41],
#     "Chernivtsi": [-326, -33],
#     "Chernihiv": [-18, 239],
#     "Uzhhorod": [-354, 214],
#     "Lutsk": [-346, 217],         
#     "Kropyvnytskyi": [-24, -9],
#     "Crimea": [129, -250]
# }
# region_names = []
# x_coordinates = []
# y_coordinates = []

# for region, coords in regions.items():
#     if coords:
#         region_names.append(region)
#         x_coordinates.append(coords[0])
#         y_coordinates.append(coords[1]) 
# regions_data = pandas.DataFrame({
#     "Region" : region_names,
#     "x" : x_coordinates,
#     "y" : y_coordinates
# })
# regions_data.to_csv(r"C:\Users\jenia\Desktop\learn_python\day_21\ukraine.py\regions.csv")


guessed_regions = []
data = pandas.read_csv(r"C:\Users\jenia\Desktop\learn_python\day_21\ukraine\regions.csv")
regions = data["Region"].to_list()


while len(guessed_regions) < 25:
    answer_region = turtle.textinput(f"{len(guessed_regions)}/25 Regions Correct", "What's another region name?").title()
    if answer_region == "Exit":
        missing_region = []
        for region in regions:
            if region not in guessed_regions:
                missing_region.append(region)
        ungessed_df = pandas.DataFrame(missing_region)
        ungessed_df.to_csv(r"C:\Users\jenia\Desktop\learn_python\day_21\ukraine\ungessed_regions.csv")
        break
    if answer_region in regions and answer_region not in guessed_regions:
        guessed_regions.append(answer_region)
        
        t = turtle.Turtle()
        
        t.penup()
        t.hideturtle()
        region_data = data[data["Region"] == answer_region]
        t.goto(region_data.x.item(), region_data.y.item())
        t.write(region_data["Region"].item(), align="left", font=("Arial", 10, "normal"))
        