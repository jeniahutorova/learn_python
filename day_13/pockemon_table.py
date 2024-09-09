# Attributes represent data or properties that describe an object.
# Example: self.color, self.make
# Methods represent actions or behaviors that an object can perform.
# Example: self.drive(), self.stop()

from prettytable import PrettyTable

table = PrettyTable()

# Methods
table.add_column("Pockemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Attributes
table.align["Pockemon Name"] = "l"
table.align["Type"] = "l"

print(table)
