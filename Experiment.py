class Outer():
    @staticmethod
    def fish():
        print('Fish!')


class Inner(Outer):
    def test_fish(self, greeting):
        print(greeting)
        self.fish()

z = Inner()
z.test_fish('Hello')