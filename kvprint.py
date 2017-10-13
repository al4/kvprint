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


def kvprint(data, separator=': '):
    """ Print a dictionary of key values aligned by separator
    """
    longest_key = max([len(k) for k in data.keys()])
    logger.debug('longest_key: {}'.format(longest_key))

    lines = []
    for key, value in data.items():
        print('{0:>{x}}'.format('foo', x=1))
        print('key: {}'.format(key))
        print('value: {}'.format(value))

        lines.append([
            '{0:>{x}}'.format(key, x=longest_key),
            value
        ])

    for l in lines:
        print(separator.join([str(v) for v in l]))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    kvprint({'foo': 'bar', 'ilohsdgudlfhg': 123})
