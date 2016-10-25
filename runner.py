import logging
import os
import inotify.adapters

from wrapper import wrapper

_DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(filename='wrapper.log', level=logging.INFO)
_LOGGER = logging.getLogger(__name__)

LOCK_FILE = '.lock'


def _configure_logging():
    _LOGGER.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()

    formatter = logging.Formatter(_DEFAULT_LOG_FORMAT)
    ch.setFormatter(formatter)

    _LOGGER.addHandler(ch)


def _main():
    i = inotify.adapters.Inotify()

    fp = b'/dir'

    # clean any locks that exist before init
    try:
        os.remove(fp + '/' + LOCK_FILE)
    except OSError:
        pass

    i.add_watch(os.getcwd() + '/' + fp)

    try:
        for event in i.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                if "IN_CREATE" in type_names:
                    _LOGGER.info("header=%s | fn=%s | MASK->NAMES=%s | wp=%s", header, filename, type_names, watch_path)
                    wrapper(filename, watch_path, LOCK_FILE)

    finally:
        i.remove_watch(fp)


if __name__ == '__main__':
    _configure_logging()
    _main()
