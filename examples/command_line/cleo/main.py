# Author: Alejandro M. BERNARDIS
# Email alejandro.bernardis at gmail.com
# Created: 2019/11/12 07:39

import sys
from pathlib import Path
from cleo import Application, Command


class WalkCommand:
    """
    Recorre de forma recursiva un directorio específico.

    walk
        {path : Direcotrio a recorrer.}
        {--f|file : Mostrar sólo archivos.}
        {--d|dir : Mostrar sólo directorios.}
        {--p|pattern=? : Filtro de busqueda.}
    """
    def handle(self):
        path = Path(self.argument('path')).absolute()
        if path.exists():
            for x in path.rglob(self.option('pattern') or '*'):
                if (self.option('file') and not x.is_file()) \
                        or (self.option('dir') and not x.is_dir()):
                    continue
                self.line(str(x))


def run():
    app = Application()
    app.add(WalkCommand())
    app.run()


if __name__ == '__main__':
    sys.exit(run())
