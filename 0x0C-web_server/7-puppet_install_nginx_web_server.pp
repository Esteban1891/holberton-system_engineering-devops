#Time to practice configuring your server with Puppet! Just as 
#you did before, we’d like you to install and configure an Nginx
#server using Puppet instead of Bash. To save time and effort, you
#should also include resources in your manifest to perform a 301
#redirect when querying /redirect_me.

class nginx {
  package { 'nginx':
    ensure => absent,
  }
package { 'nginx':
  ensure  => installed,
  require => Package['ngingx'],
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-enabled/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://twitter.com/Esteban18911/ permanent;',
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
