import re
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class MakeButtons:
    """
    Create buttons from list
    """

    def makebuttons(self, set1: list, set2: list, isUrl=False, isCallback=True,rows = 1):
        self._set1 = set1.copy()
        self._set2 = set2.copy()
   #self._set3 = set3.copy()   #Added By Fazanul
   #self._set4 = set4.copy()   #Added By Fazanul
   #self._set5 = set5.copy()   #Added By Fazanul

        self._isUrl = isUrl
        self._isCallback = isCallback
        self.rows = rows
        return self._make()

    def _make(self):
        butt = []
        if self._isUrl:
            while self._set1:
                buttons = []
                for i in range(self.rows):
                    if len(self._set1) != 0:
                        buttons.append(
                            InlineKeyboardButton(text=self._set1[0], url=self._set2[0])
                        )
                        self._set1.pop(0)
                        self._set2.pop(0)
                       
                    
                    
                 #self._set3.pop(0)   #Added By Fazanul
                 #self._set4.pop(0)   #Added By Fazanul
                 #self._set5.pop(0)   #Added By Fazanul
                
                butt.append(buttons)
        if self._isCallback:
            while self._set1:
                buttons = []
                for i in range(self.rows):
                    if len(self._set1) != 0:
                        buttons.append(
                            InlineKeyboardButton(
                                text=self._set1[0], callback_data=self._set2[0]  #comma added
                                
             #text=self._set3[0], callback_data=self._set4[0]
                                
                            )
                        )
                        self._set1.pop(0)
                        self._set2.pop(0)
                        
                   #self._set3.pop(0)
                   #self._set4.pop(0)
                    
                butt.append(buttons)
        return butt
