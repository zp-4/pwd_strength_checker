# Password Strength Checker

The Password Strength Checker is a Python script that assesses the strength of passwords based on various criteria such as length, complexity, and common patterns. It calculates the entropy of a password to estimate its strength and provides recommendations for stronger passwords.

## Usage

1. Ensure you have Python installed on your system.
2. Download the `ps-checker.py` script from this repository.
3. Open a terminal or command prompt and navigate to the directory where the script is saved.
4. Run the script using the following command:
   > ps-checker.py
5. Follow the prompts to enter the password you want to check.
6. The script will evaluate the strength of the password and display a recommendation.

## Entropy Calculation

The script calculates the entropy of a password as a measure of its strength. Entropy refers to the randomness or unpredictability of the password. Higher entropy indicates a stronger password that is harder to guess or crack.

In this script, entropy is calculated based on the character sets used in the password: lowercase letters, uppercase letters, numbers, and special characters. Each character set adds to the total entropy based on whether it is present in the password.

The entropy calculation considers the length of the password as well. Longer passwords typically have higher entropy since there are more characters to guess. The script multiplies the entropy by the password length to adjust the overall entropy value.

## Recommendations

The script provides recommendations based on the assessed strength of the password. The recommendations are as follows:

- Weak password: Passwords with a length less than 8 characters, low entropy (less than 40), or matching common weak patterns are considered weak. It is recommended to choose a stronger password.
- Moderate password: Passwords with a length between 8 and 11 characters or moderate entropy (between 40 and 59) are considered moderate. It is recommended to consider increasing the length and complexity for better security.
- Strong password: Passwords with a length of 12 characters or more and high entropy (60 or above) are considered strong. Well done!

## Security Considerations

When running the script, keep the following security considerations in mind:

- Ensure you are running the script in a trusted and secure environment.
- Exercise caution when entering passwords, especially if running the script on a shared or public system.
- The script does not store or transmit any passwords. The evaluation is performed locally on your system.

## Contributing

Contributions to the Password Strength Checker script are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

The Password Strength Checker script is released under the [Unlicense](http://unlicense.org/). It is a public domain dedication that allows you to use, modify, and distribute the script freely without any restrictions. See the `UNLICENSE` file for more information.



