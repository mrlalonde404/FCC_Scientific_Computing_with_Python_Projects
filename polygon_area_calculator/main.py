class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        # Returns area (width * height)
        return self.width * self.height

    def get_perimeter(self):
        # Returns perimeter (2 * width + 2 * height)
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        # Returns diagonal ((width ** 2 + height ** 2) ** .5)
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        # Returns a string that represents the shape using lines of "*".
        # The number of lines should be equal to the height and the number of "*" in each line should
        # be equal to the width. There should be a new line (\n) at the end of each line.
        # If the width or height is larger than 50, this should return the string: "Too big for picture.".
        ret_string = ""
        if self.width > 50 or self.width > 50:
            return "Too big for picture."
        else:  # make the picture string and return it
            for i in range(self.height):
                for j in range(self.width):
                    ret_string += "*"
                ret_string += "\n"
        return ret_string

    def get_amount_inside(self, shape):
        # Takes another shape (square or rectangle) as an argument.
        # Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        # For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        num_times = 0
        width_counter = self.width // shape.width
        height_counter = self.height // shape.height
        # print("width_counter:", width_counter, "\n")
        # print("height_counter", height_counter, "\n")
        for i in range(width_counter):
            for j in range(height_counter):
                num_times += 1
        return num_times

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.set_width(side)

    def __repr__(self):
        return f"Square(side={self.width})"


def main():
    rect = Rectangle(15, 10)
    sq = Square(5)

    print(rect)
    print(rect.get_picture())
    print(sq)
    print(sq.get_picture())

    actual = rect.get_amount_inside(sq)
    expected = 6
    print(actual)

    if expected == actual:
        print("pass\n")
    else:
        print(f"failed: {actual} != {expected}\n")


if __name__ == '__main__':
    main()
