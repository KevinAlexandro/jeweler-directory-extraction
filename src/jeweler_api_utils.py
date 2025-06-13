# Scrape data from all 177 paginated results.
# Collect the following data fields for each listed business:
# Business Name
# Town
# Phone Number
# Compile the data into a clean, structured Excel spreadsheet (.xlsx or .csv).
# Ensure no duplicates and data is aligned correctly in rows/columns.
# Optional but helpful: include a timestamp of when the data was scraped.

from store import Store
from datetime import datetime, timezone


class JewelerAPIUtils:
    @staticmethod
    def __get_business_name(name: str):

        if not name or not isinstance(name, str):
            return None

        return name

    @staticmethod
    def __get_store_id(store_id: str):

        if not store_id or not isinstance(store_id, str):
            return None

        return store_id

    @staticmethod
    def __parse_properties(properties: dict):

        if not properties:
            return None

        town = properties.get('Town/City')
        phone_number = properties.get('Phone number')

        return town, phone_number

    def get_store_data(self, metadata: dict):
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
