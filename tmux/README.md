# Tmux dotfiles

## How I use tmux

I use tmux primarily for local sessions.

The features I use are:
- Persistent sessions
- Terminal tabs (terminal multiplexing)
- Copy mode

There are terminal emulators that offer tabs and copy mode features. In the future I can see myself dropping tmux for local sessions and using the tabs and copy mode features of a terminal emulator instead. But for now I'm happy with how tmux works.

In principle tmux is also my tool for terminal pair programming and remote sessions, but I haven't had the need for that yet.

## Design decisions

- I use i3/sway with the GUI modifier. I use tmux with ALT for a clean separation.
- Already using i3/sway, panes don't offer enough value for me to add them to my workflow. I use the 'ta' script to be able to open different tabs from the same session side by side. Every time I attach to a session I create a temporary session that is linked to a session group with the specified name.  
- Common actions are also mapped in the root table, to keys that I don't use in any cli application today.

