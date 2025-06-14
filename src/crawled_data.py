from store import Store


class CrawledData:
    """
    A class to store and manage crawled jeweler store data.

    This class maintains a collection of Store objects and provides methods
    to add new stores while preventing duplicates.
    """
    def __init__(self):
        """
        Initialize an empty CrawledData object.
        """
        self.__crawled_data = {'jeweler_stores': []}

    def __is_already_crawled(self, store_id: str) -> bool:
        """
        Check if a store with the given ID is already in the crawled data.

        Args:
            store_id (str): The ID of the store to check.

        Returns:
            bool: True if the store is already crawled, False otherwise.
        """
        # Check if the store with the given ID is already crawled
        return any(store.store_id == store_id for store in self.__crawled_data['jeweler_stores'])

    def add_store(self, store: Store) -> None:
        """
        Add a store to the crawled data if it doesn't already exist.

        Args:
            store (Store): The store object to add.
        """
        # Check for duplicates based on 'íd'
        if not self.__is_already_crawled(store.store_id):
            self.__crawled_data['jeweler_stores'].append(store)
            print(f'Successfully crawled {store.business_name} with ID {store.store_id}.')
