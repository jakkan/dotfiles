### BEHAVIOR

# Load config from file only, not from browser - quickmarks and bookmarks are not part of config.
config.load_autoconfig(False)

# Spellcheck
# disbled until next release because of bug 
# /usr/share/qutebrowser/scripts/dictcli.py install en-US
# c.spellcheck.languages = ["en-US", "sv-SE"]

# Save session tabs on close
c.auto_save.session = True

# Autoplay video
c.content.autoplay = False

# It is possible to whitelist domains instead for these options
c.content.javascript.can_access_clipboard = True
c.content.notifications.enabled = True

# Close browser when last tab is closed
c.tabs.last_close = "close"

### APPEARANCE

c.zoom.default = 100

c.fonts.completion.category = "10pt bold Hack Nerd Font"
c.fonts.completion.entry = "10pt Hack Nerd Font"
c.fonts.debug_console = "10pt Hack Nerd Font"
c.fonts.default_family = "Hack Nerd Font"
c.fonts.downloads = "10pt Hack Nerd Font"
c.fonts.hints = "bold 10pt Hack Nerd Font"
c.fonts.keyhint = "10pt Hack Nerd Font"
c.fonts.messages.error = "10pt Hack Nerd Font"
c.fonts.messages.info = "10pt Hack Nerd Font"
c.fonts.messages.warning = "10pt Hack Nerd Font"
c.fonts.prompts = "10pt Hack Nerd Font"
c.fonts.statusbar = "10pt Hack Nerd Font"
c.fonts.tabs.selected = "10pt Hack Nerd Font"
c.fonts.tabs.unselected = "10pt Hack Nerd Font"

c.colors.webpage.preferred_color_scheme = "dark"

# Show tab numbor to make it easier to jump to tab number
c.tabs.title.format = '{private} {current_title}'

# Show tab bar only when there is more than 1 tab
c.tabs.show = "multiple"

### URLS

# search engines
c.url.searchengines = {
    "DEFAULT": "https://google.com/search?q={}",
    "d": "https://duckduckgo.com/?q={}",
    "r": "https://reddit.com/r/{}",
    'w': 'https://en.wikipedia.org/wiki/{}',
    'gh': 'https://github.com/search?q={}',
    "g": "https://google.com/search?q={}",
    "gm": "https://www.google.com/maps/search/{}",
    "y": "https://www.youtube.com/results?search_query={}"
}

# Default page in new tabs
c.url.default_page = "about:blank"


### MODES

# Prefix key bindings that I may regret: https://qutebrowser.org/doc/help/settings.html#bindings.commands
c.bindings.default['normal'] = {}
c.bindings.commands['normal'] = {
    # restore defaults
	'=': 'zoom-in',
	'-': 'zoom-out',

	'/': 'set-cmd-text /',
    ':': 'set-cmd-text :',
    '?': 'set-cmd-text ?',

    '<alt-1>': 'tab-focus 1',
    '<alt-2>': 'tab-focus 2',
    '<alt-3>': 'tab-focus 3',
    '<alt-4>': 'tab-focus 4',
    '<alt-5>': 'tab-focus 5',
    '<alt-6>': 'tab-focus 6',
    '<alt-7>': 'tab-focus 7',
    '<alt-8>': 'tab-focus 8',
    '<alt-9>': 'tab-focus 9',

    '<alt-m>': 'tab-mute',

	'<ctrl-u>': 'scroll-page 0 -0.5',
	'<ctrl-d>': 'scroll-page 0 0.5',
	'<ctrl-b>': 'scroll-page 0 -1',
	'<ctrl-f>': 'scroll-page 0 1',

	'<ctrl-n>': 'open -w',
	'<ctrl-t>': 'open -t',
    'o': 'set-cmd-text -s :open',
    'O': 'set-cmd-text -s :open -t',

    '<ctrl-v>': 'mode-enter passthrough',
    'V': 'mode-enter caret ;; selection-toggle --line',
    'v': 'mode-enter caret',

    'N': 'search-prev',
    'n': 'search-next',

    'f': 'hint',
    'gg': 'scroll-to-perc 0',
    'G': 'scroll-to-perc',
	'u': 'undo',
    
	'yy': 'yank',
	'yt': 'yank title',

    # prefix
	'<ctrl-a>H': 'back',
	'<ctrl-a>J': 'tab-next',
	'<ctrl-a>K': 'tab-prev',
	'<ctrl-a>L': 'forward',

	'<ctrl-a>d': 'tab-close',
	'<ctrl-a>r': 'reload',
}

# Make active/inactive colors consistent with i3 and tmux config
c.colors.tabs.even.bg = "#333333"
c.colors.tabs.odd.bg = "#333333"
c.colors.tabs.even.fg = "#FFFFFF"
c.colors.tabs.odd.fg = "#FFFFFF"
c.colors.tabs.selected.even.bg = "#008800"
c.colors.tabs.selected.odd.bg = "#008800"
c.colors.tabs.selected.even.fg = "#FFFFFF"
c.colors.tabs.selected.odd.fg = "#FFFFFF"
c.colors.tabs.even.bg = "#333333"
c.colors.tabs.odd.bg = "#333333"
c.colors.tabs.even.fg = "#FFFFFF"
c.colors.tabs.odd.fg = "#FFFFFF"
