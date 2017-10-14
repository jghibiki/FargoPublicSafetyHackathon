
class Eventable:

    def handle_event(self, event):
        raise Exception("{0} must override {0}.handle_event()".format(type(self).__name__))
