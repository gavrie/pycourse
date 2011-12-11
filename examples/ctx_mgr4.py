from contextlib import contextmanager

class Logger():

    def __init__(self):
        self._indentation = -1

    def log(self, msg):
        print "..." * self._indentation, msg

    
    @contextmanager
    def indent(self):
        self._indentation += 1
        yield self.log
        self._indentation -= 1


if __name__=="__main__":
    
    logger = Logger()
    with logger.indent() as log:
        log("message")
        with logger.indent() as log:
            log("indented")
        log("unindented")
