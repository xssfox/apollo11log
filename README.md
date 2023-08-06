### Install
```sh
sudo pip3 install apollo11log #to install system wide
```

### Run as a CLI app
```
$ apollo11log
[CDR] 00 00:00:04 Roger. Clock.
[CDR] 00 00:00:13 Roger. We got a roll program.
[CMP] 00 00:00:15 Roger. Roll.
[CDR] 00 00:00:34 Roll's complete an
```

### Run as a systemd service

Create a unit file - such as `/etc/systemd/system/apollo11.service`
with the contents like
```
[Unit]
Description=apollo11
After=syslog.target

[Service]
ExecStart=/usr/local/bin/apollo11log
Restart=always
RestartSec=120
SyslogIdentifier=apollo11

[Install]
WantedBy=multi-user.target
```

The enable and start the service
```
sudo systemctl enable apollo11.service
sudo systemctl start apollo11.service
```

### Watch the logs
```
journalctl -u apollo11 -f -n
```