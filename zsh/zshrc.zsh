# Set apps config location environmental variables
GIT_CONFIG=$XDG_CONFIG_HOME/git/config
GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
# XAUTHORITY="$XDG_CONFIG_HOME"/Xauthority
KDEHOME=$XDG_CONFIG_HOME/kde
PYTHONSTARTUP=$XDG_CONFIG_HOME/python/pythonrc
LESSHISTFILE=$XDG_CONFIG_HOME/less/lesshst
LANG=en_US.UTF-8
EDITOR='nvim'
ARCHFLAGS="-arch x86_64"

# Set less settings.
export LESS='-R '
export LESSOPEN="| /usr/bin/source-highlight-esc.sh %s"

# Add some items to path
PATH="$PATH:$HOME/go/bin"
PATH="$PATH:$HOME/.cargo/bin"
PATH="$PATH:$HOME/.local/share/nvim/mason/bin/"

# export PYTHONPATH=/home/artin/.local/share/nvim/mason/packages/:$PYTHONPATH

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
source "$XDG_CACHE_HOME/p10k-instant-prompt-$USER.zsh"
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f $ZDOTDIR/p10k.zsh ]] || source $ZDOTDIR/p10k.zsh
DISABLE_UPDATE_PROMPT="true"

# Set history file settings.
export HISTFILE=$ZDOTDIR/histfile
HISTSIZE=100000
SAVEHIST=100000

# Set vim key-bindings.
bindkey -v

# Set some aliases
alias ls=lsd
alias vim=nvim
alias nv=nvim
alias cat=bat
alias make=colormake
alias grep='grep --color=auto'
alias ip='ip -color=auto'
alias cmatrix='cmatrix -C blue'
alias sudo='nocorrect sudo -E '
alias '..'='cd ..'
alias backup='pacman -Qeq > backup.txt'
alias minecraft='java -jar ~/.local/bin/TLauncher-2.75.jar'
alias update='yay -Syyu --noconfirm; sudo pacman -Rsn $(pacman -Qdtq) --noconfirm; yay -Sc --noconfirm'
alias neofetch='python $XDG_CONFIG_HOME/neofetch/neofetch.py'
alias comcpp=''
alias compy=''

# FZF
source /usr/share/fzf/key-bindings.zsh
source /usr/share/fzf/completion.zsh
export FZF_DEFAULT_OPTS="--layout=reverse --inline-info --height=80%"
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
alias fzf="fzf --preview 'bat --style=numbers --color=always --line-range :500 {}'"

# Z plugins for easy jumping from a directory to another directory.
source /usr/share/zsh/plugins/zsh-z/zsh-z.plugin.zsh

# Syntax highlighting.
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Set auto compilation
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
autoload -Uz compinit
compinit -d $XDG_CACHE_HOME/zsh/zcompdump-$ZSH_VERSION
zstyle ':completion:*' cache-path $XDG_CACHE_HOME/zsh/zcompcache
zstyle ':completion:*' menu select

# Add colors to man pages.
man() {
  LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    command man "$@"
}

# PROXY_FILE_ADDR=$HOME/proxy.txt
# if [[ -f ~/proxy.txt ]]; then
  # If I'm connected to my galaxy s23+
  # if [[ $(nmcli -t -f name,device connection show --active | grep wlp3s0 | cut -d\: -f1) == "Artin's Galaxy S23+" ]]; then
    # export https_proxy=$(bat -p $PROXY_FILE_ADDR)
    # export http_proxy=$(bat -p $PROXY_FILE_ADDR)
  # fi
# fi
