# Installing puppet lint
package { 'puppet-lint':
  ensure   => '2.1.1',
  provide => 'gem',
}
