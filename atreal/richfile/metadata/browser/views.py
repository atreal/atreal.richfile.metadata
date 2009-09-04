from zope.interface import implements
from Products.Five  import BrowserView

from zope.interface import implements
from kss.core import KSSView, kssaction

from Products.Archetypes.BaseObject import Wrapper

from atreal.richfile.metadata import RichFileMetadataMessageFactory as _
from atreal.richfile.metadata.interfaces import IMetadataExtractor
from atreal.richfile.qualifier.common import RFView
from atreal.richfile.qualifier.interfaces import IRFView


class RFMetadataView(RFView):
    
    #implements(IRFView)

    plugin_interface = IMetadataExtractor
    kss_id = 'metadata'
    viewlet_name = 'atreal.richfile.metadata.viewlet'
    update_message = _('The metadatas have been updated.')
    active_message = _('Metadatas activated.')
    unactive_message = _('Metadatas un-activated.')    
