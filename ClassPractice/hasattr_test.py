can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(can_we_count_it, "count"):
    print(str(type(element)) + " has the count attribute!")
