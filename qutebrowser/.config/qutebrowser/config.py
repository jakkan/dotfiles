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

# Don't swith modes automatically
# For this to not be annoying I need to always exit input mode immediately after input
# Don't automatically enter insert mode when input element is clicked
c.input.insert_mode.auto_enter = False
# Don't automatically leave intert mode when non-input element is clicked
c.input.insert_mode.auto_leave = False
# Don't automatically leave input mode when site is kinda reloaded
c.input.insert_mode.leave_on_load = False

### KEY MAPPINGS

# Editor bindings
c.editor.command = ['alacritty', '-e', 'nvim', '{}']
config.bind("gF", "view-source --edit", "normal")

# Rebind enter passthrough mode, to not accidentally enter when attempting to paste
config.unbind("<Ctrl+V>", mode="normal")
config.bind("I", "mode-enter passthrough", mode="normal")

# Binds for opening archived version of current page
config.bind('aa', 'open -t https://web.archive.org/web/*/{url}')
config.bind('ag', 'open -t https://www.google.com/search?q=cache:{url}')

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
