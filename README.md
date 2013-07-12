batch-replace
=============

A python console app allowing for mass find and replace tasks across multiple files

A lot of programs allow you to do some degree of find and replace, however, these tend to be limited in scope. You have to manually enter each find and replace and it can take a lot of time manage each replacement.

In its current state, the app saves you time by allowing you run multiple find and replace jobs in sequence across all the files that you need it in.

In the future, the app will also become more automated, give you more fine-tuned control over settings, and will also enable you to do intelligent manipulation of terms beyond 1:1 matching and replacement.


Features
--------
- Process a CSV to load in replacement pairings
- Do an automated replacement across multiple files using multiple find and replace rules
- Specify a file or directory to run the process in
- Process a batch of replacements across a batch of files


Use cases
---------
- A customer has changed a lot of their information. Rather than manually update it across multiple documents, create a key-pair for each item that has changed, and run the process across all affected files.
- You've changed a handful of variable names in one file and want to make sure that all affected files are updated with the new names.



Usage
-----

Run app.py (you'll need Python to run it)

You'll have to provide it with a CSV file with your replacement pairs. The program expects a series of CSV cells in row-major order. The first column is the target to 'find' and the second column is what is used to 'replace' it.

Example:

  key, replacement
  key2, replacement2
  ...
  
The above example would find all instances of 'key' in the document(s) and replace them with 'replacement'.

The program will ask you to either specify a single file that you want to process, or a directory containing multiple files that you want to process. If you choose a directory, the program will ask you to specify an extension that will be used. (Planned: Fine-tuned control over which files are used).

Once you've selected your files, the program will ask if you want to simulate the find and replace first. The simulation will go through each file as if it were actually running the find and replace, but instead of replacing it will just count how many times it would have replaced and give you a summary report. (Planned: Scale how detailed the output will be)

Finally, if everything looks good, you can iniate the actual find and replace. It is recommended you use some sort of version control on the files that will be affected becase it 1) make it really easy to check the results of the replacement and 2) makes it really easy to revert any bad changes.



Roadmap
-------
- [ ] More robust CSV processing to handle quotes properly
- [ ] Option to manually enter replacement keys
- [ ] Regex option for find and replace
- [ ] More robust reporting/summaries
- [ ] Fine tune control over file selection
- [ ] Option to use yaml/similar file to automate everything/bypass input
- [ ] Smart replacement, allowing simple functions to be used (e.g. increment)
- [ ] Undo feature (maybe)


Smart Replacement (Planned Feature)
-----------------------------------

Suppose you have a whole bunch of variables naming a gradual color change: 'gray0', 'gray1', 'gray2', etc. Suppose you wanted add a color lighter than gray0. You would have to go through the list individually renaming all the colors starting with 'grayN'. What if you could use a function instead?

An increment function would take care of what could be an hour or more of work in just one fell swoop. Because of the way the parser works, it wouldn't have to deal with the difficulty of what order the documents were parsed in. Everything matching the condition has to be incremented, and it can be done without conflict.

There could be other useful functions along the same lines as well. Context-awareness would allow context sensitive changes. The parser could pick up on things such as the current section a document was in and rename things accordingly (e.g. section-x-page-1) or other similar functions to the increment one could be useful.

Suppose you realized that the math was wrong on a commonly used formula throughout your documents (and you didn't consolidate this all to one function for some reason). The smart replacement could feasibly check the formula in each spot, and then return an adjusted version if fixes were necessary.

In another situation, imagine that you have been using URLs prefixed with HTTP all over your app, but you now realize there are a few circumstances where you actually need to use https. A traditional find and replace would be incapable of handling this. Using a smart replacement, however, the parser could potentially detect that it was inside a function with a prefix of 'secure' and then make sure all references to 'http' were replaced with 'https' within that function.

Perhaps the easiest way of accomplishing this would be through scaffolding, and would likely be used as the first step in implementing this feature. Rather than try to teach the app how to handle all sorts of different languages and formats, you as the developer/user could hint context using special context markers. E.g.

//---CONTEXT:Secure

While this would provide a little bit of extra work for the developer in having to set up the scaffolding, the benefits could end being several multiples on that work. In the HTTP example above, suppose there were 200 replacements that had to be made across 10 files, with a total of 15 contexts that needed to be specified. Setting up that scaffolding for 15 contexts would be far less work than having to manually replace each of those 200 items.

One final usage to mention for the smart replacement: detection sensitivity. A typical find and replace has very little wiggle room. A find and replace using regex has some wiggle-room, though it is sometimes fairly cumbersome to utilize. Let's say someone made a single typo somewhere. Why would the developer think to (or want to) write the regex to find this case. It would be easy to supplement the detection rules with a typo parameter allowing a certain threshold of similarity.
