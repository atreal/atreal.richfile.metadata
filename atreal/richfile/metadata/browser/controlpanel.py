from zope.interface import Interface
from zope.component import adapts
from zope.interface import implements
from zope.schema import TextLine, Choice, List, Bool
from zope.formlib import form

from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

from atreal.richfile.metadata import RichFileMetadataMessageFactory as _
from atreal.richfile.qualifier.common import RFControlPanel

from atreal.richfile.metadata.interfaces import IMetadataExtractor
from plone.app.controlpanel.form import ControlPanelForm


class IRichFileMetadataSchema(Interface):
    """ """

    rf_metadata_collapsed = Bool(
        title=_(u"label_rf_metadata_collapsed",
                default=u"Display collapsed ?"),
        description=_(u"help_rf_streaming_collapsed",
                      default=u"Do you want the plugin's display to be collapsed ?"
                     ),
        default=False)
    
    
    
class RichFileMetadataControlPanelAdapter(SchemaAdapterBase):
    """ """
    adapts(IPloneSiteRoot)
    implements(IRichFileMetadataSchema)
    
    rf_metadata_collapsed = ProxyFieldProperty(IRichFileMetadataSchema['rf_metadata_collapsed'])
    
    
    
class RichFileMetadataControlPanel(RFControlPanel):
    template = ZopeTwoPageTemplateFile('controlpanel.pt')
    form_fields = form.FormFields(IRichFileMetadataSchema)
    label = _("RichFileMetadata settings")
    description = _("RichFileMetadata settings for this site.")
    form_name = _("RichFileMetadata settings")
    plugin_iface = IMetadataExtractor
    supported_ifaces = ('atreal.richfile.metadata.interfaces.IMetadata',)
