from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class IReceiver(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def format(self):
        pass


class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):
    def format(self):
        return ''.join(['<MyML>', self.text, '</MyML>'])


class Sender(ISender):
    def format(self):
        return ''.join(["I'm ", self.sender])


class Receiver(IReceiver):
    def format(self):
        return ''.join(["I'm ", self.receiver])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')

my_sender = Sender("qmal")
email.set_sender(my_sender)

my_receiver = Receiver('james')
email.set_receiver(my_receiver)

my_content = MyContent('Hello, there!')
email.set_content(my_content)

print(email)
