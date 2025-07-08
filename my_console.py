import cmd

class MyConsole(cmd.Cmd):
    prompt = "(myconsole) "
    def do_hello(self, arg):
        """Say hello"""
        print("Hello, world!")

    def do_exit(self, arg):
        """Exit the console"""
        return True
                                                    
