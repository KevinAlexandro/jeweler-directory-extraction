class CrawledData:
    def __init__(self):
        self.__crawled_data = {'jeweler_stores': []}

    def is_already_crawled(self, store_id: str) -> bool:
        # Check if the store with the given ID is already crawled
        return any(store['id'] == store_id for store in self.__crawled_data['jeweler_stores'])

    def add_store(self, store):
        # Check for duplicates based on 'Title' and 'Phone'
        if not self.is_already_crawled(store['id']):
            self.__crawled_data['jeweler_stores'].append(store)