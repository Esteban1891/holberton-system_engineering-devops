# 0x05-processes_and_signals


![N|Solid](https://media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-1-4842-5049-5_13/MediaObjects/473415_1_En_13_Fig4_HTML.png =12x)


## Description

This projects deals with processes and signals in bash.

## Mandatory Tasks

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

## Advanced Tasks

| Files | Description |
| ----- | ----------- |
| 100-process_and_pid_file | Creates the file `/var/run/holbertonschool.pid` containing its PID, displays `To infinity and beyond` indefinitely, displays `I hate the kill command` when receiving a `SIGTERM` signal, displays `Y U no love me?!` when receiving a `SIGINT` signal, and deletes the file `/var/run/holbertonschool.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal |
| 101-manage_my_process | Manages the `manage_my_process` file's process |
| manage_my_process | Indefinitely writes `I am alive!` to the file `/tmp/my_process` and has a sleep of 2 |
| 102-zombie.c | Creates 5 zombie processes |

## Compilation

To compile 102-zombie.c run the command `gcc -Wall -Werror -Wextra -pedantic` and run using the command `./[executable name]`

