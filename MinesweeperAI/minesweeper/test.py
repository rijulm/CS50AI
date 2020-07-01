import  pyautogui
for i in range(35):
    pyautogui.typewrite("BHARGAVI IS GORGEOUS!!!")
    pyautogui.press('enter')

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # to check if cell in sentence, i think we check within the self.cells
        if cell in self.cells:
            self.cells.discard(cell)
            self.count -= 1


        # we dont change the number of count
        # raise NotImplementedError

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.discard(cell)
        # raise NotImplementedError



