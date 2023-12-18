class LocalPlugin:

    name = "flake8-local-plugin"
    version = "1.0.0"

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        yield 1, 1, "EL001 Local plugin", type(self)
