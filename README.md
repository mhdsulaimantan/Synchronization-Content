# Synchronization-Content
## Overview:
This is a simple synchronization program between two folders (source and replica). The project was built using python==3.10.5. it contains four main features:
  - **Source:** The folder where data will be monitored and synced from.
  - **Replica:** The folder where data will be copied and synced to.
  - **Log:** Report and track the sync process.
  - **Period:** Time wanted to repeat the sync process.

## How it works:
1. When the user run the program, it will ask him to enter some informations (using command line):
   - **Log path** 
   - **Source path**
   - **Replica path**
   - **Period**
  
    `Note: The program will create a log file automatically if it does not exist in the provided path.`
 2. The synchronization process will start by copying the data from the source to the replica directory.
 3. The program will track any changes that happened in the source dir. Those changes could be: ***create***, ***remove*** files/folders or ***update*** the content inside an already exist file.
 4. The log system will report the changes into the log file and the command line.
 5. it is a one-way process, which means any changes in the replica will not apply to the source directory.
 6. The table below describes the context of a log message:
     
     <table>
        <tr>
          <td><b>Date</b></td>
          <td><tt>fixed</tt></td>
          <td>The date when the log message was created. <b>[dd/mm/yyyy HH:MM:SS]</b></td>
        </tr>
        <tr>
          <td><b>Log Level</b></td>
          <td><tt>fixed</tt></td>
          <td><b>INFO</b> - <b>ERROR</b> - <b>WARNING</b></td>
        </tr>
        <tr>
          <td><b>Message</b></td>
          <td><tt>fixed</tt></td>
          <td>Description for the log message</td>
        </tr>
        <tr>
          <td><b>Name</b></td>
          <td><tt>optional</tt></td>
          <td>The name of the item (file/folder) where the changes occured.</td>
        </tr>
        <tr>
          <td><b>Operation</b></td>
          <td><tt>optional</tt></td>
          <td>The type of sync process. <b>CREATE</b> - <b>REMOVE</b> - <b>COPY</b> - <b>UPDATE</b></td>
        </tr>
        <tr>
          <td><b>Path</b></td>
          <td><tt>optional</tt></td>
          <td>The path to the item (file/folder)</td>
        </tr>
    </table>
  
7. **Log Level** commands:
```diff
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
+ INFO: Confirmation that things are working as expected.
! WARNING: An indication that something unexpected happened, or indicative of some problem in the near future.The software is still working as expected.
```
8. The table below shows all log messages that may occure during the sync process:
   
   <table>
     <tr>
        <td><b>Log level</b></td>
        <td><b>Message</b></td>
        <td><b>Operation type</b></td>
      </tr>
      <tr>
          <td>INFO</td>
          <td>Synchronization started</td>
          <td>-</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>source files copied to replica directory</td>
          <td>[COPY]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>folder removed from source directory</td>
          <td>[REMOVE]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>file removed from source directory</td>
          <td>[REMOVE]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>folder removed from replica directory</td>
          <td>[REMOVE]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>file removed from replica directory</td>
          <td>[REMOVE]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>new folder copied to replica directory</td>
          <td>[COPY]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>new file copied to replica directory</td>
          <td>[COPY]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>new folder created in source directory</td>
          <td>[CREATE]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>new file created in source directory</td>
          <td>[CREATE]</td>
        </tr>
        <tr>
          <td>INFO</td>
          <td>file updated in source directory</td>
          <td>[UPDATE]</td>
        </tr>
        <tr>
          <td>WARNING</td>
          <td>The path is not found</td>
          <td>-</td>
        </tr>
        <tr>
          <td>WARNING</td>
          <td>The period is not a number</td>
          <td>-</td>
        </tr>
        <tr>
          <td>WARNING</td>
          <td>File does not have extension</td>
          <td>-</td>
        </tr>
        <tr>
          <td>WARNING</td>
          <td><tt>File name</tt> is not in source folder</td>
          <td>-</td>
        </tr>
        <tr>
          <td>WARNING</td>
          <td>The source and replica paths should not be equal</td>
          <td>-</td>
        </tr>
        <tr>
          <td>ERROR</td>
          <td><tt>error message context</tt></td>
          <td>-</td>
        </tr>
    </table>
    
 ## Run and installation:
 - Clone the repository: `git clone repo`
 - Navigate to the project path and run: `python main.py`
 - Enter the required information and start testing.

