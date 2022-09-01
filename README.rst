***********
COTProxyWeb
***********

COTProxy Web Administration
###########################

COTProxyWeb is a web-baesd front-end for the `COTProxy <https://github.com/ampledata/cotproxy>`_ program. 
COTProxyWeb supports creation, replacement, updating and deletion (CRUD) of COTproxy 
Objects & Transforms. 

`YouTube: Getting started with COTProxy <https://www.youtube.com/watch?v=ltVxh1uQ_EQ>`_.

Concept:

.. image:: https://raw.githubusercontent.com/ampledata/cotproxy/main/docs/cotproxy-concept.png
   :alt: COTProxy concept diagram.
   :target: https://raw.githubusercontent.com/ampledata/cotproxy/main/docs/cotproxy-concept.png


Support Development
===================

**Tech Support**: Email support@undef.net or Signal/WhatsApp: +1-310-621-9598

This tool has been developed for the Disaster Response, Public Safety and
Frontline Healthcare community. This software is currently provided at no-cost
to users. Any contribution you can make to further this project's development
efforts is greatly appreciated.

.. image:: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
    :target: https://www.buymeacoffee.com/ampledata
    :alt: Support Development: Buy me a coffee!


Installation
============

COTProxyWeb should be installed from source::

    mkdir -p /usr/src
    cd ~/src
    git clone https://github.com/ampledata/cotproxyweb.git
    cd cotproxyweb/
    python3 -m pip install -r requirements.txt
    python3 manage.py migrate
    python3 manage.py createsuperuser \
      --username admin --email admin@example.com


Running
=======

COTProxyWeb should be started as a background sevice (daemon). Most modern systems 
use systemd.


Debian, Ubuntu, RaspberryOS, Raspbian
-------------------------------------

1. Copy the following code block to ``/etc/systemd/system/cotproxyweb.service``::

    [cotproxy]
    Description=COTProxyWeb Service
    After=multi-user.target
    [Service]
    WorkingDirectory=CHANGEME: PATH TO COTPROXYWEB SOURCE
    ExecStart=python3 manage.py runserver 0:10415
    Restart=always
    RestartSec=5
    [Install]
    WantedBy=multi-user.target

(You can create ``cotproxyweb.service`` using Nano: ``$ sudo nano /etc/systemd/system/cotproxyweb.service``)

2. Enable cotproxy systemd service::
    
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable cotproxyweb
    $ sudo systemctl start cotproxyweb

4. You can view logs with: ``$ sudo journalctl -xef``




Source
======
Github: https://github.com/ampledata/cotproxyweb


Author
======
Greg Albrecht W2GMD oss@undef.net

https://ampledata.org/


Copyright
=========
COTProxyWeb is Copyright 2022 Greg Albrecht


License
=======
COTProxyWeb is licensed under the Apache License, Version 2.0. See LICENSE for details.
