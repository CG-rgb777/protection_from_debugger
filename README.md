# protection_from_debugger
Although the name of the program is ultimate_protect_from_debuggers, the protection isn't that cool. There are many more ways to hook the debugger into the process, but I guess I'll figure out how to protect against them someday. There is also a very weak defense against intercepting data sent from the server (and it will work if the attacker uses wireshark and it doesn't occur to him to rename the executable :D). There are also traps that are not activated by themselves in any way, only if someone curious tries to make the program not terminate by itself, and if they try to disable the traps or protection threads, they will have more traps waiting for them :D. Also in the code there is a function “protection_started_check”, if it is disabled, then the “last wall of protection” will be activated, if it is activated the attacker's computer will be shut down.

You can choose between protection written entirely in Python and protection written entirely in C.
Or choose both (I recommend)

For better protection, it's better not to use exec and eval, but if you really need them, just remove lines 11 and 12 from the code.

I strongly recommend that you do not disable all levels of protection or disable lines of code that terminate the program, 
doing so may activate protection that shuts down your computer or fills RAM with “garbage”.

Protection against Windows debugger, VEH debugger, Windows Sandbox(Virtualization) and almost all debuggers from cheat engine version 7.5.
The C version of protection can detect debuggers even if you enable the function of hiding the debugger in the cheat engine settings, 
protection written in Python cannot do this.

To enable protection in your project, simply import the upfd file and call the upfd.start() function for python protection
and upfd_c.start() for C protection

Also remember to compile the C file correctly using this command: gcc -fPIC -shared -o AD.so AD.c
Instead of "AD" you can put your own file name, but then change the path in the code of the file upfd_с.py

Compilation: if you need to compile this project, then I advise you to use the Nuitka library. 
When compiling with protection written in python, add a flags: "--follow-imports"
When compiling with protection written in C, add the flag: "--include-data-file=AD.so=." and "--follow-imports"

An example of what I wrote: "nuitka --standalone --onefile --onefile-no-compression --windows-uac-admin --follow-imports --include-data-file=AD.so=. test.py"

Well, if you want your project to be opened in 15 seconds, use pyinstaller and the --add-binary="path" flag

Interesting fact: if you add the --onefile flag to compile everything 
into 1 file and then upload this file to virustotal, 
you will get a list of ~20 antiviruses that you should not buy (they will detect it as a virus). 
Although even without this flag some antiviruses will identify your file as a virus, if you want to increase the “trust factor” of the file, digitally sign it (there are guides on the Internet that show how to do this for free).
If you have nothing to do at all, then send your file for analysis to a company that owns an antivirus that identified your file as a virus.

And if you need normal protection only against debuggers, then the AD.c file is enough for you(Antiviruses they mark it as suspicious less, but for some reason they mark it as suspicious anyway :/  ).
