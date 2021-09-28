class FileSystem:

    def __init__(self):
        self.d = {}

    def ls(self, path: str) -> List[str]:
        hier = path.split('/')[1:]
        h = self.d
        for level in hier:
            if level == '':
                break
            elif level not in h:
                return None
            elif isinstance(h[level], str):
                return [level]
            h = h[level]
        return sorted(h.keys())

    def mkdir(self, path: str) -> None:
        location = path.split('/')[1:]
        h = self.d
        for level in location:
            if level not in h:
                h[level] = {}
            h = h[level]
            
    def addContentToFile(self, filePath: str, content: str) -> None:
        location = filePath.split('/')[1:]
        h = self.d
        for level in location[:-1]:
            if level not in h:
                h[level] = {}
            h = h[level]
        h[location[-1]] = h.get(location[-1], '') + content
        
    def readContentFromFile(self, filePath: str) -> str:
        h = self.d
        location = filePath.split('/')[1:]
        for level in location[:-1]:
            if level not in h:
                return None
            h = h[level]
        return h.get(location[-1], None)