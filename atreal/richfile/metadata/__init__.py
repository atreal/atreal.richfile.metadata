from zope.i18nmessageid import MessageFactory
RichFileMetadataMessageFactory = MessageFactory('atreal.richfile.metadata')

from Products.Archetypes.utils import unique

from atreal.richfile.metadata.interfaces import IMetadata
from atreal.richfile.metadata.extractors_mimetypes import HACHOIR_MT
from atreal.richfile.metadata.extractors_mimetypes import EXIF_MT


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    try:
        from atreal.richfile.qualifier.registry import registerRFPlugin
    except:
        return
    
    supported_mimetypes = unique(HACHOIR_MT + EXIF_MT)
    
    registerRFPlugin(IMetadata, supported_mimetypes)
