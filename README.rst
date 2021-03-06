Python bindings to the Rackspace Legacy Cloud Servers API
=========================================================

This is a client for the Rackspace Legacy Cloud Servers API. There's a Python API (the
``lnovaclient`` module), and a command-line script (``lnova``). Each
implements 100% of the Rackspace Legacy Cloud Servers API.

You'll also probably want to read `Rackspace's API guide`__ (PDF) :
The guide will provide you an overview of all of the available functions.

__ http://docs.rackspace.com/servers/api/v1.0/cs-devguide/content/Overview-d1e70.html

Development has stopped on this client, though I will be maintaining it for functionality.

.. contents:: Contents:
   :local:

Command-line API
----------------

Installing this package gets you a shell command, ``nova``, that you
can use to interact with any Rackspace compatible API (including OpenStack).

You'll need to provide your OpenStack username and API key. You can do this
with the ``--username``, ``--apikey`` and  ``--projectid`` params, but it's easier to just
set them as environment variables::

    export NOVA_USERNAME=openstack
    export NOVA_API_KEY=yadayada
    export NOVA_PROJECT_ID=myproject

You will also need to define the authentication url with ``--url`` and the
version of the API with ``--version``.  Or set them as an environment
variables as well::

    export NOVA_URL=http://example.com:8774/v1.1/
    export NOVA_VERSION=1.1

If you are using Keystone, you need to set the NOVA_URL to the keystone
endpoint::

    export NOVA_URL=http://example.com:5000/v2.0/

Since Keystone can return multiple regions in the Service Catalog, you
can specify the one you want with ``--region_name`` (or 
``export NOVA_REGION_NAME``). It defaults to the first in the list returned.

You'll find complete documentation on the shell by running
``nova help``::

    usage: lnova [--username USERNAME] [--apikey APIKEY] [--password PASSWORD]
             [--projectid PROJECTID] [--url URL] [--region_name REGION_NAME]
             [--endpoint_name ENDPOINT_NAME] [--version VERSION]
             <subcommand> ...

    Command-line interface to the OpenStack Nova API.

    Positional arguments:
      <subcommand>
        add-fixed-ip        Add a new fixed IP address to a servers network.
        add-floating-ip     Add a floating IP address to a server.
        backup              Backup a server.
        backup-schedule     Show or edit the backup schedule for a server.
        backup-schedule-delete
                            Delete the backup schedule for a server.
        boot                Boot a new server.
        delete              Immediately shut down and delete a server.
        flavor-list         Print a list of available 'flavors' (sizes of
                            servers).
        floating-ip-create  Allocate a floating IP to the current tenant.
        floating-ip-delete  De-allocate a floating IP from the current tenant.
        floating-ip-list    List allocated floating IPs for the current tenant.
        help                Display help about this program or one of its
                            subcommands.
        image-create        Create a new image by taking a snapshot of a running
                            server.
        image-delete        Delete an image.
        image-list          Print a list of available images to boot from.
        ip-share            Share an IP address from the given IP group onto a
                            server.
        ip-unshare          Stop sharing an given address with a server.
        ipgroup-create      Create a new IP group.
        ipgroup-delete      Delete an IP group.
        ipgroup-list        Show IP groups.
        ipgroup-show        Show details about a particular IP group.
        keypair-add         Create a new key pair for use with instances
        keypair-delete      Delete keypair by its id
        keypair-list        Show a list of keypairs for a user
        list                List active servers.
        migrate             Migrate a server to a new host in the same zone.
        reboot              Reboot a server.
        rebuild             Shutdown, re-image, and re-boot a server.
        remove-fixed-ip     Remove an IP address from a server.
        remove-floating-ip  Remove a floating IP address from a server.
        rename              Rename a server.
        rescue              Rescue a server.
        resize              Resize a server.
        resize-confirm      Confirm a previous resize.
        resize-revert       Revert a previous resize (and return to the previous
                            VM).
        root-password       Change the root password for a server.
        secgroup-add-group-rule
                            Add a source group rule to a security group.
        secgroup-add-rule   Add a rule to a security group.
        secgroup-create     Create a new security group.
        secgroup-delete     Delete a security group.
        secgroup-delete-group-rule
                            Delete a source group rule from a security group.
        secgroup-delete-rule
                            Delete a rule from a security group.
        secgroup-list       List security groups for the curent tenant.
        secgroup-list-rules List rules for a security group.
        show                Show details about the given server.
        unrescue            Unrescue a server.
        volume-attach       Attach a volume to a server.
        volume-create       Add a new volume.
        volume-delete       Remove a volume.
        volume-detach       Detach a volume from a server.
        volume-list         List all the volumes.
        volume-show         Show details about a volume.
        zone                Show or edit a Child Zone
        zone-add            Add a Child Zone.
        zone-boot           Boot a server, considering Zones.
        zone-delete         Remove a Child Zone.
        zone-info           Show the capabilities for this Zone.
        zone-list           List all the immediate Child Zones.


    Optional arguments:
      --username USERNAME   Defaults to env[NOVA_USERNAME].
      --apikey APIKEY       Defaults to env[NOVA_API_KEY].
      --apikey PROJECTID    Defaults to env[NOVA_PROJECT_ID].
      --url AUTH_URL        Defaults to env[NOVA_URL] or
                            https://auth.api.rackspacecloud.com/v1.0
                            if undefined.
      --version VERSION     Accepts 1.0 or 1.1, defaults to
                            env[NOVA_VERSION].
      --region_name NAME    The region name in the Keystone Service Catalog
                            to use after authentication. Defaults to first
                            in the list returned.

    See "lnova help COMMAND" for help on a specific command.

--------

This code a fork of `Jacobian's python-cloudservers`__ If you need API support
for the Rackspace API soley or the BSD license, you should use that repository.
python-client is licensed under the Apache License like the rest of OpenStack.

__ http://github.com/jacobian/python-cloudservers

