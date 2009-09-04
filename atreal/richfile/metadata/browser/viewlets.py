from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.annotation.interfaces import IAnnotations

from atreal.richfile.qualifier.browser.viewlets import RichfileViewlet
from atreal.richfile.metadata.browser.controlpanel import IRichFileMetadataSchema
from atreal.richfile.metadata.interfaces import IMetadata
from atreal.richfile.metadata.interfaces import IMetadataExtractor
from atreal.richfile.metadata import RichFileMetadataMessageFactory as _

class MetadataViewlet(RichfileViewlet):
    """ """
    
    marker_interface = IMetadata
    plugin_interface = IMetadataExtractor
    plugin_id = 'metadata'
    plugin_title = 'Metadata'
    controlpanel_interface = IRichFileMetadataSchema


    @property
    def metadata(self):
        """ """
        info = IMetadataExtractor(self.context).info
        if info.has_key('metadata'):
            return info['metadata']
        else:
            return

    
    index = ViewPageTemplateFile("viewlet.pt")
