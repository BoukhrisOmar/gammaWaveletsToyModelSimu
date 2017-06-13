import sys

class MyProgressBar :
    def __init__ (self, nb_element=100, width=100) :
        self.el_cpt = 0
        self.nb_element = nb_element
        self.width = width
        sys.stdout.write("[%s]" % (" " * self.width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (self.width+1))

    def update (self) :
        self.el_cpt += 1
        if self.el_cpt >= (self.nb_element/self.width) :
            n = round(self.width/self.nb_element)
            n = n if n != 0 else 1
            sys.stdout.write("="*n)
            sys.stdout.flush()
            self.el_cpt = 0
