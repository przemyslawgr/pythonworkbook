gizmo_weight = 112
widgets_weight = 75
gizmo_quantity = int(input("Quantity of gizmos:"))
widgets_quantity = int(input("Quantity of widgets:"))
total_weight = gizmo_quantity * gizmo_weight + widgets_quantity * widgets_weight
print(f"Total weight: {total_weight}")