import requests
class Fetch:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == requests.codes.ok:
            print 'INFO: Data successfully retrieved.'
	    return response.text
        else:
            print 'INFO: Error in fetching data. Response code: ' + str(response.status_code)
            return None
