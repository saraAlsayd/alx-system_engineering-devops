#!/usr/bin/pup
# This Puppet manifest installs puppet-lint
package { 'flask':
  ensure   => '2.1.1',
  provider => 'pip3'
}
