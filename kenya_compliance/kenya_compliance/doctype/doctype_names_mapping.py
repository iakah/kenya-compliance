"""Maps doctype names defined and used in the app to variable names"""

from typing import Final

# Doctypes
COMMUNICATION_KEYS_DOCTYPE_NAME: Final[str] = "Bollex KRA eTims Communication Key"
SETTINGS_DOCTYPE_NAME: Final[str] = "Bollex KRA eTims Settings"
LAST_REQUEST_DATE_DOCTYPE_NAME: Final[str] = "Bollex KRA eTims Last Request Date"
ROUTES_TABLE_DOCTYPE_NAME: Final[str] = "Bollex KRA eTims Route Table"
ROUTES_TABLE_CHILD_DOCTYPE_NAME: Final[str] = "Bollex KRA eTims Route Table Item"

# Global Variables
SANDBOX_SERVER_URL: Final[str] = "https://etims-api-sbx.kra.go.ke/etims-api"
PRODUCTION_SERVER_URL: Final[str] = "https://etims-api.kra.go.ke/etims-api"
