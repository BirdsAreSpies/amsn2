
import pymsn
import pymsn.event


class ClientEvents(pymsn.event.ClientEventInterface):
    def __init__(self, client, amsn_core):
        self._amsn_core = amsn_core
        pymsn.event.ClientEventInterface.__init__(self, client)

    def on_client_state_changed(self, state):
        self._amsn_core.connectionStateChanged(self._client._amsn_profile, state)

    def on_client_error(self, error_type, error):
        print "ERROR :", error_type, " ->", error
    
    
