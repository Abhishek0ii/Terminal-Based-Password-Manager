import mysql.connector


from rich import print as printc
from rich.console import Console
console = Console()


def dbconfig():
    db = mysql.connector.connect(
        host='localhost'
        user='pm'
        passwd='password'
    )

#for error handlanding 
except Exception as e:
console.print_exception(show_local=True)


return db

# import mysql.connector
# from mysql.connector import Error
# from rich import print as printc
# from rich.console import Console

# console = Console()

# def dbconfig():
#     try:
#         db = mysql.connector.connect(
#             host='localhost',
#             user='pm',
#             passwd='password'
#         )
#         if db.is_connected():
#             printc("[green]Connected to the database successfully![/green]")
#         return db
#     except Error as e:
#         console.print_exception(show_locals=True)
#         printc(f"[red]Error: {e}[/red]")
#         return None