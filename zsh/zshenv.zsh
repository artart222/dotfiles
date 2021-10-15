ZDOTDIR=$HOME/.config/zsh
_Z_DATA=$HOME/.cache/zsh/z
GIT_CONFIG=$XDG_CONFIG_HOME/git/config
export XAUTHORITY="$XDG_RUNTIME_DIR"/Xauthority
CARGO_HOME=$XDG_CONFIG_HOME/rust/cargo

if [ -r ~/.config/zsh/zshrc.zsh ]; then
    source ~/.config/zsh/zshrc.zsh
fi


if [ -r ~/.config/zsh/zprofile.zsh ]; then
    source ~/.config/zsh/zprofile.zsh
fi
