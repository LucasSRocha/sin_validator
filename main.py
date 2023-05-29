from argparse import ArgumentParser
from re import findall, sub


class SinValidator:
    @staticmethod
    def string_space_clean(string: str) -> str:
        return sub(r"\s", "", string)

    @staticmethod
    def _guarantee_only_digits(string: str) -> str:
        return not bool(findall(r"\D", string))

    @staticmethod
    def _lenght_validator(sin_string: str) -> bool:
        return len(sin_string) == 9

    @staticmethod
    def _sum_validator(sin_string: str) -> bool:
        sin_numbers = [int(i) for i in sin_string]
        nums_to_multiply = sin_numbers[1::2]  # slice list to get every 2nd number
        non_multiplied_nums = sin_numbers[::2]  # remaining numbers that don't get multiplied
        sin_multiplied_numbers = [SinValidator._sum_multiply_method(number) for number in nums_to_multiply]

        return SinValidator._divisible_validator(sum([*sin_multiplied_numbers, *non_multiplied_nums]))

    @staticmethod
    def _sum_multiply_method(num: int) -> int:
        resp = num * 2
        if resp > 9:
            return sum(int(i) for i in str(resp))
        return resp

    @staticmethod
    def _divisible_validator(num: int) -> bool:
        return num % 10 == 0

    @staticmethod
    def validate(sin_string: str) -> bool:
        validation_functions = (
            SinValidator._guarantee_only_digits,
            SinValidator._lenght_validator,
            SinValidator._sum_validator,
        )
        return all(func(sin_string) for func in validation_functions)


def main() -> None:
    parser = ArgumentParser(description="Validate if a SIN number is valid or not.")
    parser.add_argument(
        "sin_number",
        help="the SIN number to validate or a comma separated list of SIN numbers to validate. i.e. '123456789' or '123456789, 000000000'",
    )
    args = parser.parse_args()
    sin_numbers = {i.strip() for i in args.sin_number.split(",")}
    validation_message = "{number} is {valid} SIN number."
    for number in sin_numbers:
        valid_message = "a valid" if SinValidator.validate(number) else "an invalid"
        print(validation_message.format(number=SinValidator.string_space_clean(number), valid=valid_message))


if __name__ == "__main__":  # pragma: no cover
    main()
