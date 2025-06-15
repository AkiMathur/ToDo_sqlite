import sqlite3

con = sqlite3.connect("todo.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY,date DEFAULT CURRENT_DATE,task TEXT NOT NULL)")

def show_lst():
    week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    rows = cur.execute("""SELECT id,strftime('%w',date) AS weekday,date,task FROM todo""").fetchall()
    print("ID \t\t Date \t\t\t Task")
    for id,weekday,date,task in rows:
        print()
        print(f"{id}\t{week[int(weekday)]}\t{date}\t{task}")

def add_tsk(tsk,date):
    
    if date.lower() == "today":
        cur.execute("INSERT INTO todo (task) VALUES (?)",(tsk,))
        con.commit()
    else:
        date = "2025-" + date[3:] + '-' + date[:2]
        cur.execute("INSERT INTO todo (date,task) VALUES (?,?)",(date,tsk))
        con.commit()

def update_tsk(id,task,date):
    date = "2025-" + date[3:] + '-' + date[:2]
    cur.execute("UPDATE todo SET date = ?, task = ? WHERE id = ?",(date,task,id))
    con.commit()
    print("\n---------Done---------")

def del_tsk(id):
    cur.execute("DELETE FROM todo WHERE id = ?",(id,))
    con.commit()
    print("\n---------Done---------")

def main():
    print("""**************\n Welcome to the TODO App \n A Command-line tool to help you track tasks, stay organized, and boost productivity right from your terminal \n**************""")
    while True:
        print("\n******* MENU *******")
        print("1} View your current To-Do list")
        print("2} Add new task to the To-do list")
        print("3} Edit a task in the To-do list")
        print("4} Delete a task you no longer need")
        print("5} Exit")        
        
        action = int(input("Choose the action number: "))

        match action:
            case 1:
                show_lst()
                
            case 2:
                task = input("Please Enter Your Task: ")
                date = input("Enter the date dd/mm (or type 'today' to use the current date): ")
                add_tsk(task,date)
                print("\n---------Done---------")
            case 3:
                id = input("Please Enter The Task ID: ")
                task = input("Please Enter Your Task: ")
                date = input("Enter the date dd/mm (or type 'today' to use the current date): ")
                update_tsk(id,task,date)
            case 4:
                id = input("Please Enter The Task ID: ")
                del_tsk(id)
                
            case 5:
                break
            case _:
                print("\nInvalid option")

if __name__ == "__main__":
    main()