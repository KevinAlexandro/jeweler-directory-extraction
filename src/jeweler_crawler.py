from jeweler_api import JewelerAPI
from crawled_data import CrawledData
from jeweler_api_utils import JewelerAPIUtils
from writer import Writer


class JewelerCrawler:
    """
    A class to crawl jeweler store data from the NAJ API.

    This class coordinates the process of fetching store data from the API,
    processing it, and writing it to files.

    # TODO: Consider separating the data crawling and writing functionality
    # to make the class more testable and follow the single responsibility principle.
    """
    def __init__(self):
        """
        Initialize the crawler and start the crawling process.

        This constructor initializes all necessary components and immediately
        starts the crawling process, then writes the results to files.
        """
        self.__crawled_data = CrawledData()
        self.__api = JewelerAPI()
        self.__api_utils = JewelerAPIUtils()
        self.__run()
        self.__writer = Writer(self.__crawled_data)

    def __get_all_stores(self):
        """
        Fetch all stores from the API and add them to the crawled data.

        Raises:
            Exception: If no response is received from the API.
        """
        response = self.__api.get_stores()

        if not response:
            raise Exception('No response from webpage.')

        # parse response
        for store in response:
            self.__crawled_data.add_store(self.__api_utils.get_store_data(store))

    def __run(self):
        """
        Run the crawling process by fetching all stores.
        """
        self.__get_all_stores()


if __name__ == '__main__':
    JewelerCrawler()
