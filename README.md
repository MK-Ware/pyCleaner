# pyCleaner
Securely wipe files or folders and clean duplicated files

# Screenshots
[![py_Cleaner_1.jpg](https://s14.postimg.org/3qc5zmudt/py_Cleaner_1.jpg)](https://postimg.org/image/k1c9vy6vh/)
<br />
[![py_Cleaner2_1.jpg](https://s14.postimg.org/79y3phmtt/py_Cleaner2_1.jpg)](https://postimg.org/image/fs7jtttcd/)

# Features
- Simple, user friendly GUI.
- Cross platform.
- Secure file deletion with multiple passes.
- Scan directories or whole drives for duplicated files.
- Choice between secure wiping or normal deletion for dealing with duplicated files.
- Uses md5 hashing and file size to detect duplicate files.
- No realistic chance of false positives (see below).
- Available as a pre compiled Windows binary, or a Python script for Linux in the releases tab.

# Is it possible for the program to make false detections?
Short answer: No.

Long version: The program uses md5 hashing with file size checking to detect duplicated files. What are the odds of 2 different files of different sizes generating the same md5 hash code? Negligibly small! md5 is a 128-bit hash, so the odds of 2 different files generating identical md5 sums are 1 / 2^128.. That's 1 / 340282366920938463463374607431768211456. In other words, you'd need to have 2^64 files on your computer before there's a 10% chance. Even if those were 1KB text files they would require 16384 Exabytes of storage capacity. In short, it isn't happening.

# If you like it, don't forget to star the repo!
