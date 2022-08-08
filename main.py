from time import sleep
from rich.console import Console
from rich.theme import Theme
from random import randint

theme = Theme({"success": 'green', "error": 'bold red', "info": 'bold blue', "warning": 'bold yellow'})
console = Console(theme=theme)
a, b = 1, 20


class GuessingGame:
    def __init__(self):
        self.action = None
        self.name = None
        self.games = 0
        self.computer_win, self.user_win = 0, 0

    def start(self) -> None:
        console.print('Hello guest, before starting the game you should write your name', style='warning')
        name = input('my name is: ')
        while not name:
            console.print('Please enter your name: ', style='warning')
            name = input('my name is: ')
        self.name = name
        console.print(
            f'Hello {self.name} welcome to our game in this game I think a random number and you should guess it\n'
            f'are you ready? Y/N', style='info')
        action = input('->').lower()
        self.action = True if action == 'y' else False

    @staticmethod
    def __play_again() -> bool:
        console.print('do you want to play again? Y/N', style='magenta')
        is_continue = input('->').lower()
        return True if is_continue == 'y' else False

    def user_guess(self, x: int) -> bool:
        number = randint(1, x)
        console.print(f'ok, guess the number between 0 and {x}')
        attempt = 1
        guess_number = 0
        while guess_number != number:
            guess_number = input('~# ')
            while not guess_number.isdigit():
                console.print('use only numbers', style="error")
                guess_number = input("~# ")
            guess_number = int(guess_number)
            if guess_number > number:
                console.print(f'it is lower than {guess_number}', style='warning')
                attempt += 1
            elif guess_number < number:
                console.print(f'it is greater than {guess_number}', style='warning')
                attempt += 1
        attempts = 'at once' if attempt == 1 else 'in ' + str(attempt) + ' times'
        console.print(f'congratulations you found the number {attempts}', style='success')
        self.user_win += 1
        self.games += 1
        return self.__play_again()

    def computer_guess(self, x: int) -> bool:
        console.print(f'ok, {self.name} you have 3 seconds to think a number between 1 and {x}.', style='warning')
        sleep(3)
        attempt = 1
        low = 1
        high = x
        user_answer = ''
        while user_answer != 'c':
            if low > high:
                console.print(f'Hey, {self.name} are you cheating ? i cannot guess between {low} and {high}.',
                              style='warning')
                console.print(f'it should be {low}!!!')
                break
            random = randint(low, high)
            console.print(f'is it {random} ?', style='info')
            console.print(f'Too high (H), Too low (L), Correct (C) ', style='cyan')
            user_answer = input('-> ').lower()
            if user_answer == 'h':
                attempt += 1
                high = random - 1
            elif user_answer == 'l':
                attempt += 1
                low = random + 1
        attempts = 'at once' if attempt == 1 else 'in ' + str(attempt) + ' times'
        console.print(f'Yesss! I could find your number {attempts}', style='success')
        self.computer_win = +1
        self.games += 1
        return self.__play_again()

    def game_loop(self) -> None:
        while True:
            if self.action:
                user = self.user_guess(10)
                while user:
                    user = self.user_guess(10)
                self.action = False
            else:
                console.print('do you want me to find your number ? Y/N', style='warning')
                bot = input('-> ').lower()
                if bot == 'y':
                    computer = self.computer_guess(10)
                    while computer:
                        computer = self.computer_guess(10)
                console.print('game over!!!')
                break

    def statistics(self) -> None:
        console.print(f'we have played {self.games} games in total and '
                      f'you won in {self.user_win} and i won in {self.computer_win} games')


if __name__ == '__main__':
    game = GuessingGame()
    game.start()
    game.game_loop()
    game.statistics()
