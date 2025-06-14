def get_function():
    def get(collection, key, default_value=None):
        return collection.get(key, default_value)
    return get
