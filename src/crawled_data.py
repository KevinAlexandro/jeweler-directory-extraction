from store import Store


class CrawledData:
    def __init__(self):
        self.__crawled_data = {'jeweler_stores': []}

    def __is_already_crawled(self, store_id: str) -> bool:
        # Check if the store with the given ID is already crawled
        return any(store.store_id == store_id for store in self.__crawled_data['jeweler_stores'])

    def add_store(self, store: Store) -> None:
        # Check for duplicates based on 'íd'
        if not self.__is_already_crawled(store.store_id):
            self.__crawled_data['jeweler_stores'].append(store)
            print(f'Successfully crawled {store.business_name} with ID {store.store_id}.')
