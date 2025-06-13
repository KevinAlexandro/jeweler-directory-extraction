import csv
import json
import os
from datetime import datetime
from crawled_data import CrawledData

class Writer:
    def __init__(self, crawled_data: CrawledData):
        """
        Initialize the Writer class with a CrawledData object.
        
        Args:
            crawled_data (CrawledData): The crawled data to be written to files.
        """
        self.crawled_data = crawled_data
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
            
        # Ensure the data directory exists
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        self.__write_to_csv()
        self.__write_to_json()
    
    def _get_filename(self, extension):
        """
        Generate a filename with timestamp.
        
        Args:
            extension (str): File extension (csv or json).
            
        Returns:
            str: The generated filename.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"jeweler_data_{timestamp}.{extension}"
    
    def _prepare_data_for_export(self):
        """
        Prepare the data for export by converting Store objects to dictionaries.
        
        Returns:
            list: List of store dictionaries.
        """
        stores_data = []
        for store in self.crawled_data._CrawledData__crawled_data['jeweler_stores']:
            stores_data.append(store.get_metadata())
        return stores_data
    
    def __write_to_csv(self):
        """
        Write the crawled data to a CSV file.
        
        Returns:
            str: The path to the created CSV file.
        """
        stores_data = self._prepare_data_for_export()
        
        if not stores_data:
            print("No data to write to CSV.")
            return None
        
        filename = self._get_filename('csv')
        filepath = os.path.join(self.data_dir, filename)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            # Get field names from the first store
            fieldnames = stores_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for store in stores_data:
                writer.writerow(store)
        
        print(f"Data successfully written to CSV file: {filepath}")
        return filepath
    
    def __write_to_json(self):
        """
        Write the crawled data to a JSON file.
        
        Returns:
            str: The path to the created JSON file.
        """
        stores_data = self._prepare_data_for_export()
        
        if not stores_data:
            print("No data to write to JSON.")
            return None
        
        filename = self._get_filename('json')
        filepath = os.path.join(self.data_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump({'jeweler_stores': stores_data}, jsonfile, indent=4)
        
        print(f"Data successfully written to JSON file: {filepath}")
        return filepath
