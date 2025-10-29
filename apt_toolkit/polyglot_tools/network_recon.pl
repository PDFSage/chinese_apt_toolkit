#!/usr/bin/perl
use strict;
use warnings;

my $network = "192.168.1.";
for my $i (1..254) {
    my $ip = $network . $i;
    if (system("ping -c 1 $ip") == 0) {
        print "$ip is up\n";
    }
}

