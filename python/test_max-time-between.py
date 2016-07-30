import pytest
import arrow

from max_time_between import max_time_between


def test_no_timestamps_returns_none():
    expected = None
    actual = max_time_between([])

    assert expected == actual


def test_list_with_one_or_more_invalid_dates_raises():
    with pytest.raises(arrow.parser.ParserError):
        max_time_between([
            '2015-01-01 01:01:',
            ])


def test_simple_pair_returns_correct_difference():
    expected = (60, '2016-01-01 01:01:01', '2016-01-01 02:01:01')
    actual = max_time_between([
        '2016-01-01 01:01:01',
        '2016-01-01 02:01:01',
        ])
    assert expected == actual


def test_several_pairs_returns_correct_difference():
    expected = (120, '2016-01-01 07:01:01', '2016-01-01 09:01:01')
    actual = max_time_between([
        '2016-01-01 06:01:01',
        '2016-01-01 07:01:01',
        '2016-01-01 09:01:01',
        '2016-01-01 10:01:01',
        '2016-01-01 11:01:01',
        '2016-01-01 12:01:01',
        ])
    assert expected == actual


def test_several_pairs_returns_correct_difference():
    expected = (50, '2016-01-01 23:11:01', '2016-01-02 00:01:01')
    actual = max_time_between([
        '2016-01-01 23:07:01',
        '2016-01-01 23:08:01',
        '2016-01-01 23:09:01',
        '2016-01-01 23:10:01',
        '2016-01-01 23:11:01',
        '2016-01-02 00:01:01',
        ])
    assert expected == actual
