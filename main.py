# from turtle import Turtle, Screen
# # import another_module

# # print(another_module.another_variable)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table.align)
table.align = "l"
print(table)
