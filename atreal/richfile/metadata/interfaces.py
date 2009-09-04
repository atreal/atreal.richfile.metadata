from zope.interface import Interface

class IRichFileMetadataLayer(Interface):
    """ Marker interface that defines a Zope 3 browser layer.
    """

class IRichFileMetadataSite(Interface):
    """ Marker interface for sites with this product installed.
    """ 

class IMetadata(Interface):
    """
    """
    
class IMetadataExtractor(Interface):
    """
    """

class IExtractorWrapper(Interface):
    """ Interface for an extractor's wrapper """
    
    def available(self):
        """ True if the matching lib/binary is available"""

    def bestMimetypes(self):
        """ Return the more effective mimetypes list supported by the extractor """
    
    def supportedMimetypes(self):
        """ Return the mimetypes list supported by the extractor """
    
    def extract(self, myfile):
        """ Return a mapping filled with the file metadatas """
