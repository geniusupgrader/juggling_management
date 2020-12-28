from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Juggling Management"),
        "items": [
                                   {
              "type": "doctype",
              "name": "Jugglingtrick_juggling_management",
              "label": _("Jugglingtrick"),
              "description": _("Description of Jugglingtricks"),
            },
                    {
              "type": "doctype",
              "name": "Routine_juggling_management",
              "label": _("Routine"),
              "description": _("Description of Lists"),
            },
                                   {
              "type": "doctype",
              "name": "Category_juggling_management",
              "label": _("Category"),
              "description": _("Description of Categories"),
            },
                                   {
              "type": "doctype",
              "name": "Prop_juggling_management",
              "label": _("Prop"),
              "description": _("Description of Props"),
            }
        ]
      }
  ]
