from amsn2.ui import base
import gobject

class aMSNMainLoop(base.aMSNMainLoop):
    def __init__(self, amsn_core):
        self._amsn_core = amsn_core

    def run(self):
        self._mainloop = gobject.MainLoop(is_running=True)
        while self._mainloop.is_running():
            try:
                self._mainloop.run()
            except KeyboardInterrupt:
                self.quit()


    def idler_add(self, func):
        gobject.idle_add(func)

    def timer_add(self, delay, func):
        gobject.timeout_add(delay, func)

    def quit(self):
        self._mainloop.quit()

