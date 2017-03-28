"""
Module for parsing JSON files
"""

class JSONParser:
    """
    The base class for parsing JSON files
    """

    def __init__(self, path):
        """
        Constructor

        Args:
            self(JSONParser): the JSON parser
            path(Str): The file path to read JSON data from
        """
        self._path = path
        self._data = self._readfile()

    def getdata(self):
        """
        Returns the data associated with the JSON file of the JSON parser

        Args:
            self(JSONParser): the JSON parser

        Returns:
            Dict: A dictionary representation of the JSON data
        """
        return self._data

    def savedata(self, savedata=None):
        """
        Saves the input data to the JSON file of the JSON parser
        Saves the current data of the parser if no input data is given

        Args:
            self(JSONParser): the JSON parser
            savedata(Dict): the JSON data to be saved to file
        """
        if savedata is None:
            # TODO: save current class data to the JSON file at path
            pass
        else:
            # TODO: save the input data to the JSON file at path
            pass

    def _readfile(self):
        """
        Reads the data from the JSON file associated with the JSON parser

        Args:
            self(JSONParser): the JSON parser
        """
        # TODO: implement JSON file reading
        pass
