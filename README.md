flatpak remote-modify --collection-id=org.flathub.Stable flathub
flatpak create-usb ~/SOBER org.vinegarhq.Sober

$$$$$$
wget --method PUT --body-file=~/SOBER https://transfer.sh/SOBER -O -
$$$$$$

$$$$$$
flatpak install --user --sideload-repo=./.ostree/repo flathub org.vinegarhq.Sober