# tree_generator

Recursively goes through a directory and generates an ASCII art tree. I find this useful for my git repos. 

## Running tree_generator

- Execute as follows: `python tree_generator.py /path/to/target_directory /path/to/output/directory/output.txt`

- To ignore hidden directories (like .git, etc.): `python tree_generator.py /path/to/target_directory /path/to/output/directory/output.txt --ignore-hidden`

### Outputs 

#### Without hidden directores 
<pre>
├── README.md
├── outputs
│   └── output_tree.txt
└── tree_generator.py
</pre>
#### Including hidden directories 
<pre>
├── .git
│   ├── HEAD
│   ├── branches
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │   │   ├── heads
│   │   │       └── main
│   │   │   └── remotes
│   │   │       └── origin
│   │   │           └── HEAD
│   ├── objects
│   │   ├── info
│   │   └── pack
│   │   │   ├── pack.idx
│   │   │   └── pack.pack
│   ├── packed-refs
│   └── refs
│   │   ├── heads
│   │       └── main
│   │   ├── remotes
│   │       └── origin
│   │       │   └── HEAD
│   │   └── tags
├── README.md
├── outputs
│   └── output_tree.txt
└── tree_generator.py
</pre>

#### NOTES

tree_generator will append the start and end of each tree with `<pre></pre>` tags in order to create a a preformatted block of text suitable for Markdown in Git. If these tags are not used, Git will format it all into a wall of text. 




