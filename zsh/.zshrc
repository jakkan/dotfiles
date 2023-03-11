### PROMPT

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

ZSH_THEME="powerlevel10k/powerlevel10k"

### VI MODE

export VISUAL=nvim
export EDITOR=nvim

VI_MODE_RESET_PROMPT_ON_MODE_CHANGE=true
VI_MODE_SET_CURSOR=true

# In vi input mode, it takes 0.4 s for Esc to take effect, this changes to 10ms: https://superuser.com/questions/1579208/delay-after-hitting-escape
KEYTIMEOUT=1

# Add useful emacs-like bindings in vi insert mode
bindkey -M viins '\ef' forward-word
bindkey -M viins '\eb' backward-word
bindkey -M viins '^e' end-of-line
bindkey -M viins '^a' beginning-of-line
bindkey -M viins '\ed' kill-word
bindkey -M viins '^w' backward-kill-word
bindkey -M viins '^k' kill-line
# By default ^u is mapped to backward-kill-line in bash and kill-whole-line in zsh
bindkey -M viins '^u' backward-kill-line

### PLUGINS (VI, NODE, FZF)

export ZSH=$HOME/.oh-my-zsh
export  NVM_LAZY_LOAD=true
plugins=(vi-mode zsh-z zsh-syntax-highlighting zsh-autosuggestions fzf zsh-nvm)
source $ZSH/oh-my-zsh.sh

### SEARCH

# GLOBDOTS lets files beginning with a . be matched without explicitly specifying the dot
setopt globdots

# Use fd for fzf
export FZF_DEFAULT_COMMAND='fd --type file --follow --hidden --exclude .git'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"

### PATH

# User scripts
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# Aliases to make life easier
alias vim=nvim
alias v=nvim
alias lz=lazygit
alias ls=exa
alias cat=batcat
alias grep=rg
alias find=fd

# Aliases to make original tools possible to access
alias vim_=/usr/bin/vim
alias ls_=/usr/bin/ls
alias cat_=/usr/bin/cat
alias grep_=/usr/bin/grep
alias find_=/usr/bin/find

# Go
export PATH=$PATH:/usr/local/go/bin

# Markdown notes
export ZK_NOTEBOOK_DIR=$HOME/Notes

# Python
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
