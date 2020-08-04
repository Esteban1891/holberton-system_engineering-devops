# Calling pkill
exec {
  path => ['/usr/bin', '/usr/sbin', '/bin', '/sbin']
  command => 'pkill -f killmenow'
}

