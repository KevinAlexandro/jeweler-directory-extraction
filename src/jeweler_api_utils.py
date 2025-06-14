from store import Store
from datetime import datetime, timezone


class JewelerAPIUtils:
    """
    A utility class for processing jeweler API data.

    This class provides methods to extract and validate store data from the API response
    and convert it into Store objects.
    """
    @staticmethod
    def __get_business_name(name: str):
        """
        Validate and extract the business name.

        Args:
            name (str): The business name to validate.

        Returns:
            str or None: The validated business name or None if invalid.
        """
        if not name or not isinstance(name, str):
            return None

        return name

    @staticmethod
    def __get_store_id(store_id: str):
        """
        Validate and extract the store ID.

        Args:
            store_id (str): The store ID to validate.

        Returns:
            str or None: The validated store ID or None if invalid.
        """
        if not store_id or not isinstance(store_id, str):
            return None

        return store_id

    @staticmethod
    def __parse_properties(properties: dict):
        """
        Extract town and phone number from store properties.

        Args:
            properties (dict): Dictionary containing store properties.

        Returns:
            tuple or None: A tuple containing (town, phone_number) or None if properties is invalid.
        """
        if not properties:
            return None

        town = properties.get('Town/City')
        phone_number = properties.get('Phone number')

        return town, phone_number

    def get_store_data(self, metadata: dict):
        """
        Process store metadata and create a Store object.

        Args:
            metadata (dict): Dictionary containing store metadata from the API.

        Returns:
            Store or None: A Store object with the extracted data or None if required data is missing.

        # TODO: Consider adding error handling for cases where properties are missing or malformed.
        """
        store_id = self.__get_store_id(metadata.get('Id'))
        business_name = self.__get_business_name(metadata.get('Title'))

        if not store_id or not business_name:
            return None

        properties = metadata.get('Properties') or None
        town, phone_number = self.__parse_properties(properties)
        raw_scraped_at = datetime.now(timezone.utc)
        formatted_scraped_at = raw_scraped_at.strftime('%Y-%m-%d %H:%M:%S %Z')

        return Store(
            store_id=store_id,
            business_name=business_name,
            town=town,
            phone_number=phone_number,
            scraped_at=formatted_scraped_at
        )
