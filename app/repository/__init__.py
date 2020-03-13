class Repository(object):
    def __init__(self, adapter=None):
        self.client = adapter()

    def find_all(self, selector):
        return self.client.find_all(selector)

    def find(self, selector):
        return self.client.find(selector)

    def update(self, selector, PFRM):
        return self.client.update(selector, PFRM)

    def delete(self, selector):
        return self.client.delete(selector)

#possibility of DRYer structure?
