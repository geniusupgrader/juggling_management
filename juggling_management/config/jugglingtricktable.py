from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Juggling_management"),
        "icon": "octicon octicon-briefcase",
        "items": [
                                   {
              "type": "doctype",
              "name": "Jugglingtrick",
              "label": _("Jugglingtrick"),
              "description": _("Description of Jugglingtricks"),
            },
                    {
              "type": "doctype",
              "name": "Routine",
              "label": _("Routine"),
              "description": _("Description of Lists"),
            },
                                   {
              "type": "doctype",
              "name": "Category",
              "label": _("Category"),
              "description": _("Description of Categories"),
            },
                                   {
              "type": "doctype",
              "name": "Prop",
              "label": _("Prop"),
              "description": _("Description of Props"),
            }
        ]
      }
  ]
