# 0x05-processes_and_signals :satellite:


![N|Solid](https://www.tecmint.com/wp-content/uploads/2018/06/fkill-Kill-Linux-Process-by-Name-PID.png)


## Description :computer:

This projects deals with processes and signals in bash.

## Mandatory Tasks :sound:

| Files | Description |
| ----- | ----------- |
| 0-what-is-my-pid | Script to display its own PID |
| 1-list_your_processes | Lists all currently running processes |
| 2-show_your_bash_pid | Displays the line(s) containing the word `bash` |
| 3-show_your_bash_pid_made_easy | Displays the PID and process name of processes that contain the word `bash` |
| 4-to_infinity_and_beyond | Displays `To inifinity and beyond` indefinitely |
| 5-kill_me_now | Kills the `4-to_infinity_and_beyond` process |
| 6-kill_me_now_made_easy | Kills the `4-to_infinity_and_beyond` process |
| 7-highlander | Displays `To infinity and beyond` indefinitely with a sleep period of 2 and prints `I am invincible!!!` when receiving a `SIGTERM` |
| 8-beheaded_process | Kills the process `7-highlander` |

## Advanced Tasks :dart:

| Files | Description |
| ----- | ----------- |
| 100-process_and_pid_file | Creates the file `/var/run/holbertonschool.pid` containing its PID, displays `To infinity and beyond` indefinitely, displays `I hate the kill command` when receiving a `SIGTERM` signal, displays `Y U no love me?!` when receiving a `SIGINT` signal, and deletes the file `/var/run/holbertonschool.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal |
| 101-manage_my_process | Manages the `manage_my_process` file's process |
| manage_my_process | Indefinitely writes `I am alive!` to the file `/tmp/my_process` and has a sleep of 2 |
| 102-zombie.c | Creates 5 zombie processes |
| 103-screencast_unix_signal | [How to kill a process in linux with C](https://youtu.be/02HjGHEX21o) |

## Compilation :flashlight:

To compile 102-zombie.c run the command `gcc -Wall -Werror -Wextra -pedantic` and run using the command `./[executable name]`

## Author :octocat:

[Esteban De La Hoz](https://www.linkedin.com/in/esteban-de-la-hoz-romero-b6270017b/) | [Twitter](https://twitter.com/Esteban18911) | [GitHub](https://github.com/Esteban18911)

