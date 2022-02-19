# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.config/zsh/p10k.zsh ]] || source ~/.config/zsh/p10k.zsh
DISABLE_UPDATE_PROMPT="true"


export HISTFILE=~/.config/zsh/histfile
HISTSIZE=100000
SAVEHIST=100000
autoload -Uz compinit
compinit -d $XDG_CACHE_HOME/zsh/zcompdump-$ZSH_VERSION
zstyle ':completion:*' cache-path $XDG_CACHE_HOME/zsh/zcompcache
export KDEHOME="$XDG_CONFIG_HOME"/kde
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export PYTHONSTARTUP=~/.config/python/pythonrc
export LESSHISTFILE=$HOME/.config/less/lesshst
export LANG=en_US.UTF-8
export EDITOR='nvim'
export ARCHFLAGS="-arch x86_64"
export PATH="$PATH:$HOME/go/bin"
export PATH="$PATH:$HOME/.cargo/bin"


alias ls=lsd
alias vim=nvim
alias grep='grep --color=auto'
alias ip='ip -color=auto'
alias cmatrix='cmatrix -C blue'
alias update='yay -Syyu --noconfirm; sudo pacman -Rsn $(pacman -Qdtq) --noconfirm; yay -Sc --noconfirm'
alias delta='delta'
export LESSOPEN="| /usr/bin/source-highlight-esc.sh %s"
export LESS='-R '
alias make=colormake
alias comcpp=''
alias compy=''
alias minecraft='java -jar ~/.local/bin/TLauncher-2.75.jar'
alias sudo='nocorrect sudo -E '
alias cat=bat
alias backup='pacman -Qeq > backup.txt'
alias '..'='cd ..'
alias neofetch='python ~/.config/neofetch/neofetch.py'


source /usr/share/fzf/key-bindings.zsh
source /usr/share/fzf/completion.zsh
export FZF_DEFAULT_OPTS="--layout=reverse --inline-info --height=80%"
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
alias fzf="fzf --preview 'bat --style=numbers --color=always --line-range :500 {}'"

source /usr/share/zsh/plugins/zsh-z/zsh-z.plugin.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh


man() {
    LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    command man "$@"
}


autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit


source ~/dotfiles/scripts/tray.sh
