import pandas as pd

date = ['1950-8-31',
'1950-9-5',
'1950-10-18',
'1950-10-21',
'1951-5-18',
'1951-10-2',
'1952-2-3',
'1952-8-30',
'1953-6-6',
'1953-8-29',
'1953-9-20',
'1953-9-26',
'1953-10-9',
'1955-8-21',
'1956-7-6',
'1956-9-24',
'1956-10-15',
'1957-6-8',
'1957-9-8',
'1958-9-4',
'1959-6-18',
'1959-10-8',
'1959-10-18',
'1960-7-29',
'1960-9-10',
'1960-9-15',
'1960-9-23',
'1961-9-11',
'1961-10-29',
'1962-8-26',
'1963-10-21',
'1964-6-6',
'1964-8-27',
'1964-9-10',
'1964-9-20',
'1964-10-5',
'1964-10-14',
'1965-6-15',
'1965-9-8',
'1965-9-30',
'1966-6-9',
'1966-6-30',
'1966-7-24',
'1966-10-4',
'1968-6-4',
'1968-6-18',
'1968-7-5',
'1968-8-10',
'1968-8-28',
'1968-9-26',
'1968-10-19',
'1969-6-9',
'1969-8-18',
'1969-8-29',
'1969-9-7',
'1969-9-21',
'1969-10-1',
'1969-10-2',
'1969-10-21',
'1970-5-25',
'1970-7-22',
'1970-8-6',
'1970-9-13',
'1970-9-27',
'1971-8-10',
'1971-8-13',
'1971-8-29',
'1971-9-1',
'1971-9-16',
'1971-10-13',
'1972-5-28',
'1972-6-19',
'1972-9-5',
'1973-6-7',
'1973-6-23',
'1973-9-3',
'1973-9-25',
'1974-6-25',
'1974-9-8',
'1974-9-27',
'1974-10-7',
'1975-6-27',
'1975-7-29',
'1975-9-23',
'1975-10-1',
'1975-10-16',
'1976-5-23',
'1976-6-11',
'1976-8-19',
'1976-9-13',
'1977-8-27',
'1977-9-5',
'1978-6-22',
'1979-7-11',
'1979-9-3',
'1979-9-12',
'1979-9-24',
'1980-8-7',
'1980-11-18',
'1981-8-17',
'1982-6-18',
'1982-9-11',
'1983-8-28',
'1984-9-9',
'1984-9-27',
'1984-10-26',
'1985-7-23',
'1985-8-15',
'1985-10-10',
'1985-11-21',
'1986-6-26',
'1986-8-13',
'1987-8-14',
'1987-9-7',
'1987-10-12',
'1987-11-4',
'1988-5-30',
'1988-8-4',
'1988-8-13',
'1988-8-23',
'1988-9-4',
'1988-9-10',
'1988-9-13',
'1988-11-23',
'1989-9-22',
'1990-5-25',
'1990-10-9',
'1990-10-12',
'1991-6-30',
'1991-10-16',
'1992-6-25',
'1992-8-24',
'1992-9-29',
'1993-6-1',
'1994-7-3',
'1994-8-15',
'1994-10-2',
'1994-11-16',
'1995-6-5',
'1995-7-27',
'1995-8-2',
'1995-8-23',
'1995-10-4',
'1996-7-11',
'1996-9-2',
'1996-10-8',
'1996-10-18',
'1997-7-19',
'1998-9-3',
'1998-9-20',
'1998-9-25',
'1998-11-5',
'1999-8-29',
'1999-9-15',
'1999-9-21',
'1999-10-15',
'2000-8-23',
'2000-9-9',
'2000-9-18',
'2000-9-22',
'2000-10-3',
'2001-6-12',
'2001-8-6',
'2001-9-14',
'2001-11-5',
'2002-7-13',
'2002-8-4',
'2002-9-4',
'2002-9-14',
'2002-9-26',
'2002-10-3',
'2002-10-11',
'2003-4-20',
'2003-6-30',
'2003-7-25',
'2003-8-14',
'2003-8-30',
'2003-9-6',
'2003-9-13',
'2004-8-12',
'2004-8-13',
'2004-9-5',
'2004-9-13',
'2004-9-16',
'2004-10-10',
'2005-6-11',
'2005-7-6',
'2005-7-10',
'2005-8-25',
'2005-9-12',
'2005-9-20',
'2005-10-5',
'2005-10-24',
'2006-6-13',
'2006-8-30',
'2007-5-9',
'2007-6-2',
'2007-8-23',
'2007-9-8',
'2007-9-13',
'2007-9-22',
'2007-10-31',
'2007-12-13',
'2008-7-16',
'2008-7-22',
'2008-8-18',
'2008-8-31',
'2008-9-2',
'2009-8-16',
'2009-8-21',
'2009-11-9',
'2010-6-30',
'2010-7-23',
'2010-8-10',
'2010-8-31',
'2010-9-29',
'2011-7-18',
'2011-8-25',
'2011-9-3',
'2011-10-28',
'2011-11-9',
'2012-5-28',
'2012-6-23',
'2012-8-25',
'2012-10-25',
'2015-8-30',
'2015-10-1',
'2016-6-6',
'2016-9-1',
'2016-9-14',
'2016-10-7',
'2017-6-21',
'2017-7-31',
'2017-9-10',
'2017-10-29']


print(type(date))

pd.to_datetime(date)

print(type(date))