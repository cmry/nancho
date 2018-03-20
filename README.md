# nanchō

This app only works for :penguin: using :snake: 2 or 3.

## Install

Nancho can be ran in the backgroud automatically as a service. However, as it needs access to the `dbus` operations on user-level, these needed to be added to `systemctl --user`. The instructions below explain how to set this up.

### Cloning the Repository

Clone the repository to `somedir` (where `somedir` is a directory name of your choosing).

```shell
cd /home/username/path/to/somedir
git clone https://github.com/cmry/nancho
```

From now on, we'll refer to the path to the script as `/home/user/path/to/somedir/nancho/nancho.py`. Please remember this `somedir` path, because you'll need it at more places in the set-up.

### Adding the `.service` File

Now set up a `systemd` file like so:

```shell
sudo vi /etc/systemd/user/nancho.service
```

And add the following text:

```
[Unit]
Description=Automute Music on Browser Audio
After=multi-user.target

[Service]
Type=idle
ExecStart=/bin/sh /home/yourusername/path/to/somedir/nancho/nancho.sh

[Install]
WantedBy=multi-user.target
```

**Note**: change the `/home/yourusername/path/to/somedir/` part to the correct one!

### Configuring the `.sh` Script

Now configure `nancho.sh` (in `/home/username/path/to/somedir/nancho/nancho.sh`) to match your username and the somedir directory. Make sure that the directory is absolute!

```shell
vi /home/yourusername/path/to/somedir/nancho/nancho.sh
```

And change the directory in the first line:

```shell
/usr/bin/python3 /home/yourusername/path/to/somedir/nancho/nancho.py --browser=Firefox --music=Spotify --poll_time=2 --pause
```

**If Python 2**: change the python3 part in `/usr/bin/python3` to either `python2` or `python`.

#### Arugments

Note that this uses default arguments for the code above (e.g. `--browser=Firefox`), for an overview and help see `python nancho.py -h`. Moreoever, `poll_time` is set to 2 seconds - if you'd like more responsive pausing and trade-off some system load, decrease this number. 

### Running it as a Service

After you set this all up can run the service with:

```shell
systemctl --user start nancho
```

And check for any errors with:

```shell
systemctl --user status nancho
```
