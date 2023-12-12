





from requests import get
from bs4 import BeautifulSoup
import datetime

from .models import LicenseKey
from .exceptions import LicenseKeyNotFound, LicenseKeyExpired, LicenseKeyNotActive, SheetNotFound

class LicenseManager:
    """A license manager.

    Attributes
    ----------
    url_id : str
        The URL of the Google Sheets page containing the database.
    sheet_id : str
        The ID of the Google Sheets page containing the database.

    """

    def __init__(self, url_id : str, sheet_id : str = 0):
        self.url = "https://docs.google.com/spreadsheets/d/{0}/htmlview".format(url_id)
        self.sheet_id = sheet_id
    def get_license(self, key : str) -> LicenseKey:
        """Get a license key from the database.

        Parameters
        ----------
        key : str
            The license key to get.

        Returns
        -------
        LicenseKey
            The license key object.

        Raises
        ------
        LicenseKeyNotFound
            If the license key is not found in the database.
        LicenseKeyExpired
            If the license key is expired.
        LicenseKeyNotActive
            If the license key is not active.
        SheetNotFound
            If the sheet is not found in the database.

        """
        # Get the HTML from the Google Sheets page
        html = get(self.url).text
        # Parse the HTML
        soup = BeautifulSoup(html, 'html.parser')
        # Find the Sheet
        sheet = soup.find('div', attrs={'id': self.sheet_id})
        if sheet is None:
            raise SheetNotFound("Sheet not found in database.")
        # Find the table
        table = sheet.find('table', attrs={'class':'waffle'})
        # Get the tbody
        tbody = table.find('tbody')
        
        keys = {}
        for tr in tbody.find_all('tr')[1:]:
            td = tr.find_all('td')
            keys[td[0].text] = [td[1].text, td[2].text]


        if keys.get(key) is None:
            raise LicenseKeyNotFound("License key not found in database.")
        
        
        
        if keys[key][1] != "1":
            raise LicenseKeyNotActive("License key is not active.")
        
        if datetime.datetime.strptime(keys[key][0], '%m/%d/%Y') < datetime.datetime.now():
            raise LicenseKeyExpired("License key is expired.")
        
        return LicenseKey(key, keys[key][0], True if keys[key][1] == "1" else False)
    

        