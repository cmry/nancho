# nanchō

This app only works for :penguin: using :snake: 3.

## Install

Clone the repository to `somedir` (i.e. the path to the script is now `somedir/nancho/nancho.py`), and set up a `systemd` file like so:

```shell
sudo vi /etc/systemd/system/nancho.service
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

> Note that this uses default arguments for the code, for an overview and help see `python nancho.py -h`. Moreoever, `poll_time` is set to 2 seconds - if you'd like more responsive pausing and trade-off some system load, decrease this number.

Now configure `nancho.sh` (in `somedir/nancho/nancho.sh`) to match your username and the somedir directory. Make sure that the directory is absolute!
