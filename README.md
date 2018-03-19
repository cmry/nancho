# nanchō

This app only works for :penguin: using Python 3.

## Install

Clone the repository to `somedir` (i.e. the path to the script is now `somedir/nancho/nancho.py`), and set up a `systemd` file like so:

```shell
sudo vi /lib/systemd/system/nancho.service
```

And add the following text:

```
[Unit]
Description=Automute Music on Browser
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /path/to/somedir/nancho/nancho.py --browser=Firefox --music=Spotify --poll_time=2 --pause

[Install]
WantedBy=multi-user.target
```

Note that this uses default arguments for the code, for an overview and help see `python nancho.py -h`. Moreoever, `poll_time` is set to 2 seconds - if you'd like more responsive pausing and trade-off some system load, decrease this number.
