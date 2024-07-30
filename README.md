


# Bashrc
```bash

alias app='cd ~/pymahex-scaler/'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias kk='killall python'
alias ls='ls --color=auto'
alias run='python ~/pymahex-scaler/main.py'
alias web='python ~/pymahex-scaler/web.py'

killall python
cd ~/pymahex-scaler/
nohup python ~/pymahex-scaler/web.py &
python ~/pymahex-scaler/main.py

```


# Wifi
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf   

```bash
  network={
   ssid="Rahkar-2.4GHz"
   psk="RSA@#4410?"
   priority=4
  scan_ssid=1
  }
```

/boot/firmware/config.txt   


