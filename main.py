import admin
import quiz
import leaderboard
import sqlite3 as db

conn=db.connect("Quiz.db")
cur=conn.cursor()
def main():
    global conn
    while(True):
        choice=int(input('''
        Main Menu
        1)Login
        2)PlayGame
        3)Show Leader Board
        4)Exit
        Enter your choice:-'''))
        if(choice==1):
            admin.auth(conn)
        elif(choice==2):
            pass
        elif(choice==3):
            pass
        elif(choice==4):
            return
        else:
            print("Invalid Choice")




if __name__=="__main__":
    main()