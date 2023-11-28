# install flask from pip3 by use  Puppet,

package {'puppet-lint':
  ensure => '2.1.0',
  provider => 'gem',
}
