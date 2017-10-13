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
    longest_key = max([len(k) for k in data.keys()])
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


def kvprint(data, separator=': ', width=None):
    """ Print a dictionary of key values aligned by separator
    """
    for l in kvalign(data, max_width=width):
        print(separator.join([str(v) for v in l]))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    kvprint({'foo': 'bar', 'longer key string': 123}, width=4)
