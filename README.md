PakMan - Packet Mangler in Python.
==================================

Goal of this project is to write a packet mangling service based on the netfilter queue. This is much like the [FakeNet](http://practicalmalwareanalysis.com/fakenet/), but allows you to do everything you want with packets.

Turning on netfilter queue
--------------------------

It's as simple as:

    iptables -A INPUT -i vboxnet0 -j NFQUEUE
