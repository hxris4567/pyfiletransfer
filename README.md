# pyfiletransfer
A basic file transfer script written in Python. Sloppily written in a night.
## Python Dependencies
`socket`
`struct`
`os`
`tkinter`
## Use
In `client.py`, change the strings `SERVER_IP` and `SERVER_PORT` to the server you wish to connect to. 
######
In `server.py`, change `SERVER_IP` to your local network IP and `SERVER_PORT` to the port opened for receiving files. If the two devices are on the same network, then any port can be used. Additionally, change `DIRECTORY` to whatever directory name you wish for the script to use. It will be created if it does not exist.
######
Files with the same name will be overwritten.
## Function
Both scripts use the `socket`	 library to communicate between different devices over a network. The `struct` library is used to encode and decode transferred files in binary. The `os` library provides access to the server's filesystem, and the `tkinter` library creates some level of a GUI in the client script.
## Notes
Cannot send multiple files or directories (yet).
