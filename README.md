# Control Raspberry Temperature and Fan
The script on python 3, to monitor the temperature of Raspberry Pi 4 and automatically turn on the cooling fan
> Скрипт на python 3, для мониторинга температуры Raspberry Pi 4 и автоматического включения вентилятора охлаждения

After running the script, the processor temperature and the current state of the fan are displayed in the console (test interval 2 seconds). When the temperature specified in the script is exceeded (55 degrees Celsius), cooling is turned on for 20 seconds, after the temperature drops (to 40 degrees Celsius), the fan turns off.
>После запуска скрипта, в консоль выводится температура процессора и текущее состояние вентилятора (интервал проверки 2 секунды). При превышении заданной в скрипте температуры (55  градусов по цельсию), включается охлаждение на 20 секунд, после снижения температуры (до 40 градусов по цельсию) вентилятор выключается.

In the script, you can manually set the parameters:
```
FAN_ON_MODE = 55 # (In celsius) The upper temperature threshold at which cooling is turned on.
FAN_OFF_MODE = 40 # (In celsius) Lower temperature threshold at which cooling is turned off
SLEEP_INTERVAL = 2 # (In seconds) Temperature Check Interval
SLEEP_INTERVAL_FAN = 10 # (In seconds) Temperature Check Interval
FAN_PIN = 21 # GPIO port.
```
>В скрипте можно вручную задать следующие параметры:
```
FAN_ON_MODE = 55 # (в градусах Цельсия) Верхний температурный порог, при котором включается охлаждение.
FAN_OFF_MODE = 40 # (в градусах Цельсия) Нижний температурный порог, при котором охлаждение отключено
SLEEP_INTERVAL = 2 # (в секундах) Интервал проверки температуры
SLEEP_INTERVAL_FAN = 20 # (в секундах) Интервал проверки температуры
FAN_PIN = 21 # GPIO порт.
```

This script can be run either manually or added to cron
>Данный скрипт можно запускать как вручную, так и добавить в крон (автозапуск)

### Necessary components:
```
Raspberry Pi 4 Model B (or analog)
5V fan
680Ω resistor (in my case, it's just a LED)
NPN transistor (2N2222)
```

>Необходимые компоненты:
```
Raspberry Pi 4 Model B (или аналог)
вентилятор 5V
резистор 680Ом (в моем случае это просто сведодиод)
NPN транзистор (2N2222)
```

You will also need to install separately in python 3, the GPIO module
>Так же понадобится установить отдельно в Python3,  модуль GPIO
```
pip install RPi.GPIO
```
OR \ или
```
pip3 install RPi.GPIO
```


### Scheme
> Общая схема

![Scheme](https://github.com/blyamur/Control-Raspberry-Temperature-and-Fan/blob/master/img/image.jpg)

### Copyrights and Licenses
Not for commercial use.

2020  [Mons](https://blog.mons.ws)


### Did you find this useful?!
> Вы нашли это  полезным ?!

Happy to hear that :) *If You want to help me, you can buy me a cup of cup of coffee ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [PayPal](https://paypal.me/enkonu) or [ko-fi](https://ko-fi.com/W7W460SQ3) )*

> Рад это слышать :) Если вы хотите мне помочь, вы можете угостить меня чашкой кофе



*Thanks for reading :heart_eyes_cat:*
> Спасибо за чтение!

~Mons
