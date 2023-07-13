# Set xdg config and xdg cache environmental variables
XDG_CONFIG_HOME=$HOME/.config
XDG_CACHE_HOME=$HOME/.cache

# Set zsh environmental variables
ZDOTDIR=$XDG_CONFIG_HOME/zsh
_Z_DATA=$XDG_CACHE_HOME/zsh/z

# Set display environmental variable
export DISPLAY=:0

# Loading other zsh files
if [ -r $ZDOTDIR/zshrc.zsh ]; then
  source $ZDOTDIR/zshrc.zsh
fi
if [ -r $ZDOTDIR/zprofile.zsh ]; then
  source $ZDOTDIR/zprofile.zsh
fi
