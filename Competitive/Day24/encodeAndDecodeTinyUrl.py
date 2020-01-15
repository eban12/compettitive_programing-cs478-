class Codec:
    def __init__(self):
        self.store = {}
        
    def encode(self, longUrl: str) -> str:
        url = longUrl[longUrl.index(':') + 2:]
        key = hash(url)
        self.store[str(key)] = longUrl
        return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        key = shortUrl[len("http://tinyurl.com/") :]
        return self.store[key]
