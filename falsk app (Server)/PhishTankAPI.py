"""
Simple phishtank api.
"""

__docformat__ = 'restructuredtext'
__author__ = "Samuel Cleveland"
__version__ = '1.0.0'
__license__ = 'MIT License'

from datetime import datetime
from datetime import timedelta
import requests
import base64



class PhishTankError(Exception):
    """
    Exception for PhishTank errors.
    """
    pass
    
class PhishTankAPILimitExceeded(Exception):
    """
    Exception for exceeding the PhishTank API limit.
    """
    pass

class PhishTankAPILimitReached(Exception):
    """
    Exception when the PhishTank API limit is reached.
    """
    pass

class Result():
    """
    Result sent back from PhishTank.
    """

    def __init__(self, response):
        """
        Initialize Result object.
        :Parameters:
           - `response`: actual json response from the service
        """
        
        self.url = response.get('url', None)
        self.in_database = response.get('in_database', None)
        self.phish_id = response.get('phish_id', None)
        self.phish_detail_page = response.get('phish_detail_page', None)
        self.verified = response.get('verified', None)
        self.verified_at = response.get('verified_at', None)
        if self.verified_at:
            self.verified_at = self.__format_date(self.verified_at)
        self.valid = response.get('valid', None)
        self.submitted_at = response.get('submitted_at', None)
        if self.submitted_at:
            self.submitted_at = self.__format_date(self.submitted_at)

    def __format_date(self, date_str):
        """
        Format a date string into a datetime object.
        :Parameters:
           - `date_str`: the date string in %Y-%m-%dT%H:%M:%S+00:00 format.
        """
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S+00:00')

    def __phish(self):
        """
        Returns True if the URL checked is known to be a phish, False if not.
        """
        if self.valid:
            return True
        return False

    def __repr__(self):
        """
        Representation of Result object.
        """
        return "<Result: url=%s, phish=%s>" % (self.url, self.__phish())

    def __eq__(self, other):
        """
        Checks to see if this instance is the same as another.
        :Parameters:
           - `other`: The other instance to look at.
        """
        for key in self.__slots__:
            try:
                if getattr(self, key) != getattr(other, key):
                    raise KeyError()
            except:
                return False
        return True


class PhishTank():
    """
    PhishTank abstraction class.
    """

    __apikey = ''
    _requests_available = 200
    _requests_made = 0
    _time_to_next_request = datetime.utcnow()
    _request_interval = 60

    def __init__(self, api_url='http://checkurl.phishtank.com/checkurl/', apikey='922bb8fdac4c98eb1351cf3ad4b86ddc565412e593f4106633aed223560fcb8e'):
        """
        Create an instance of the API caller.
        :Parameters:
           - `apikey`: optional apikey to use in calls
        """
        self.__apikey = apikey
        self._api_url = api_url
        
    def requests_left(self):
        """Check if there are API requests available, returns True if there are, False if not."""
        if (self._time_to_next_request >= datetime.utcnow()):
            return False
            
        if (self._requests_available - self._requests_made) > 0:
            return True
        else:
            return False
            
    def time_to_wait(self):
        """Update the time to wait until next request allowed."""
        self._time_to_next_request = datetime.utcnow() + timedelta(seconds=self._request_interval)

    def check(self, url):
        """
        Check a URL.
        :Parameters:
           - `url`: url to check agianst the PhishTank database
        """
        post_data = {
            'url': base64.b64encode(url.encode("utf-8")),
            'format': 'json',
            'app_key': self.__apikey,
        }
    
        response = requests.post(self._api_url, data=post_data)
        self._requests_made = int(response.headers.get('X-Request-Count', 0))
        self._requests_available = int(response.headers.get('X-Request-Limit', 50))
        self._request_interval = int(response.headers.get("X-Request-Limit-Interval", 300)[:-8])
        
    
        if response.status_code == 509:
            raise PhishTankAPILimitExceeded(self._request_interval)
                
        data = response.json()

        if 'errortext' in data.keys():
            raise PhishTankError(data['errortext'])
        return Result(data['results'])