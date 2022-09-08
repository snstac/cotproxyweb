***********
COTProxyWeb
***********

.. image:: https://raw.githubusercontent.com/ampledata/cotproxy/main/docs/youtube.png
    :alt: YouTube: Getting started with COTProxy
    :target: https://www.youtube.com/watch?v=ltVxh1uQ_EQ

COTProxy Web Administration
###########################

COTProxyWeb is a web-baesd front-end for the `COTProxy <https://github.com/ampledata/cotproxy>`_ program. 
COTProxyWeb supports creation, replacement, updating and deletion (CRUD) of COTproxy 
Objects & Transforms. 

Concept of Operations CONOPS:

.. image:: https://raw.githubusercontent.com/ampledata/cotproxy/main/docs/cotproxy-concept.png
   :alt: COTProxyWeb Concept of Operations CONOPS
   :target: https://raw.githubusercontent.com/ampledata/cotproxy/main/docs/cotproxy-concept.png


Support This Project
====================

**Help**: Email takhelp@undef.net or Signal/WhatsApp: +1-310-621-9598

This project has been developed for the Disaster Response, Public Safety and
Frontline Healthcare community. All contributions further project development and 
ensure ongoing support.

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

COTProxyWeb should be started as a background sevice ('run forever', daemon, etc). 
Most modern Linux-based operating systems use the `systemd <https://systemd.io/>`_ 
System and Service Manager.

CentOS, Debian, Ubuntu, RaspberryOS, Raspbian
---------------------------------------------

These instructions will create, enable and start a service on Linux.

1. Download the example cotproxy systemd service definition::

    $ sudo wget --output-document=/etc/systemd/system/cotproxyweb.service https://raw.githubusercontent.com/ampledata/cotproxyweb/main/cotproxyweb.service

2. Edit the COTProxyWeb service and change ``CHANGEME`` to the path to the directory where you downloaded cotproxyweb::

    $ sudo nano /etc/systemd/system/cotproxyweb.service

(e.g. If you downloaded cotproxyweb to /home/pi, CHANGEME should be changed to /home/pi)

3. Edit COTProxyWeb settings.py and append your systems IP address to the ALLOWED_HOSTS list (that is, add the IP of 
the system where you're running COTProxyWeb)::

    $ nano cotproxyweb/settings.py

4. Enable cotproxyweb systemd service::
    
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable cotproxyweb
    $ sudo systemctl start cotproxyweb

5. You can view logs with: ``$ sudo journalctl -xef``


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
