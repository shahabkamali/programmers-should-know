
class Handler:  # Abstract handler
    """Abstract Handler"""
    def __init__(self, successor):
        # Define who is the next handler
        self._successor = successor  # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request)  # If handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


class ConcreteHandler1(Handler):  # Inherits from the abstract handler
    """Default handler"""
    def _handle(self, request):
        if 0 < request <= 10: # Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True  # Indicates that the request has been handled


class DefaultHandler(Handler):  # Inherits from the abstract handler
    """Default handler"""

    def _handle(self, request):
        """If there is no handler available"""
        # No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True # Indicates that the request has been handled


class Client:  # Using handlers
    def __init__(self):
        # Create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):  # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


# Create a client
c = Client()
# Create requests
requests = [2, 5, 30]

# Send the request
c.delegate(requests)