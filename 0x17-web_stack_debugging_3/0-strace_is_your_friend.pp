#File: 0-strace_is_your_friend.pp
exec { 'fix-apache-error':
	 command     => '/bin/bash -c "some_command_to_fix_the_issue"',
	 path        => '/usr/bin:/bin',
	refreshonly  => 'true',
	subscribe   => Service['apache2'],

}
