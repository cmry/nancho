# nanchō

This app only works for :penguin: using :snake: 2 or 3.

## Install

Clone the repository to `somedir` (i.e. the path to the script is now `somedir/nancho/nancho.py`), and set up a `systemd` file like so:

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
ExecStart=/bin/sh /path/to/somedir/nancho/nancho.sh

[Install]
WantedBy=multi-user.target
```

And change the `/path/to/somedir` part to the correct one.

Now configure `nancho.sh` (in `somedir/nancho/nancho.sh`) to match your username and the somedir directory. Make sure that the directory is absolute!

```shell
vi /home/yourusername/path/to/somedir/nancho/nancho.sh
```

And change the directory in the first line:

```shell
/usr/bin/python3 /home/yourusername/path/to/somedir/nancho/nancho.py --browser=Firefox --music=Spotify --poll_time=2 --pause
```

> Note that this uses default arguments for the code, for an overview and help see `python nancho.py -h`. Moreoever, `poll_time` is set to 2 seconds - if you'd like more responsive pausing and trade-off some system load, decrease this number. **If Python 2**: change the python3 part in `/usr/bin/python3` to either python2 or python.

After you can run the service with:

```
systemctl --user start nancho
```
