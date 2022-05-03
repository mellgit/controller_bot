# controller_bot

for help selenium

* Chromedriver - https://chromedriver.chromium.org/downloads
* instraction - https://chromedriver.chromium.org/getting-started

работа со звуком - https://ru.stackoverflow.com/questions/773188

сделать меню для команд - https://ru.stackoverflow.com/questions/1345315


Создать юнит и bash скрипт, после добавить права для них
```
sudo chmod 644 /lib/systemd/system/name.service
sudo chmod 744 /usr/bin/name_starter.sh
```
Запуск daemon
```
sudo systemctl daemon-reload
sudo systemctl start name.service
sudo systemctl status name.service
# если все норм и юнит запустился...
sudo systemctl enable name.service
```