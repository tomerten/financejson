class Tree:
    """
    Class to print nested dictionary
    as a tree (similar to unix command).
    """

    def __init__(self):
        self.keyCount = 0
        self.listCount = 0
        self.outstr = ''

    def register(self, dc):
        """
        Method to keep track of the number of (subkeys)
        and number of lists in the structure.
        :param dc: dictionary or list
        :type dc: dictionary or list
        :return:
        """
        if isinstance(dc, dict):
            self.keyCount += 1
        elif isinstance(dc, list):
            self.listCount += 1

    def summary(self) -> str:
        """
        Print dictionary summary.
        :return: print summary of data
        """
        return str(self.keyCount) + " keys, " + str(self.listCount) + " lists"

    def walk(self, dc, prefix=""):
        """
        Method to walk through the
        data structure and build
        tree representation as a string
        which is stored in outstr.
        :param dc: data structure to print
        :param prefix: initial prefix
        :return: updates self.outstr
        """
        # finance data
        # is either dict or list of dicts
        # to print the structure we only
        # need the keys of one of the elements
        # in case data is a list
        if isinstance(dc, list):
            if isinstance(dc[0], dict):
                dc = dc[0]

        for i in range(len(dc)):
            k = list(dc.keys())[i]
            v = dc[k]
            self.register(v)

            if i == len(dc) - 1:
                self.outstr += f'{prefix}└─── {k} ({type(v)})\n'
                if isinstance(v, dict):
                    self.walk(v, prefix + "    ")
                elif isinstance(v, list):
                    self.walk(v, prefix + "    ")
            else:
                self.outstr += f'{prefix}├─── {k} ({type(v)})\n'
                if isinstance(v, dict):
                    self.walk(v, prefix + "|   ")
                elif isinstance(v, list):
                    if isinstance(v[0], dict):
                        self.walk(v[0], prefix + "|   ")
