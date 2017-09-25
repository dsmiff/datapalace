# Dominic Smith <domlucasmith@gmail.com>

import os, errno, sys
import logging
from .Logic import Logic

##__________________________________________________________________||
class Datasets(object):
    """
    Args:
        in_dir : Input directory to create the Master directory.
        filesize: Size of the file under the subdirectory to the Master directory.
        structure: Structure under the Master directory. CSV input with subdirectory name and 
                   size of the subdirectory.
        force: Force remake of Master directory.
        dry_run: Perform a dry run.
        logging_level: Level of verbose from logging package.
    """
    
    def __init__(self, in_dir, filesize, structure, out_dir, force, dry_run, logging_level):
        self.dir = in_dir
        self.file_size = filesize
        self.structure = structure
        self.out_dir = out_dir
        self.force = force
        self.dry_run = dry_run
        self.logging_level = logging.getLevelName(logging_level)
        self.logger = logging.getLogger('Master datasets')
        self.logic = Logic()

    def mkdir_p(self, dir):
        '''
        Make subdirectories for a given dir.
        '''        
        try:
            os.makedirs(dir)
            self.logger.info('created a directory, {}'.format(dir))
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(dir):
                self.logger.log(self.logging_level, 'tried to create a directory, {}. already existed'.format(dir))
                if self.force:
                    self.logger.log(self.logging_level, 'force removal of directory, {}. remaking new directory'.format(dir))   
                    import shutil
                    shutil.rmtree(dir)
                    os.makedirs(dir)
                pass
            else: raise
        
    def make_subdir(self):
        '''
        Make subdirectories and create and fill files.
        '''
        for subdir, dir_target_size in self.structure_dict.iteritems():
            self.full_path = os.path.join(self.dir, subdir)
            self.mkdir_p(self.full_path)
            self.logic.fill_subdir(self.full_path, self.file_size, dir_target_size)
        
    def update_subdir(self):
        '''
        Get the size of each subdirectory in self.structure_dict.
        Returns a dictionary where keys are the subdirectories and 
        values are a tuple with (subdir_size, max_file_size)
        max_file_size is the largest file (in bytes) and represents 
        the upper limit.
        '''
        for subdir, dir_target_size in self.structure_dict.iteritems():
            self.full_path = os.path.join(self.dir, subdir)
            size = self.logic.dir_size(self.full_path, False, True)
            self.logic.performUpdate(size)

    def backup_dir(self):
        self.top_tree = os.path.abspath(os.path.expanduser(self.dir))
        self.out_dir  = os.path.abspath(os.path.expanduser(self.out_dir))
        self.logic.backupDir(self.top_tree, self.out_dir, self.dry_run)
        
    def beginWorkspace(self):
        '''
        Main method to execute the logic of making a database.
        '''
        self.structure_dict = self.logic.convert_structure(self.structure)
        self.mkdir_p(self.dir)
        self.make_subdir()

    def updateWorkspace(self):
        '''
        Main method to update the database.
        '''
        self.structure_dict = self.logic.convert_structure(self.structure)
        self.update_subdir()

    def backupWorkspace(self):
        '''
        Main method to backup an existing database.
        '''
        self.backup_dir()
