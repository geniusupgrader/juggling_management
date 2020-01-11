from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Jugglingtricktable"),
        "icon": "octicon octicon-briefcase",
        "items": [
                                   {
              "type": "doctype",
              "name": "Jugglingtricks",
              "label": _("Jugglingtricks"),
              "description": _("Description of Jugglingtricks"),
            },
                    {
              "type": "doctype",
              "name": "Lists",
              "label": _("Lists"),
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
              "name": "Props",
              "label": _("Props"),
              "description": _("Description of Props"),
            }
        ]
      }
  ]