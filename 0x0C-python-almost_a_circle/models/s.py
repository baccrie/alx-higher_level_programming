def update(self, *args, **kwargs):
        if (args) and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
            else:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]

        if not args:
            for key, value in kwargs.items():
                if len(kwargs) == 1:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]
                elif len(kwargs) == 2:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]
                elif len(kwargs) == 3:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]
                elif len(kwargs) == 4:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]
