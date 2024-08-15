#!/usr/bin/env python

######################################################################
## Shell library
module = {
    'name':     'linux_mod',
    'version':  '0.1',
    'purpose':  'Linux library'
    }

######################################################################
## Libraries Import

# Standard
import logging

# Other
from shell_mod import Shell

######################################################################
logging_level = logging.DEBUG

######################################################################
## Classes & Objects

# Documentation Class & Object
class Documentation:
    ''' '''
    
    documentation_commands = {
        'Disks':        {
            'Disks':        'fdisk -l',
            'Homes':        'du -sh -c /home/*',
            'Partitions':   'df -h',
            'IDs':          'blkid'
            },
        'Processor':    {
            'Processors':   'cat /proc/cpuinfo'
            },
        'Memory':        {
            'Memory':       'cat /proc/meminfo'
            }
        }
        
    def document() -> dict:
        ''' '''
        #shells = {}
        results = {}
        message_info = ''
        
        for key, val in Documentation.documentation_commands.items():
            message_info += f'{key}:\n'
            
            for k, command in val.items():
                message_info += f'{k}:\n'
                message_info += f'command:\t{command}:\n'
                
                # Run command
                sh = Shell()
                
                index = f'{key}{k}'
                results[index] = sh.__run__(command=command)
                
        return results
                
## Main
if __name__ == '__main__':
    
    ## Logging
    logging.basicConfig(level=logging_level)
    
    results = Documentation.document()
    
    print(results)

    for index, result in results.items():
        message = f'{index}:\t{result}\n'
        logging.info(message)
