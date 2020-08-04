# Calling pkill
exec {
  path => ['/bin']
  command => 'pkill -f killmenow'
}
