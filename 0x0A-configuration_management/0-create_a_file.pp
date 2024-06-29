# create a file in /tmp

file {'/tmp/school':
ensure  => file,
mode    => '0744',
owner   => 'www-data',
content => 'I love Puppet',
group   => 'www-data',
}
