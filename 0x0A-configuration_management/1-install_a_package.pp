# File: install_flask.pp
# Description: Install Flask using pip3

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
