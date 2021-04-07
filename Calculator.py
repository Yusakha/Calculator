import wx
import main
import re

class sub(main.Calculator):
    def __init__(self, parent):
        main.Calculator.__init__(self, parent)
    
    def getValue(self):
        return self.Textarea.GetValue()

    def check(self):
        value = self.getValue()
        if re.search("[a-z]", value.lower()) or value == '0':
           return self.Textarea.SetValue("")
    def checkDot(self):
        value = self.getValue()
        if value.endswith('.'):
            self.Textarea.SetValue(value[:-1])
    # Number
    def buttonOneOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(1))
    def buttonTwoOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(2))
    def buttonTreeOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(3))
    def buttonFourOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(4))
    def buttonFiveOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(5))
    def buttonSixOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(6))
    def buttonSevenOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(7))
    def buttonEightOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(8))
    def buttonNineOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(9))
    def buttonZeroOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        self.Textarea.SetValue(value+str(0))
    def buttonDotOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        if value.endswith('.') or value.endswith(' '):
            pass
        elif re.search("[0-9]", value.lower()):
            self.Textarea.SetValue(value+str('.'))
        else:
            pass
    # Func
    def buttonPMOnButtonClick(self, event):
        value = self.getValue()
        valSplit = value.split()
        count = len(valSplit)
        if count == 0 :
            self.Textarea.SetValue('-{}'.format(value))
        elif count == 1 :
            if valSplit[0].startswith('-'):
                self.Textarea.SetValue(value[1:])
            elif re.search("[0-9]", value.lower()):
                self.Textarea.SetValue('-{}'.format(value))
        elif count == 2 :
            self.Textarea.SetValue('{}-'.format(value))
        elif count == 3 :
            if valSplit[2].startswith('-'):
                valSplit[2] = valSplit[2][1:]
                value = ' '.join(valSplit)
                self.Textarea.SetValue(value)
            elif re.search("[0-9]", valSplit[2]):
                valSplit[2] = '-{}'.format(valSplit[2])
                value = ' '.join(valSplit)
                self.Textarea.SetValue(value)
    def buttonBackOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        if value.endswith(' '):
            self.Textarea.SetValue(value[:-3])
        else:
            self.Textarea.SetValue(value[:-1])
    def buttonClearOnButtonClick(self, event):
        self.Textarea.SetValue("")
    def buttonKuadratOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        valSplit = value.split()
        count = len(valSplit)
        if (count == 1):
            result = float(value) * float(value)
            result = str(result)
            if result.endswith('.0'):
                result = result[:-2]
            self.Textarea.SetValue(str(result))
        elif (count == 2):
            result = float(valSplit[0]) * float(valSplit[0])
            result = str(result)
            if result.endswith('.0'):
                result = result[:-2]
            self.Textarea.SetValue(str(result))
        elif (count == 3):
            self.results()
    def buttonPlusOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        valSplit = value.split()
        count = len(valSplit)
        if (count == 1):
            self.Textarea.SetValue(value+str(' + '))
        elif (count == 2):
            valSplit.pop(1)
            value = ' '.join(valSplit)
            self.Textarea.SetValue(value+str(' + '))
        elif (count == 3):
            self.results()
    def buttonMinusOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        valSplit = value.split()
        count = len(valSplit)
        if (count == 1):
            self.Textarea.SetValue(value+str(' - '))
        elif (count == 2):
            valSplit.pop(1)
            value = ' '.join(valSplit)
            self.Textarea.SetValue(value+str(' - '))
        elif (count == 3):
            self.results()
    def buttonXOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        valSplit = value.split()
        count = len(valSplit)
        if (count == 1):
            self.Textarea.SetValue(value+str(' * '))
        elif (count == 2):
            valSplit.pop(1)
            value = ' '.join(valSplit)
            self.Textarea.SetValue(value+str(' * '))
        elif (count == 3):
            self.results()
    def buttonDivideOnButtonClick(self, event):
        self.check()
        value = self.getValue()
        valSplit = value.split()
        count = len(valSplit)
        if (count == 1):
            self.Textarea.SetValue(value+str(' / '))
        elif (count == 2):
            valSplit.pop(1)
            value = ' '.join(valSplit)
            self.Textarea.SetValue(value+str(' / '))
        elif (count == 3):
            self.results()
    def results(self):
        try:
            value = self.getValue()
            valSplit = value.split()
            first = float(valSplit[0])
            second = float(valSplit[2])
            operator = valSplit[1]

            for symbol in operator.lower():
                if symbol in operator.lower():
                    if symbol == '+':
                        result = first + second
                    elif symbol == '-':
                        result = first - second
                    elif symbol == '/':
                        try:
                            result = first / second
                        except ZeroDivisionError:
                            result = 'Cannot divide by zero'
                    elif symbol == 'x' or symbol == '*':
                        result = first * second
                    elif symbol == '%':
                        result = first % second
                    else:
                        return
            result = str(result)
            if result.endswith('.0'):
                result = result[:-2]
            self.Textarea.SetValue(result)
        except IndexError:
            pass 
        except ValueError:
            pass 
    def buttonResultOnButtonClick(self, event):
        self.results()

# main
app = wx.App()
frame = sub(parent=None)
frame.Show()
app.MainLoop()