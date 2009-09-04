from zope.interface.interfaces import IInterface
from zope.component import queryUtility

from atreal.richfile.metadata.interfaces import IMetadataExtractor


def is_richfilemetadata_installed():
    """
    """
    return queryUtility(IInterface, name=u'atreal.richfile.metadata.IRichFileMetadataSite', default=False)

def extractMetadata(obj, event):
    """
    """
    if not is_richfilemetadata_installed():
        return
    print "Extracting metadatas for %s" % ('/'.join(obj.getPhysicalPath()))
    IMetadataExtractor(obj).process()

def cleanMetadata(obj, event):
    """
    """
    if not is_richfilemetadata_installed():
        return
    print "Clean metadata %s" % ('/'.join(obj.getPhysicalPath()))
    IMetadataExtractor(obj).cleanUp()
