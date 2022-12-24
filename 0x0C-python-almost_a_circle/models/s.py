def update(self, *args, **kwargs):
        """Magical method"""
        if (args) and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            else:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]

        if not args:
            for key, value in kwargs.items():
                if len(kwargs) == 1:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                elif len(kwargs) == 2:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                elif len(kwargs) == 3:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                elif len(kwargs) == 4:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                else:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
