from Ui import *

# fix/understand mainloop
# start with dnd api/db



root = tk.Tk()

bag1 = BagWidget(root, "backpack")
bag2 = BagWidget(root, "knapsap")

bag1.create_item("potion", 1)
bag1.create_item("tee", 2)
bag1.create_item("great sword", 2)
bag2.create_item("potion", 1)
bag2.create_item("tee", 2)
bag2.create_item("great sword", 2)

bag1.mainloop()
bag2.mainloop()

