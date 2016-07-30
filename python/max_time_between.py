import arrow
import toolz


def max_time_between(oldest_to_most_recent=None):
    """Return the timestamp pairs with the most minutes between each timestamp."""
    if oldest_to_most_recent:
        dates = [arrow.get(date) for date in oldest_to_most_recent]
        return _get_minutes(dates)
    else:
        return None


def _get_minutes(dates):
    max_ts_diff = None
    for ts1, ts2 in toolz.itertoolz.sliding_window(2, dates):
        ts_diff = abs(ts2-ts1).seconds / 60
        if not max_ts_diff or ts_diff > max_ts_diff[0]:
            max_ts_diff = (
                ts_diff,
                ts1.format('YYYY-MM-DD HH:mm:ss'),
                ts2.format('YYYY-MM-DD HH:mm:ss'),
            )
        print(ts1,ts2,ts_diff)
    return max_ts_diff
