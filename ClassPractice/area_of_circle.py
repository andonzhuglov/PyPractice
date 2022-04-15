class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print(f"Creating circle with diameter {diameter}")
    # Add assignment for self.radius here:
    self.radius = diameter / 2
  def circumference(self):
    return 2 * Circle.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())

print(teaching_table.circumference())

print(round_room.circumference())