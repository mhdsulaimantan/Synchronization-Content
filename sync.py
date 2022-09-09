from genericpath import isfile
import os
import shutil
import time
import logging
import hashlib


class Synchronization:
    def __init__(self, source_path, replica_path, period):
        self.source_path = source_path
        self.replica_path = replica_path
        self.sync_period = period

    def run(self):
        logging.info('Synchronization started')
        # get all files and subdir in source
        source_dir_files = self._get_all_files(self.source_path)
        # copy all source data to the replica dir
        self._copy_to_replica()

        while True:
            self._sync_source(source_dir_files)
            source_dir_files = self._get_all_files(self.source_path)

            self._sync_replica()

            # repeat
            time.sleep(self.sync_period)

    def _copy_to_replica(self):
        shutil.copytree(self.source_path, self.replica_path,
                        dirs_exist_ok=True)
        logging.info(
            "source files copied to replica directory - [COPY] - [PATH='" + self.replica_path + "']")

    def _sync_source(self, pre_files):
        # changes in source
        self.sync_changes = {}

        new_source_files = self._get_all_files(self.source_path)

        # source files update
        # compare similar files in replica and source folders
        self._updated_source_files()

        # check removed files from source
        self._removed_source_files(pre_files, new_source_files)

        # check created files in source
        self._added_source_files(pre_files, new_source_files)

    def _sync_replica(self):
        for type, data in self.sync_changes.items():
            # remove
            if type == 'rm':
                for source_file in data:
                    rep_file = self.replica_path + \
                        source_file.replace(self.source_path, '')
                    # dir or file
                    # after remove from source
                    if os.path.isdir(rep_file):
                        logging.info(
                            "folder removed from replica directory [FOLDER_NAME='" + os.path.basename(rep_file) + "'] - [REMOVE] - [PATH='" + rep_file + "']")
                        shutil.rmtree(rep_file)
                    elif os.path.isfile(rep_file):
                        logging.info(
                            "file removed from replica directory [FILE_NAME='" + os.path.basename(rep_file) + "'] - [REMOVE] - [PATH='" + rep_file + "']")
                        os.remove(rep_file)

            # update or create
            else:
                # after create in source
                for source_file in data:
                    rep_file = self.replica_path + \
                        source_file.replace(self.source_path, '')
                    if os.path.isdir(source_file):
                        logging.info(
                            "new folder copied to replica directory [FOLDER_NAME='" + os.path.basename(rep_file) + "'] - [COPY] - [PATH='" + rep_file + "']")
                        shutil.copytree(source_file, rep_file,
                                        dirs_exist_ok=True)

                    else:
                        logging.info(
                            "new file copied to replica directory [FILE_NAME='" + os.path.basename(rep_file) + "'] - [COPY] - [PATH='" + rep_file + "']")
                        shutil.copy2(source_file, rep_file)

    def _removed_source_files(self, pre_files, new_source_files):
        # file removed from source
        self.sync_changes['rm'] = []
        for source_file in pre_files:
            if source_file not in new_source_files:
                # check in replica which type of file deleted
                rep_file = self.replica_path + \
                    source_file.replace(self.source_path, '')
                if (os.path.isdir(rep_file)):
                    logging.info(
                        "folder removed from source directory [FOLDER_NAME='" + os.path.basename(source_file) + "'] - [REMOVE] - [PATH='" + source_file + "']")
                else:
                    logging.info(
                        "file removed from source directory [FILE_NAME='" + os.path.basename(source_file) + "'] - [REMOVE] - [PATH='" + source_file + "']")

                self.sync_changes['rm'].append(source_file)

    def _added_source_files(self, pre_files, new_source_files):
        # file added to source
        self.sync_changes['add'] = []
        for source_file in new_source_files:
            if source_file not in pre_files:
                if os.path.isdir(source_file):
                    logging.info(
                        "new folder created in source directory [FOLDER_NAME='" + os.path.basename(source_file) + "'] - [CREATE] - [PATH='" + source_file + "']")

                else:
                    logging.info(
                        "new file created in source directory [FILE_NAME='" + os.path.basename(source_file) + "'] - [CREATE] - [PATH='" + source_file + "']")

                    # file does not have extension
                    if '.' not in source_file:
                        logging.warning('File does not have extension')

                self.sync_changes['add'].append(source_file)

    def _updated_source_files(self):
        # updated files info in source
        self.sync_changes['upt'] = []
        replica_files = self._get_all_files(self.replica_path)
        for rep_file in replica_files:
            if os.path.isdir(rep_file):
                pass
            else:
                source_file = self.source_path + \
                    rep_file.replace(self.replica_path, '')
                try:
                    if self._compare_two_files(source_file, rep_file):
                        logging.info(
                            "file updated in source directory [FILE_NAME='" + os.path.basename(source_file) + "'] - [UPDATE] - [PATH='" + source_file + "']")

                        self.sync_changes['upt'].append(source_file)

                except FileNotFoundError:
                    logging.warning(os.path.basename(
                        rep_file) + " is not in source folder")

    def _get_all_files(self, path):
        all = []
        for path, subdirs, files in os.walk(path):
            all.extend(os.path.join(path, name) for name in files)
            all.extend(os.path.join(path, dir) for dir in subdirs)
        
        return all

    def _compare_two_files(self, file1, file2):
        with open(file1, 'rb') as f1:
            with open(file2, 'rb') as f2:
                if hashlib.md5(f1.read()).hexdigest() != hashlib.md5(f2.read()).hexdigest():
                    return True
                else:
                    return False
