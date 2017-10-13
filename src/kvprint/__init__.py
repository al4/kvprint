"""
kvprint

A module for printing a list of key-values, aligned by separator

Example:

       foo: bar
longer-key: even longer value
       baz: boz
"""
import logging

logger = logging.getLogger(__name__)


def kvalign(data, max_width=None):
    """ Return a list of lines, with the keys left-padded to the length of
    the longest key or max_width, whichever is shorter.
    """
    try:
        longest_key = max([len(k) for k in data.keys()])
    except ValueError:
        logger.debug("Could not determine longest key length, probably empty")
        return []
    logger.debug('longest_key: {}'.format(longest_key))

    if max_width:
        column_width = longest_key if longest_key < max_width else max_width
    else:
        column_width = longest_key
    logger.debug('column_width: {}'.format(column_width))

    lines = []
    for key, value in data.items():
        lines.append([
            '{0:>{x}}'.format(str(key), x=column_width)[:column_width],
            value
        ])

    return lines


def kvstring(data, separator=': ', width=None):
    """ Return a string of key values aligned by separator

    :param data:
    :param separator:
    :param width:
    :return:
    """
    s = ""
    for l in kvalign(data, max_width=width):
        s += separator.join([str(v) for v in l])
        s += '\n'


def kvprint(data, separator=': ', width=None):
    """ Print a dictionary of key values aligned by separator

    :param data:
    :param separator:
    :param width:
    :return:
    """
    print(kvstring(data, separator=separator, width=width))


if __name__ == "__main__":
    kvprint({'foo': 'bar', 'longer key string': 123}, width=4)
