<<<<<<< HEAD
The :mod:`llnovaclient` Python API
==================================

.. module:: llnovaclient
   :synopsis: A client for the OpenStack Nova API.

.. currentmodule:: llnovaclient
=======
The :mod:`novaclient` Python API
==================================

.. module:: novaclient
   :synopsis: A client for the OpenStack Nova API.

.. currentmodule:: novaclient
>>>>>>> 2019f5edf36f07152e75717f21875ad0adb0e0d6

Usage
-----

First create an instance of :class:`OpenStack` with your credentials::

<<<<<<< HEAD
    >>> from llnovaclient import OpenStack
    >>> llnova = OpenStack(USERNAME, PASSWORD, AUTH_URL)
=======
    >>> from novaclient import OpenStack
    >>> nova = OpenStack(USERNAME, PASSWORD, AUTH_URL)
>>>>>>> 2019f5edf36f07152e75717f21875ad0adb0e0d6

Then call methods on the :class:`OpenStack` object:

.. class:: OpenStack

    .. attribute:: backup_schedules

        A :class:`BackupScheduleManager` -- manage automatic backup images.

    .. attribute:: flavors

        A :class:`FlavorManager` -- query available "flavors" (hardware
        configurations).

    .. attribute:: images

        An :class:`ImageManager` -- query and create server disk images.

    .. attribute:: ipgroups

        A :class:`IPGroupManager` -- manage shared public IP addresses.

    .. attribute:: servers

        A :class:`ServerManager` -- start, stop, and manage virtual machines.

    .. automethod:: authenticate

For example::

<<<<<<< HEAD
    >>> llnova.servers.list()
    [<Server: buildslave-ubuntu-9.10>]

    >>> llnova.flavors.list()
=======
    >>> nova.servers.list()
    [<Server: buildslave-ubuntu-9.10>]

    >>> nova.flavors.list()
>>>>>>> 2019f5edf36f07152e75717f21875ad0adb0e0d6
    [<Flavor: 256 server>,
     <Flavor: 512 server>,
     <Flavor: 1GB server>,
     <Flavor: 2GB server>,
     <Flavor: 4GB server>,
     <Flavor: 8GB server>,
     <Flavor: 15.5GB server>]

<<<<<<< HEAD
    >>> fl = llnova.flavors.find(ram=512)
    >>> llnova.servers.create("my-server", flavor=fl)
=======
    >>> fl = nova.flavors.find(ram=512)
    >>> nova.servers.create("my-server", flavor=fl)
>>>>>>> 2019f5edf36f07152e75717f21875ad0adb0e0d6
    <Server: my-server>

For more information, see the reference:

.. toctree::
   :maxdepth: 2

   ref/index
