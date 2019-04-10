import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\n Would you like to see data for Chicago, New York or Washington? :')
    while True:
            if city in ('Chicago','New York','Washington'):
                break
            else:
                print ('\nWrong input. Enter a valid city!!!')
                return

    response = input('\nWould you like filter data by month, day, both or not at all? Type "none" for no time filter. :')

    if response == 'both':
        # TO DO: get user input for month (all, january, february, ... , june)
            month = input('\nWhich month? January, February, March, April, May or June?: ').title()
            while True:
                if month in ('January','February','March','April','May','June','Both'):
                    break
                else:
                    print ('\nWrong Month. Enter a valid month!!!')
                    return
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            key = input ('\nWhich day? Please type your response as an integer (e.g., 1=Sunday)').title()
            day_of_week = {'1':'Sunday','2':'Monday','3':'Tuesday','4':'Wednesday','5':'Thursday','6':'Friday','7':'Saturday'}
            while True:
                if key in day_of_week:
                    day = day_of_week.get(key)
                    break
                else:
                    print('\nEnter a no between 1 and 7')
                    return

    if response == 'month':
            day ='all'
        # TO DO: get user input for month (all, january, february, ... , june)
            month = input('\nWhich month? January, February, March, April, May or June?: ').title()
            while True:
                if month in ('January','February','March','April','May','June','Both'):
                    break
                else:
                    print ('\n Enter a valid month!!!')
                    return


    if response == 'day':
            month ='all'
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            key = input ('\nWhich day? Please type your response as an integer (e.g., 1=Sunday)').title()
            day_of_week = {'1':'Sunday','2':'Monday','3':'Tuesday','4':'Wednesday','5':'Thursday','6':'Friday','7':'Saturday'}
            while True:
                if key in day_of_week:
                    day = day_of_week.get(key)
                    break
                else:
                    print('\nEnter a no between 1 and 7')
                    return
    if response == 'none':
            month = 'all'
            day = 'all'


    print('-'*40)
    print("\n City Entered: {}".format(city))
    print("\n Month Entered: {}".format(month))
    print("\n Day of the week: {}".format(day))
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common month :', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most day of the week :', common_day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nMost Common Start Station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nMost Common End Station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    trip_data = df['Start Station'].astype(str) + "to" + df['End Station'].astype(str)
    trip_data.describe()
    common_combo = trip_data.describe()["top"]
    print('\nMost Frequent Combo of start station and end station trip :',common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('\nTotal travel time: ', total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('\nMean travel time: ', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('\nEach user type:\n',user_types)
    except KeyError as k:
        print('\n User Data Unavailable\n')

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Counts:\n',gender_count)
    except KeyError as exc:
        print('\nGender unavailable on data!!!\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print('\nEarliest Birth Year: ',earliest_birth)
        print('\nMost Recent Birth Year: ',recent_birth)
        print('\nMost Common Birth Year: ',common_birth)
    except KeyError as e:
        print('\nBirth Year Data Unavailable!!!\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    st=0
    choice = input('\n Do you want to see raw data? : (Y/N)').title()
    while choice == 'Y':
        df_slice = df.iloc[st:st+5]
        print(df_slice)
        st+=5
        choice = input('\n Do you want to see raw data? : (Y/N)').title()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
