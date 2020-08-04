# Calling pkill
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
