import json, pathlib
class SaveLoad:
    def __init__(self, path="save.json"):
        self.path = pathlib.Path(path)
    def save(self, data):
        self.path.write_text(json.dumps(data, indent=2))
    def load(self):
        if self.path.exists():
            return json.loads(self.path.read_text())
        return {}
