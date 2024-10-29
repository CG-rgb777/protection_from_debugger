# protection_from_debugger
Honestly, I'm new to programming, and although the name of the program is ultimate_protect_from_debuggers, the protection isn't that cool. There are many more ways to hook the debugger into the process, but I guess I'll figure out how to protect against them someday. There is also a very weak defense against intercepting data sent from the server (and it will work if the attacker uses wireshark and it doesn't occur to him to rename the executable :D). There are also traps that are not activated by themselves in any way, only if someone curious tries to make the program not terminate by itself, and if they try to disable the traps or protection threads, they will have more traps waiting for them :D. Also in the code there is a function “protection_started_check”, if it is disabled, then the “last wall of protection” will be activated, if it is activated the attacker's computer will be shut down. And if the attacker's OS is undefined, the file will simply be deleted (I think it's worth cutting this function).

For better protection, it's better not to use exec and eval, but if you really need them, just remove lines 14 and 15 from the code.

I strongly recommend that you do not disable all levels of protection or disable lines of code that terminate the program, 
doing so may activate protection that shuts down your computer or fills RAM with “garbage”.

Protection against Windows debugger, VEH debugger, Windows Sandbox. 

To enable protection in your project, simply import the upfd file and call the upfd.start() function
To check if all protection is working, call the upfd.test_protection() function

Also remember to compile the C file correctly using this command: gcc -fPIC -shared -o AD.so AD.c -lntdll -lpsapi
Instead of "AD" you can put your own file name, but then change the path in the code of the file upfd.py
