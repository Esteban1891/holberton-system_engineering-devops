# create a file in /tmp.
file { 'holberton':
	path            =>  '/tmp/holberton',
	mode            =>  '0744',
	owner           =>  'www-data',
	group           =>  'www-data',
	content         =>  'I love Puppet',
}
