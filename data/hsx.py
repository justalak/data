import pandas as pd
from datetime import time
from itertools import chain
from pytz import timezone
from trading_calendars import register_calendar, TradingCalendar

from pandas.tseries.holiday import Holiday
from trading_calendars.trading_calendar import HolidayCalendar


class HoSECalendar(TradingCalendar):
    name = 'HSX'

    tz = timezone('Asia/Ho_Chi_Minh')

    open_times = (
        (None, time(9, 1)),
    )

    close_times = (
        (None, time(14, 45)),
    )

    @property
    def regular_holidays(self):
        return HolidayCalendar([
            Holiday("New Year's Day", month=1, day=1),
            Holiday("Victory Day", month=4, day=30),
            Holiday("Labor Day", month=5, day=1),
            Holiday("Independence Day", month=9, day=2),
        ])

    @property
    def adhoc_holidays(self):
        return list(chain(
            pd.to_datetime([
                '2020-04-02', #2020
                '2020-01-29',
                '2020-01-28',
                '2020-01-27',
                '2020-01-24',
                '2020-01-23',
                '2019-04-29', # 2019
                '2019-04-15',
                '2019-02-08',
                '2019-02-07',
                '2019-02-06',
                '2019-02-05',
                '2019-02-04',
                '2018-12-31', # 2018
                '2018-09-03',
                '2018-04-25',
                '2018-02-20',
                '2018-02-19',
                '2018-02-16',
                '2018-02-15',
                '2018-02-14',
                '2018-01-24',
                '2018-01-23',
                '2017-09-04', # 2017
                '2017-05-02',
                '2017-04-06',
                '2017-02-01',
                '2017-01-31',
                '2017-01-30',
                '2017-01-27',
                '2017-01-26',
                '2017-01-02',
                '2016-05-03', # 2016
                '2016-05-02',
                '2016-04-18',
                '2016-02-12',
                '2016-02-11',
                '2016-02-10',
                '2016-02-09',
                '2016-02-08',
                '2015-04-29', # 2015
                '2015-04-28',
                '2015-02-23',
                '2015-02-20',
                '2015-02-19',
                '2015-02-18',
                '2015-02-17',
                '2015-02-16',
                '2015-01-02',
                '2014-09-01', # 2014
                '2014-05-02',
                '2014-04-09',
                '2014-02-05',
                '2014-02-04',
                '2014-02-03',
                '2014-01-31',
                '2014-01-30',
                '2014-01-29',
                '2014-01-28',
                '2013-04-29', # 2013
                '2013-04-19',
                '2013-02-15',
                '2013-02-14',
                '2013-02-13',
                '2013-02-12',
                '2013-02-11',
                '2012-12-31', # 2012
                '2012-09-03',
                '2012-04-02',
                '2012-01-27',
                '2012-01-26',
                '2012-01-25',
                '2012-01-24',
                '2012-01-23',
                '2012-01-02',
                '2011-05-03', # 2011
                '2011-05-02',
                '2011-04-12',
                '2011-04-11',
                '2011-02-07',
                '2011-02-04',
                '2011-02-03',
                '2011-02-02',
                '2011-02-01',
                '2011-01-31',
                '2011-01-03',
                '2010-09-03', # 2010
                '2010-05-03',
                '2010-04-23',
                '2010-02-19',
                '2010-02-18',
                '2010-02-17',
                '2010-02-16',
                '2010-02-15',
                '2009-04-06', # 2009
                '2009-01-30',
                '2009-01-29',
                '2009-01-28',
                '2009-01-27',
                '2009-01-26',
                '2008-09-01', # 2008
                '2008-05-29',
                '2008-05-28',
                '2008-05-27',
                '2008-05-02',
                '2008-04-15',
                '2008-04-14',
                '2008-02-11',
                '2008-02-08',
                '2008-02-07',
                '2008-02-06',
                '2008-02-05',
                '2008-02-04',
                '2007-12-31', # 2007
                '2007-09-03',
                '2007-04-27',
                '2007-04-26',
                '2007-02-23',
                '2007-02-22',
                '2007-02-21',
                '2007-02-20',
                '2007-02-19',
                '2007-02-16',
                '2006-09-04', # 2006
                '2006-05-02',
                '2006-02-03',
                '2006-02-02',
                '2006-02-01',
                '2006-01-31',
                '2006-01-30',
                '2006-01-16',
                '2006-01-02',
                '2005-05-03', # 2005
                '2005-05-02',
                '2005-02-11',
                '2005-02-10',
                '2005-02-09',
                '2005-02-08',
                '2005-02-07',
                '2005-01-03',
                '2004-09-03', # 2004
                '2004-05-03',
                '2004-01-26',
                '2004-01-23',
                '2004-01-22',
                '2004-01-21',
                '2004-01-20',
                '2004-01-19',
                '2004-01-02',
            ]),
        ))


register_calendar('HSX', HoSECalendar(), True)
