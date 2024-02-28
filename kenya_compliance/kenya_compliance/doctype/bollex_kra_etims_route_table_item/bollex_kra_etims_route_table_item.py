# Copyright (c) 2024, Bollex Ltd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BollexKRAeTimsRouteTableItem(Document):
    """Route Table doctype child table"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = None

    def validate(self) -> None:
        """Validation Hook"""
        if self.url_path:
            if not self.url_path.startswith("/"):
                self.url_path = f"/{self.url_path}"
