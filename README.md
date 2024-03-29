Octoprint modified by Shohei Aoki

# How to use websocket pub-sub

Run static HTTP server
```sh
$ cd management-console
$ python -m SimpleHTTPServer 8000

open localhost:8000 to see the management console
```
Run websocket server(this will run on Local Garage server)
```sh
$ cd management-console
$ node server.js # -> start websocet server on localhost:8080
```
Run two or three Octoprint
```sh
$ ./run
```
Visit OctoPrint and select local garage tab.

Input place and printer, then push the button.
![octo](octo.png)


You will see the management console automatically updated.
![printer](printers.png)


# How to use event machine (EM) 

I added mozpi package to put websocket listener wherever (Event Machine)

```python
from mozpi import Mozpi 
import threading

m = Mozpi("ws://localhost:8080") #anywhere ws server
t = threading.Thread(target=m.start())
t.start()
# your logic continues through
```
### em-websocket server for testing
```sh
$ ruby em-websocket-server/server.rb
```

src/octoprint/mozpi/client.py
```python
    def on_message(self,ws,message):
        print message
        #Play with message for anything you want to!
```

OctoPrint
=========

[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=foosel&url=https://github.com/foosel/OctoPrint&title=OctoPrint&language=&tags=github&category=software)

OctoPrint provides a responsive web interface for controlling a 3D printer (RepRap, Ultimaker, ...). It is Free Software
and released under the [GNU Affero General Public License V3](http://www.gnu.org/licenses/agpl.html).

Its website can be found at [octoprint.org](http://octoprint.org).

Contributing
------------

Please see the project's [Contribution Guidelines](https://github.com/foosel/OctoPrint/blob/master/CONTRIBUTING.md).

Installation
------------

Installation instructions for installing from source for different operating systems can be found [on the wiki](https://github.com/foosel/OctoPrint/wiki#assorted-guides).

If you want to run OctoPrint on a Raspberry Pi you might want to take a look at [OctoPi](https://github.com/guysoft/OctoPi)
which is a custom SD card image that includes OctoPrint plus dependencies.

Dependencies
------------

OctoPrint depends on a couple of python modules to do its job. Those are automatically installed when installing
OctoPrint via `setup.py`:

    python setup.py install

You should also do this after pulling from the repository, since the dependencies might have changed.

OctoPrint currently only supports Python 2.7.

Usage
-----

From the source directory you can start the server via

    ./run

By default it binds to all interfaces on port 5000 (so pointing your browser to `http://127.0.0.1:5000`
will do the trick). If you want to change that, use the additional command line parameters `host` and `port`,
which accept the host ip to bind to and the numeric port number respectively. If for example you want the server
to only listen on the local interface on port 8080, the command line would be

    ./run --host=127.0.0.1 --port=8080

Alternatively, the host and port on which to bind can be defined via the configuration.

If you want to run OctoPrint as a daemon (only supported on Linux), use

    ./run --daemon {start|stop|restart} [--pid PIDFILE]

If you do not supply a custom pidfile location via `--pid PIDFILE`, it will be created at `/tmp/octoprint.pid`.

You can also specify the configfile or the base directory (for basing off the `uploads`, `timelapse` and `logs` folders),
e.g.:

    ./run --config /path/to/another/config.yaml --basedir /path/to/my/basedir

See `run --help` for further information.

Running the `setup.py` script also installs the `octoprint` startup script in your Python installation's scripts folder
(which depending on whether you installed OctoPrint globally or into a virtual env will be on your `PATH` or not). The
examples above also work with that startup script as it excepts the same parameters as `run`.


Configuration
-------------

If not specified via the commandline, the configfile `config.yaml` for OctoPrint is expected in the settings folder,
which is located at `~/.octoprint` on Linux, at `%APPDATA%/OctoPrint` on Windows and
at `~/Library/Application Support/OctoPrint` on MacOS.

A comprehensive overview of all available configuration settings can be found
[on the wiki](https://github.com/foosel/OctoPrint/wiki/Configuration).
