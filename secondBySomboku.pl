#!/usr/bin/perl


use strict; 
use Data::Dumper;

sub fuck_me;
fuck_me("Nur So");

my $dunno;

sub fuck_me($dunno) {
	print $dunno;
}

fuck_me('dsf');
