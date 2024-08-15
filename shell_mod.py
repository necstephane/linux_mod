#!/usr/bin/env python

######################################################################
## Shell library
module = {
    'name':     'shell_mod',
    'version':  '0.1',
    'purpose':  'Run Shell command'
    }

######################################################################
## Libraries Import
import logging
import subprocess

######################################################################
logging_level = logging.DEBUG

######################################################################
## Classes & Objects

# Shell Class & Object
class Shell:
    ''' Shell Class & Object
    '''
    
    ## Object

    def __init__(
            self,
            command: str=None,
            logging_level: int=logging.DEBUG) -> None:
        ''' '''
        ## Properties
        self.command = command
        self.logging_level = logging_level
        
        ## Initialisations
        self.result = {}
        self.returncode = 0
        self.stderr = None
        self.stdout = None
        self.stdout_list = []
    
    def __repr__(self) -> str:
        txt = f'{__class__.__name__}\n'
        if self.command:
            txt += f'Command:\t{self.command}\n'
        if self.result:
            #txt += f'{self.result}'
            if self.stdout:
                txt += f'Result Output (stdout):\t{self.stdout}\n'
                
                if self.stdout_list:
                    txt += f'Result Output (list):\t{self.stdout}\n'
                    for element in self.stdout_list:
                        txt += f'{element}\n'
            if self.stderr:
                txt += f'Result Error (stderr):\t{self.stdout}\n'
            if self.returncode:
                txt += f'Result Code (returncode):\t{self.returncode}\n'
        if self.logging_level:
            txt += f'Logging Level:\t{self.logging_level}\n'
        return txt
        
    def __str__(self) -> str:
        return self.__repr__()
    
    ## Object Methods

    # Run
    def __run__(
            self,
            command: str=None
            ) -> None:
        self.command = command
        
        ## Run
        self.result = Shell.run(command=command)
        
        if self.result:
            
            if self.result.returncode:
                self.returncode = self.result.returncode
                
            if self.result.stdout:
                stdout_bytestring = self.result.stdout
                
                # Convert byte string into string
                self.stdout = stdout_bytestring.decode('utf-8')
                
                # Create a list
                self.stdout_list = self.stdout.split('\n')[:-1]
                
            if self.result.stderr:
                self.stderr = self.result.stderr
        

    ## Static Methods
    def run(command: str) -> dict:
        ''' '''
        result = None
        message_error = None
        message_debug = None
        message_info = None
        
        try:
            result = subprocess.run(command, capture_output=True, shell=True, check=True)
            
        except Exception as err:
            message_error = f'Error trying runnung the command {command}:\t{err}\n'
            
        else:
            # no error
            message_debug = f'Result:\t{result}\n'
        
        finally:
            if message_error:
                logging.error(message_error)
            if message_debug:
                logging.debug(message_debug)
                
            if result:
                return result
            else:
                return None

######################################################################        
## Main
if __name__ == '__main__':
    
    ## Logging
    logging.basicConfig(level=logging_level)
    
    module_name = module['name']
    message = f'testing module {module_name}'
    logging.info(message)
    
    ## Create Shell Object
    sh = Shell()
    
    message = f'{sh}'
    logging.info(message)
    
    # Run command
    command = 'df -h'
    sh.__run__(command=command)
    
    message = f'{sh}'
    logging.info(message)
    
    # Exit with the command returned code
    exit(sh.returncode)
    
###################################################################### 

    if sh.command:
        message = f'Shell command:\t{sh.command}\n'
        logging.info(message)
    
    #
    if sh.result:
        message = f'Shell command result:\t{sh.result}\n'
        logging.info(message)
    
        if sh.result.returncode == 0:
            message = f'Shell command result (return code):\t{sh.result.returncode} [SUCCESS]\n'
            logging.info(message)
        else:
            message_warning = f'Error Code:\t{sh.result.returncode}\n'
            logging.warning()
        
        if sh.result.stdout:
            message = f'Shell command result (stdout):\t{sh.result.stdout}\n'
            logging.info(message)
            
            result = sh.result.stdout
            message_debug = f'Result:\t{result}\n'
            logging.debug(message_debug)

            message_debug = f'Result (type):\t{type(result)}\n'
            logging.debug(message_debug)
            
            result_data = result.decode('utf-8')
            result_list = result_data.split('\n')[:-1]
            
            message_debug = f'Result (list):\t{result_list}\n'
            logging.debug(message_debug)       
            
            for res in result_list:
                message_debug = f'{res}\n'
                logging.debug(msg=message_debug)
        
        if sh.result.stderr:
            message = f'Shell command result (stderr):\t{sh.result.stderr}\n'
            logging.info(message)