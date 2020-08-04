# Modifies the "ssh_config" file

file_line { 'Modify password authentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => 'PasswordAuthentication yes'
}

file_line { 'Add ssh key file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IndentityFile ~/.ssh/holberton'
}
