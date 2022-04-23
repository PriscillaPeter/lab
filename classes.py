class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        '''
        method to set the default state of the tv

        '''
        self.channel: int = Television.MIN_CHANNEL
        self.volume: int = Television.MIN_VOLUME
        self.status: bool = False

        """
        -This method is to create variable for the tv channel, volume and status. 
        """

    def power(self) -> None:
        if self.status == False:
            self.status = True
        elif self.status == True:
            self.status = False

        """
        - method to turn tv on and off.

        """

    def channel_up(self) -> None:
        self.channel += 1
        """
        - This method changes the TV channel. Should only work when tv is on
        """

    def channel_down(self) -> None:
        if self.power == True and self.channel != self.MIN_CHANNEL:
            self.channel -= 1
        else:
            self.channel = self.MAX_CHANNEL

        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """

    def volume_up(self) -> None:
        while self.power == True:
            if self.volume == self.MAX_VOLUME:
                pass
            else:
                self.volume += 1
        """
 
        - This method brings up tv volume. Should only work when tv is on. If it's 
        on MAX_VOLUME, the volume should not be adjusted
        """


    def volume_down(self) -> None:
        while self.power == True:
            if self.volume == self.MIN_VOLUME:
                pass
            else:
                self.volume -= 1
        """
        - This method brings down tv volume. Should only work when tv is on. If it's 
        on the MIN_VOLUME, the volume should not be adjusted.
        """

    def __str__(self) -> str:
        """
             TV status: Is on = True, Channel = 0, Volume = 0
             - This method should be used to return the TV status using the format shown in the comments of main.py
             """
        return f'TV Status: is on = {self.power}, Channel = {self.channel}, Volume = {self.volume}'

