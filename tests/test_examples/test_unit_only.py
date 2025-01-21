from conftest import describe, it

@describe("Silly Unit Tests")
class TestSillyUnitTests:
    @it("Should validate hello world")
    def test_hello_world(self, capsys):
        """
        The goal of this Challenge is to write a short program in Python that 
        prints out the phrase "Hello world!"
        """
        # Execute the actual print statement - this is the code we're testing
        print("Hello World!")
        
        # Get the captured output and verify it
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello World!"

    @it("Should validate comments")
    def test_comments(self, capsys):
        """
        The goal of this Challenge is to write a short program in Python that 
        comments out the print statement that prints "Hello world!"
        """
        # observe comments are # and als""
        # print("Hello World!")
        
        # Get the captured output and verify it
        captured = capsys.readouterr()
        # The output should not contain "Hello World!"
        assert captured.out.strip() != "Hello World!"
      

    @it("Should validate types")
    def test_types(self, capsys):
        """
        The goal of this Challenge is to verify Python's basic data types
        """
        # None type
        assert type(None) is None.__class__

        # Boolean types
        assert type(True) is bool
        assert type(False) is bool

        # Numeric types
        assert type(1) is int
        assert type(1.0) is float

        # String types (all variations are str type)
        assert type("Hello") is str
        assert type('Hello') is str
        assert type("""Hello""") is str
        assert type('''Hello''') is str

        # isinstance is a built-in function that checks if an object is an instance of a class
        assert isinstance(None, type(None))
        assert isinstance(True, bool)
        assert isinstance(1, int)
        assert isinstance(1.0, float)
        assert isinstance("Hello", str)

@describe("Arithmetic Operators")
class TestArithmeticOperators:
    @it("Should validate basic arithmetic operators")
    def test_basic_arithmetic(self):
        # Addition
        assert 5 + 3 == 8
        assert 5.0 + 3 == 8.0  # Note the float result
        assert -10 + 10 == 0 # note the negative first operand
        
        # Subtraction
        assert 10 - 4 == 6
        assert 10 - 3.4 == 6.6
        assert 5 - 8 == -3
        
        # Multiplication
        assert 3 * 4 == 12
        
        # Division (always returns float)
        assert 8 / 2 == 4.0
        assert 10 / 5 == 2.0

    @it("Should validate advanced operators")
    def test_advanced_operators(self):
        # Integer division
        assert 7 // 2 == 3
        
        # Modulus (remainder)
        assert 7 % 3 == 1
        
        # Exponentiation
        assert 2 ** 3 == 8

    @it("Should validate operator precedence")
    def test_operator_precedence(self):
        # PEMDAS demonstration
        result = 2 + 3 * 4
        assert result == 14  # multiplication happens before addition
        
        result = (2 + 3) * 4
        assert result == 20  # parentheses override normal precedence