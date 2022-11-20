#!/usr/bin/python3
""" dirkk console dev """

import cmd
import sys


class DIRKKShell(cmd.Cmd):
    """DIRKK shell"""
    intro = 'Welcome to the DIRKK  shell.   Type help or ? to list commands.\n'
    prompt = '{DIRKK} '

    #def __init__(self, username=""):
     #   """initialize user"""
      #  self.username = username

    def do_bye(self, arg):
        """close DIRKK Shell"""
        print("Thank you for your best experience")
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False
    
    def do_EOF(self, arg):
        """exit DIRKK Shell"""
        return True

    def do_connect(self, arg):
        """ connect database"""
        user = input('MYSQL DATABASE USER: ')
        pwd = input('MYSQL DATABASE PASSWORD: ')
        host = input('MYSQL DATABASE HOST: ')
        db = input('MYSQL DATABASE NAME: ')
        ty = 'db'
        env = input('Quel type d\'environnement (dev or test)? : ')
        with open('.env.example','w', encoding="utf-8") as f:
            f.write('DIRKK_MYSQL_USER={}\n'.format(user))
            f.write('DIRKK_MYSQL_PWD={}\n'.format(pwd))
            f.write('DIRKK_MYSQL_HOST={}\n'.format(host))
            f.write('DIRKK_MYSQL_DB={}\n'.format(db))
            f.write('DIRKK_TYPE_STORAGE={}\n'.format(ty))
            f.write('DIRKK_ENV={}\n'.format(env))
        #with open(".env.example") as e:
        return False

   # def do_register(self, value):
        #""" get Account """
       # value = input("what's your name ? ")
        #if type(value) is not string:
        #    raise TypeError("please enter string")
        #self.__username = value
        #fonction = input("your title job ?")

    #def do_showUser(self):
       # """ show user info"""
        #print(self.__username)

if __name__ == '__main__':
    DIRKKShell().cmdloop()
