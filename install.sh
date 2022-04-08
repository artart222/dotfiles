install_yay() {
    sudo pacman -S base-devel
    cd /tmp
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si
}

install_pkg() {
    LIST_OF_APPS=($(ls "/bin")+$(ls "/usr/bin"))
    IFS="|"
    if [[ "${IFS}"${LIST_OF_APPS[*]}"${IFS}" =~ "${IFS}$1${IFS}" ]]; then
        echo "$1, is installed. Checking next dependency.."
    else
        echo $1 "is not installed."
        echo "Installing" $1
        yay -S --noconfirm $1
    fi
}
