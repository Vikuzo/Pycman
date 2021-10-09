import threading
import time


class Character(threading.Thread):
    def __init__(self, image, x, y, size_x, size_y, maze, movement, row, column):
        threading.Thread.__init__(self)

        self.__image = image
        self.__x = x
        self.__y = y
        self.__size_x = size_x
        self.__size_y = size_y
        self.__maze = maze
        self.__direction = ''

        self.__LEFT = 'LEFT'
        self.__RIGHT = 'RIGHT'
        self.__UP = 'UP'
        self.__DOWN = 'DOWN'
        self.__MOVEMENT = movement
        self.__ROW = row
        self.__COLUMN = column

    def get_image(self):
        return self.__image

    def set_image(self, image):
        self.__image = image

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_size_x(self):
        return self.__size_x

    def set_size_x(self, size_x):
        self.__size_x = size_x

    def get_size_y(self):
        return self.__size_y

    def set_size_y(self, size_y):
        self.__size_y = size_y

    def get_maze(self):
        return self.__maze

    def set_maze(self, maze):
        self.__maze = maze

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = direction

    def get_left(self):
        return self.__LEFT

    def get_right(self):
        return self.__RIGHT

    def get_up(self):
        return self.__UP

    def get_down(self):
        return self.__DOWN

    def get_movement(self):
        return self.__MOVEMENT

    def get_row(self):
        return self.__ROW

    def get_column(self):
        return self.__COLUMN


class Player(Character):
    def __init__(self, image, x, y, size_x, size_y, maze, movement, row, column, size_adapter):
        self.__run = True
        self.__size_adapter = size_adapter
        super().__init__(image, x, y, size_x, size_y, maze, movement, row, column)

    def run(self):
        self.set_direction(self.get_left())

        while self.__run:
            if self.get_direction() == self.get_left():
                r = self.get_y()//(self.get_size_y()//self.__size_adapter)
                c = (self.get_x() - self.get_movement())//(self.get_size_x()//self.__size_adapter)
                if self.get_maze()[r][c] == '0':
                    r = (self.get_y() + self.get_size_y() - 3)//(self.get_size_y()//self.__size_adapter)
                    if self.get_maze()[r][c] == '0':
                        self.set_x(self.get_x() - self.get_movement())
            if self.get_direction() == self.get_up():
                r = (self.get_y() - self.get_movement()) // (self.get_size_y() // self.__size_adapter)
                c = self.get_x() // (self.get_size_x() // self.__size_adapter)
                if self.get_maze()[r][c] == '0':
                    c = (self.get_x() + self.get_size_x() - 3) // (self.get_size_x() // self.__size_adapter)
                    if self.get_maze()[r][c] == '0':
                        self.set_y(self.get_y() - self.get_movement())
            if self.get_direction() == self.get_right():
                r = self.get_y() // (self.get_size_y() // self.__size_adapter)
                c = ((self.get_x() + self.get_size_x()) + self.get_movement()) // (self.get_size_x() //
                                                                                   self.__size_adapter)
                if self.get_maze()[r][c] == '0':
                    r = (self.get_y() + self.get_size_y() - 3) // (self.get_size_y() // self.__size_adapter)
                    if self.get_maze()[r][c] == '0':
                        self.set_x(self.get_x() + self.get_movement())
            if self.get_direction() == self.get_down():
                r = ((self.get_y() + self.get_size_y()) + self.get_movement()) // (self.get_size_y() //
                                                                                   self.__size_adapter)
                c = self.get_x() // (self.get_size_x() // self.__size_adapter)
                if self.get_maze()[r][c] == '0':
                    c = (self.get_x() + self.get_size_x() - 3) // (self.get_size_x() // self.__size_adapter)
                    if self.get_maze()[r][c] == '0':
                        self.set_y(self.get_y() + self.get_movement())

            time.sleep(0.0175)

    def get_run(self):
        return self.__run

    def set_run(self, run):
        self.__run = run


class Ghost(Character):
    def __init__(self, image, x, y, size_x, size_y, maze, movement, row, column, player):
        super().__init__(image, x, y, size_x, size_y, maze, movement, row, column)

        self.__player = player

    def run(self):
        pass

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player
