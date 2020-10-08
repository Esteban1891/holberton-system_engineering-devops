# Web stack debugging #4

This was the fifth in a series of web stack debugging projects. In these
projects, I was given broken/bugged webstacks in isolated containers,
and tasked with fixing the web stack to a working state. For each
task, I wrote a script automating the commands necessary to fix the
web stack.

## Tasks :page_with_curl:

* **0. Sky is the limit, let's bring that limit higher**
  * [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp): Puppet manifest
  that increases the amount of traffic an Apache web server can effectively handle.
 
 ### example of all failed 
![](https://github.com/Esteban1891/holberton-system_engineering-devops/blob/master/0x1B-web_stack_debugging_4/error%20task0.png?raw=true)
	
 ### solution failed change
 ![](https://github.com/Esteban1891/holberton-system_engineering-devops/blob/master/0x1B-web_stack_debugging_4/solution%20task0.png?raw=true)
* **1. User limit**
  * [1-user_limit.pp](./1-user_limit.pp): Puppet manifest that changes the operating system
  configuration so that it is possible to login with the user `holberton` and open a file
  without error.


## Authors :black_nib:

- [Esteban De La Hoz](https://www.linkedin.com/in/esteban-de-la-hoz-romero-b6270017b/) | [Twitter](https://twitter.com/Esteban18911) | [GitHub](https://github.com/Esteban18911)

