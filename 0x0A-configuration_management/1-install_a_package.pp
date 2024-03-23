# File: install_flask.pp
# Description: Install Flask using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.2.0',  # Use a compatible Werkzeug version
  provider => 'pip3',
}
