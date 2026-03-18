# Mountain-Climber

**Mclimber** is a OSINT tool specifically for finding given data around the web and dark web. no exact data-specific terms needed, but they can be provided, and are recommended. 

## Features
 - Works with almost any given data
 - Searches breach directories, paste sites, image hosters, search engines, social media, ect.
 - Typer version available
 - Cross matching Hashes with data using weekpass and collections of wordlist files.
 - Data returned can be sorted manually, or automatically
 - More coming soon!



## Usage (so far)
```
    __   __  __             _____ _ _           _                __   
   / /  |  \/  |           / ____| (_)         | |               \ \  
  / /   | \  / |  ______  | |    | |_ _ __ ___ | |__   ___ _ __   \ \ 
 < <    | |\/| | |______| | |    | | | '_ ` _ \| '_ \ / _ \ '__|   > >
  \ \   | |  | |          | |____| | | | | | | | |_) |  __/ |     / / 
   \_\  |_|  |_|           \_____|_|_|_| |_| |_|_.__/ \___|_|    /_/
    Find the information you want (theres a lot) the best you can.

- search  [DATA] // searches everything in reach for given data. 
- search -m [name@domain]  // searches everything for the email provided.
- search -n [FIRST, LAST] // searches everything name specific per name provided

- search -u [username] // searches everything username specific (like social media) for said username.
- search -s [sensitive data] // searches sensitive data throughout breaches and data dumps, also pulling direct text matches from search engines.
- search -h [hash] // First tries to match the hash using weakpass and other various wordlists, if no match is provided, hash will be searched in breach directories.

  -s // searches through a specific service category 
  -v // verbose output, records everything to file / terminal.
  -l // Log search to a log file

- logfile // creates logfile if there isn't one, or just lists the file path
- logfile -f [file path] // sets file for logs to be written to.
- logfile -r // resets logfile if there is one.

- add [type] [object] // adds information source
      [api] [key?] // adds given api and key if one is needed. limited feature.
      [wordlist] [path] // adds given wordlist to search.
      [dump] // adds given dump to search

- match [search1] [search2] // cross references two different searches to see if any data could be related. (matches a password through likeliness or other given data through various methods. )
                                                                      
 this feature will be worked on more soon                                                                     


```


## Note
Since the tool can be very generalized, its recommended when searching for a specific thing (like a person or breach) that you make sure to provide as much detail as possible. 

also this uses a lot of amazing OSINT tools that would actually probably be better if you used them stand alone, but the advantage here is how the data is processed and sorted, and being able to generalize the search range.


