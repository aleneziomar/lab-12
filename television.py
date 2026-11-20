class Television:
    """A simple model of a television with power, mute, channel and volume controls."""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Set the television to its default state: off, unmuted, minimum channel and volume."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turn the television on if it is off, and off if it is on."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the television. Has no effect while the television is off."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Go up one channel, wrapping to the minimum channel after the maximum.

        Has no effect while the television is off.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Go down one channel, wrapping to the maximum channel below the minimum.

        Has no effect while the television is off.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase the volume by one, stopping at the maximum.

        Unmutes the television first. Has no effect while the television is off.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one, stopping at the minimum.

        Unmutes the television first. Has no effect while the television is off.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the television's state as 'Power = [status], Channel = [channel], Volume = [volume]'.

        The volume is shown as the minimum while the television is muted.
        :return: tv status.
        """
        volume = Television.MIN_VOLUME if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
