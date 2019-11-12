# Author: Alejandro M. BERNARDIS
# Email alejandro.bernardis at gmail.com
# Created: 2019/11/12 07:39

import sys
from pathlib import Path
from docopt import docopt


class WalkCommand:
    """
    Recorre de forma recursiva un directorio específico.

    usage:
        walk [-f|-d] [options] <path>

    Argumentos Opcionales:
        -f, --file                   Mostrar sólo archivos.
        -d, --dir                    Mostrar sólo directorios.
        -p VALUE, --pattern=VALUE    Filtro de busqueda. [default: *]
    """

    def __init__(self, argv=None, **kwargs):
        kwargs.setdefault('options_first', True)
        self.options = docopt(self.__doc__, argv, **kwargs)

    def execute(self, options=None, **kwargs):
        if options is None:
            options = self.options
        path = Path(options.get('<path>', '.')).absolute()
        if path.exists():
            for x in path.rglob(options.get('--pattern', '*')):
                if (options.get('--file', False) and not x.is_file()) \
                        or (options.get('--dir', False) and not x.is_dir()):
                    continue
                print(x)


def run():
    cmd = WalkCommand()
    cmd.execute()


if __name__ == '__main__':
    sys.exit(run())
