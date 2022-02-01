if [[ $(setxkbmap -query | grep "layout:\s" | awk '{print $2}') == "us" ]]; then
    setxkbmap de
elif [[ $(setxkbmap -query | grep "layout:\s" | awk '{print $2}') == "de" ]]; then
    setxkbmap fr
elif [[ $(setxkbmap -query | grep "layout:\s" | awk '{print $2}') == "fr" ]]; then
    setxkbmap ir
elif [[ $(setxkbmap -query | grep "layout:\s" | awk '{print $2}') == "ir" ]]; then
    setxkbmap us
fi
