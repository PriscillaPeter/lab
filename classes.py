class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        '''
        method to set the default state of the tv: it creates variable for the tv channel, volume and status.

        '''
        self.channel: int = Television.MIN_CHANNEL
        self.volume: int = Television.MIN_VOLUME
        self.status: bool = False


    def power(self) -> None:

        """
        - method to turn tv on and off.

        """

        if self.status == False:
            self.status = True
        elif self.status == True:
            self.status = False


    def channel_up(self) -> None:
        """
        - If the tv is on, this method turns the tv channel up.
        """
        if self.power == True and self.channel == Television.MAX_CHANNEL:
            self.channel = Television.MIN_CHANNEL
        else:
        self.channel += 1


    def channel_down(self) -> None:

        """
        - If the tv is on, this method turns the tv channel down.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.power == True and self.channel != self.MIN_CHANNEL:
            self.channel -= 1
        else:
            self.channel = self.MAX_CHANNEL


    def volume_up(self) -> None:
        """
         - If the tv is on, this method turns the tv volume up.
        - If on MAX_VOLUME, the volume should not change
        """
        while self.power == True:
            if self.volume == self.MAX_VOLUME:
                pass
            else:
                self.volume += 1



    def volume_down(self) -> None:
        """
        - If the tv is on, this method turns the tv volume down.
        -If on the MIN_VOLUME, the volume should not be adjusted.
        """
        while self.power == True:
            if self.volume == self.MIN_VOLUME:
                pass
            else:
                self.volume -= 1


    def __str__(self) -> str:
        """
             TV status: Is on = True, Channel = 0, Volume = 0
             - This method should return the TV status
             """
        return f'TV Status: is on = {self.power}, Channel = {self.channel}, Volume = {self.volume}'

