# Password Strength Checker

The Password Strength Checker is a Python script that assesses the strength of passwords based on various criteria such as length, complexity, common patterns, and known weak passwords. It calculates the entropy of a password to estimate its strength and provides recommendations for stronger passwords.

## Features

- Checks the strength of a password based on length, complexity, and patterns.
- Considers common weak patterns and known weak passwords in the evaluation.
- Provides recommendations for stronger passwords based on the assessment.
- Securely prompts the user to enter the password without displaying it on the screen.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository to your local machine or download the script file.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

> python ps-checker-v2.py


4. Follow the prompts to enter the password you want to check.

5. The script will evaluate the strength of the password and display a recommendation.

## Security Considerations

- The script does not store or transmit any passwords. The evaluation is performed locally on your system.
- The user input for the password is securely handled without displaying it on the screen.

## Entropy

Entropy is used as a metric to estimate the strength of a password. It calculates the information content and randomness of the password based on the character sets used and the password length.

## Customization

- Weak Patterns: To customize the list of weak patterns, you can modify the `weak_patterns` list in the `is_weak_password()` function.

- Weak Passwords Wordlist: If you want to update or modify the wordlist of weak passwords, edit the `weak_passwords.txt` file, adding or removing passwords as needed. Each password should be on a separate line.

## Contributing

Contributions to the Password Strength Checker script are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

The Password Strength Checker script is released under the [Unlicense](http://unlicense.org/), a public domain dedication that allows you to use, modify, and distribute the script freely without any restrictions. See the `UNLICENSE` file for more information.

## Acknowledgements

