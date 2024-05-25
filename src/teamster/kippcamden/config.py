import pendulum

from teamster.core.utils.classes import FiscalYear

CODE_LOCATION = "kippcamden"
LOCAL_TIMEZONE = pendulum.timezone("America/New_York")
CURRENT_FISCAL_YEAR = FiscalYear(datetime=pendulum.today(LOCAL_TIMEZONE), start_month=7)
