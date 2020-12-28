from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Juggling Management"),
        "icon": "octicon octicon-briefcase",
        "items": [
                                   {
              "type": "doctype",
              "name": "jugglingtrick_juggling_management",
              "label": _("Jugglingtrick"),
              "description": _("Description of Jugglingtricks"),
            },
                    {
              "type": "doctype",
              "name": "routine_juggling_management",
              "label": _("Routine"),
              "description": _("Description of Lists"),
            },
                                   {
              "type": "doctype",
              "name": "category_juggling_management",
              "label": _("Category"),
              "description": _("Description of Categories"),
            },
                                   {
              "type": "doctype",
              "name": "prop_juggling_management",
              "label": _("Prop"),
              "description": _("Description of Props"),
            }
        ]
      }
  ]
