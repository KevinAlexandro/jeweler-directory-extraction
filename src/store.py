class Store:
    """
    A class representing a jeweler store with its associated information.

    This class stores details about a jeweler store including its ID, name,
    location, contact information, and when it was scraped.
    """
    def __init__(self, store_id: str, business_name: str, scraped_at: str, town: str = None, phone_number: str = None):
        """
        Initialize a Store object with the provided information.

        Args:
            store_id (str): Unique identifier for the store.
            business_name (str): Name of the jeweler business.
            scraped_at (str): Timestamp when the store data was scraped.
            town (str, optional): Town or city where the store is located. Defaults to None.
            phone_number (str, optional): Contact phone number for the store. Defaults to None.
        """
        self.store_id = store_id
        self.business_name = business_name
        self.town = town
        self.phone_number = phone_number
        self.scraped_at = scraped_at

    def get_metadata(self):
        """
        Get the store's metadata as a dictionary.

        Returns:
            dict: A dictionary containing all store information.
        """
        return {
            'store_id': self.store_id,
            'business_name': self.business_name,
            'town': self.town,
            'phone_number': self.phone_number,
            'scraped_at': self.scraped_at
        }
