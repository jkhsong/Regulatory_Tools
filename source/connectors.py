from abc import ABC, abstractmethod ##helper class in python, Abstract Base Class
from typing import Union
import psycopg2 as pg

class User():
    def __init__(self, 
                 username: Union[None, str] = None,
                 password: Union[None, str] = None) -> None: ##None is the type that method returns
        self.username = username ##initializing username
        self.password = password ##initializing password

class ConnectorBase(ABC):  ##inheriting from ABC
    def __init__(self, user: User, dbname: str, serverIP: str, port: str) -> None:  ##User is an object representing user data 
        super().__init__()  ##inheriting initialization from supertype
        self.dbname = dbname
        self.serverIP = serverIP
        self.username = user.username
        self.serverpass = user.password
        self.port = port

    def __repr__(self) -> str:  ## how to represent as a string
        return f"Port:/IP:username - {self.port}:/{self.serverIP}:{self.username}"

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)
    
    @abstractmethod ## Designates function that needs to be overwritten
    def fetch_server_state(self, substate: str) -> dict:  ##substate is typed as a string (i.e. 'full_state', etc.)
        pass

    @abstractmethod  
    def open_connection(self) -> None:
        pass
    
    @abstractmethod
    def close_connection(self) -> None:
        pass
    
    @abstractmethod
    def execute_command(self, command: str) -> None:
        pass

    @abstractmethod
    def query_all(self, query: str) -> None:
        pass
        
    def retrieve(self, table: Union[None, str], query) -> str:
        pass

    def insert(self, table: Union[None, str] , data) -> str:
        pass

    def replace(self, table: Union[None, str], data) -> str:
        pass
    
    def delete(self, table: Union[None, str], data) -> str:
        pass



class PostgresConnector(ConnectorBase):

    def __init__(self, user: User, dbname: str, serverIP: str, port: str) -> None:
        self.conn = None
        self.cur = None
        super().__init__(user, dbname, serverIP, port)
        
    def fetch_server_state(self, substate: str) -> dict:
        """ This method returns server state as a string """
        # postgres specific code
        return super().fetch_server_state(self, substate)

    def open_connection(self) -> None:
        self.conn = pg.connect(f'dbname = {self.dbname} user = {self.username} password = {self.serverpass}')
        self.cur = self.conn.cursor() ##generate cursor
    
    def close_connection(self):
        self.cur.close()
        self.conn.close()
        
    def execute_command(self, command: str) -> None:
        self.cur.execute(command)
    
    def query_all(self, query: str) -> None:
        self.cur.execute(query)
        query_answer = self.cur.fetchall()
        return query_answer
    
    def print_query_results(self, query:str, order: Union[None,list] = None) -> None:
        printback = self.query_all(query)
        if order == None:
            for item in printback:
                print(item)
        else:
            for tuple in printback:
                printline = ''
                for i in order:
                    printline += '| ' + tuple[i] + ' |'
                print(printline)


class MongoConnector(ConnectorBase):

    def __init__(self, user: User, serverIP: str, port: str) -> None:
        super().__init__(user, serverIP, port)

    def fetch_server_state(self, substate: str) -> dict:
        """ This method returns server state as a string """
        # mongo db logic
        
        return 

    def open_connection(self) -> None:
        
        return

# if __name__ == '__main__':  ##__name__ is X, and __main__ executes this block

#     james = User('jks2022', 'pass1234')
#     pg_connector = PostgresConnector(james, 'james_DB', '128.0.0.1', '7001')
#     print(pg_connector)


    ## get Docker installation of postgres)
    ## try interface with this
    ## psychopg2  <-- interfaces with postgres
    ## Rationale: Easy/convenient, universal version compatibility
    ## Mongo works with it too (week 3)
    ## 
    ## Manually put in data, make a DB, insert rows, make an interface with this class

    ## Cloud stuff (do this second after local on AWS)
    ## boto3 <-- package that interfaces with AWS