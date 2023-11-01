# Speak Up
Speak Up Magazines archive.

## Change online references

Audio attachments are stored in git and linked in the md/html files.
When the repository changes, these need to be updated:

```bash
find /home/www \( -type d -name .git -prune \) -o -type f -print0 | xargs -0 sed -i 's/subdomainA\.example\.com/subdomainB.example.com/g'
```

`-print0` tells `find` to print each of the results separated by a null character, rather than a new line. In the unlikely event that your directory has files with newlines in the names, this still lets `xargs` work on the correct filenames.

`\( -type d -name .git -prune \)` is an expression which completely skips over all directories named `.git`. You could easily expand it, if you use SVN or have other folders you want to preserve -- just match against more names. It's roughly equivalent to `-not -path .git`, but more efficient, because rather than checking every file in the directory, it skips it entirely. The `-o` after it is required because of how `-prune` actually works.

For more information, see `man find`

**Example:**

```bash
find . -type f -print0 | xargs -0 sed -i 's/knowledge-base\/main\/English\/SpeakUp/speakup\/main/g'
```