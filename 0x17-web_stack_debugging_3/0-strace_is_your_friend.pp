# Fixes an error with a WordPress Website
exec { '/var/www/html/wp-setting.php':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
